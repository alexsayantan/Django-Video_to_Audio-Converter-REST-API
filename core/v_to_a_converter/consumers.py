from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.video_id = self.scope['url_route']['kwargs']['video_id']
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        progress = text_data_json['progress']

        # Send progress to WebSocket
        await self.send(text_data=json.dumps({
            'progress': progress
        }))
