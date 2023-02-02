import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Room, Message, User
from .serializer import MessageSerializer, RoomSerializer



class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def IsRoomExist(self):
        return Room.objects.filter(name=self.room_name).count()

    @database_sync_to_async
    def save_room(self):
        data = {'name': self.room_name}
        room = RoomSerializer(data=data)
        room.is_valid()
        room.save()

    @database_sync_to_async
    def get_room(self):
        room = Room.objects.get(name=self.room_name)
        return room


    @database_sync_to_async
    def add_user(self):
        self.room_object.current_users.add(self.user_id)

    @database_sync_to_async
    def remove_user(self):
        self.room_object.current_users.remove(self.user_id)


    @database_sync_to_async
    def get_user_id(self):
        return User.objects.get(phone=self.username).id

    @database_sync_to_async
    def get_user_object(self):
        return User.objects.get(phone=self.username)

    @database_sync_to_async
    def save_message(self, data):
        text = data['text']
        user = data['user']
        room = data['room']
        Message.objects.create(text=text, user=user, room=room)

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        if not(await self.IsRoomExist()):
            await self.save_room()

        self.room_object = await self.get_room()

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        await self.remove_user()

    async def receive(self, text_data=None, bytes_data=None):

        text_data_json = json.loads(text_data)
        print(text_data_json)
        if 'type' in text_data_json and text_data_json['type'] == "Init":
            self.username = text_data_json['username']
            self.user_id = await self.get_user_id()
            self.user_object = await self.get_user_object()
            await self.add_user()
            return
        user = text_data_json['user']
        message = text_data_json['message']
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'user': user}
        )
        message_data = {'text': message, 'user': self.user_object, 'room': self.room_object}
        await self.save_message(message_data)


    async def Init(self, event):
        print(event)

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        await self.send(text_data=json.dumps({'message': message, 'user': user}))