from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
from django.apps import AppConfig


class SendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'send'
# SENDFILE_FALLBACK_READBUFFER_SIZE