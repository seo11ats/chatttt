from django.urls import path, include
from ChildChat.consumer import ChatConsumer

# the empty string routes to ChatConsumer, which manages the chat functionality.
websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]