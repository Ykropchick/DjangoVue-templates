from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
  path('userditail/<int:pk>/', UserDitail.as_view())
]
