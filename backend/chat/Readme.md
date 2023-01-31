# Chat

### It's the example how to make chat

___
### Changed files 
* settings.py:
  ```python
    ASGI_APPLICATION = "backend.asgi.application"
  CHANNEL_LAYERS = {
      "default": {
          "BACKEND": "channels_redis.core.RedisChannelLayer",
          "CONFIG": {
              "hosts": [("127.0.0.1", 6379)],
          },
      },
  }
  ```
* asgi.py:
  ```python
    application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
        )
    }
  )
  ```

--- 
### Dependencies:
* Django
    * (with daphne{ the server application that help to run websocket}) python -m pip install -U channels["daphne")
    * (without daphne) pip install channels
    * pip install channels_redis
* Vue
  


---
### Vue Project:
* Example:
  ```vue
    this.connection = new WebSocket('ws://127.0.0.1:8001/ws/chat/12/')
    this.connection.onmessage = (message) =>{
      console.log(message.data)
    } // receive message
    sendMessage(){
      this.connection.send(JSON.stringify({"message": this.message}))
      this.message = ''
    } // send message
  ```
---
### Additional Info
Docs: https://channels.readthedocs.io/en/stable/tutorial/part_2.html

Must download redis: ``docker pull redis`` and start it  `` docker run -p 6379:6379 -d redis``


