import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


OKGREEN = '\033[92m'
ENDC = '\033[0m'


class TextRoomConsumer(WebsocketConsumer):
    def connect(self):
        print(f"{OKGREEN}\'connect\' method in \'TextRoomConsumer\' consumer{ENDC}")
        
        # settings group
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['user']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user
            }
        )
        
    def chat_message(self, event):
        message = event['message']
        user = event['user']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'user': user
        }))
