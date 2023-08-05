import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

# class TextRoomConsumer(WebsocketConsumer):
#     def connect(self):
#         print("\n\nconnect function")
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         print("\n\ndisconnected")
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     def receive(self, text_data):
#         # Receive message from WebSocket
#         print(f"\n\nreceived")
#         text_data_json = json.loads(text_data)
#         text = text_data_json['text']
#         sender = text_data_json['sender']
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': text,
#                 'sender': sender
#             }
#         )

#     def chat_message(self, event):
#         # Receive message from room group
#         text = event['message']
#         sender = event['sender']
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'text': text,
#             'sender': sender
#         }))

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

from asgiref.sync import async_to_sync

class TextRoomConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        # print("this is init function")
        self.messages = []
        super().__init__(*args, **kwargs)

    def connect(self):
        # print(f"self.scope: {self.scope}")
        print(f"{OKGREEN}\'connect\' method in \'TextRoomConsumer\' consumer{ENDC}")
        
        # settings group
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(f"self.channel_name: {self.channel_name}")
        print(f"self.room_group_name: {self.room_group_name}")

        self.accept()

        # self.send(text_data=json.dumps({
        #     'type': 'connection_established',
        #     'message': 'You are now connected!'
        # }))

        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(f"text_data_json: {text_data_json}")
        message = text_data_json['message']
        user = text_data_json['user']
        # self.messages.append(message)
        # print(f"message: {message}")
        # self.send(text_data=json.dumps({
        #     "messages": self.messages
        # }))
        # print(self.messages)
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
