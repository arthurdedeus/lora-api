"""
WS Consumers
"""
###
# Libraries
###
import json
import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer as BasicWebsocketConsumer
from django.core.cache import cache

from settings.settings import ENVIRONMENT

logger = logging.getLogger('websockets')


###
# Consumers
###
class WebsocketConsumer(BasicWebsocketConsumer):
    ###
    # Connection
    ###
    def connect(self):
        if self.scope.get('user').is_authenticated:
            async_to_sync(self.channel_layer.group_add)(
                f'websocket-{ENVIRONMENT}',
                self.channel_name,
            )
            self.accept()
            user = self.scope.get('user')
            cached_info = json.loads(cache.get(user.id, default='[]'))
            cached_info.append(self.channel_name)
            cache.set(user.id, json.dumps(cached_info), timeout=None)
            logger.info(f'User {user.email} has opened a WebSocket.')
        else:
            self.close(code=403)

    def disconnect(self, message):
        async_to_sync(self.channel_layer.group_discard)(
            f'websocket-{ENVIRONMENT}',
            self.channel_name,
        )
        if self.scope.get('user').is_authenticated:
            user = self.scope.get('user')
            cached_info = json.loads(cache.get(user.id, default='[]'))
            try:
                cached_info.remove(self.channel_name)
            except ValueError:
                pass
            cache.set(user.id, json.dumps(cached_info), timeout=None)
            logger.info(f'User {user.email} has closed a WebSocket.')

    ###
    # Internal methods
    ###
    def __check_user_on_cache(self):
        user = self.scope.get('user')
        cached_info = json.loads(cache.get(user.id, default='[]'))
        if self.channel_name not in cached_info:
            cached_info.append(self.channel_name)
            cache.set(user.id, json.dumps(cached_info), timeout=None)
            logger.info(f'Re-adding {user.email} to cache.')

    ###
    # Notification methods
    ###
    def send_notification(self, event):
        self.__check_user_on_cache()
        send_notification(self, event)

    def send_allocation_update(self, event):
        send_allocation_update(self, event)
