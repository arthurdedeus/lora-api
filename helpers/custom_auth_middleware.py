from urllib import parse

from channels.auth import AuthMiddleware
from channels.db import database_sync_to_async
from channels.sessions import (
    CookieMiddleware,
    SessionMiddleware,
)
from django.contrib.auth.models import (
    AnonymousUser,
    User,
)


@database_sync_to_async
def get_user(scope):
    if "session" not in scope:
        raise ValueError(
            "Cannot find session in scope. You should wrap your consumer in SessionMiddleware.")
    user = None
    query_string = scope.get('query_string', '').decode()
    qs = parse.parse_qs(query_string)
    if 'token' in qs:
        user = User.objects.filter(auth_token__key=qs.get('token', [''])[0]).first()

    return user or AnonymousUser()


class CustomAuthMiddleware(AuthMiddleware):
    """
    Middleware which populates scope["user"] from a Django session.
    Requires SessionMiddleware to function.
    """

    async def resolve_scope(self, scope):
        scope["user"]._wrapped = await get_user(scope)


# Handy shortcut for applying all three layers at once
CustomAuthMiddlewareStack = lambda inner: CookieMiddleware(SessionMiddleware(CustomAuthMiddleware(inner)))
