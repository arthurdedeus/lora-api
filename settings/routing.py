from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from django.core.asgi import get_asgi_application

from helpers.custom_auth_middleware import CustomAuthMiddlewareStack
from .consumer import (
    WebsocketConsumer,
)

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": CustomAuthMiddlewareStack(
            URLRouter(
                [
                    # Applications
                    re_path(r"^ws/$", WebsocketConsumer.as_asgi()),
                ]
            ),
        ),
    }
)
