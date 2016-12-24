from channels import Group
from channels.sessions import channel_session
from .models import Messages
import json

@channel_session
def ws_connect(message):
    prefix, room = message['path'].strip('/').split('/')
    # room = Room.objects.get(label=label)
    Group("chat-" + room, channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['room'] = room
    # import pdb; pdb.set_trace()

@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    # room = Room.objects.get(label=label)
    data = json.loads(message['text'])
    m = Messages.objects.create(handle=data['handle'], message=data['message'])
    Group('chat-'+label).send({'text': json.dumps(m.as_dict())})

def ws_disconnect(message):
    Group("chat-" + message.channel_session['room']).discard(message.reply_channel)
