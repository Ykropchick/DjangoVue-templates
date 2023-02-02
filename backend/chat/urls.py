
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RoomsViewSet, MessagesViewSet

router = DefaultRouter()
router.register('rooms', RoomsViewSet, basename='rooms')

urlpatterns = [
    path('', include(router.urls)),
    path('messages/<str:room_name>/', MessagesViewSet.as_view())
]