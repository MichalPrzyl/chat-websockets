from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from app.consumers import TextRoomConsumer


websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),  # 'room_name' can be accessed from 'consumers.py' classes in self.scope['kwargs'] I belive
]
