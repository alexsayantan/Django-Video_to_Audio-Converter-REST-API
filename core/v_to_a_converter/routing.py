from django.urls import re_path
from . import consumers  # replace with your actual consumers module


websocket_urlpatterns = [
    re_path(r'ws/progress/(?P<video_id>\w+)/$', consumers.ProgressConsumer.as_asgi()),
]

