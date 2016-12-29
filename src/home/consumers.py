from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session



# Connected to websocket.connect

@channel_session
def chat_connect(message):
    room = message.content['path'].strip("/")
    message.channel_session['room'] = room
    Group('chat-%s' % room).add(message.reply_channel)

# Connected to websocket.recieve
@channel_session
def chat_message(message):
    Group('chat-%s' % message.channel_session['room']).send({
        'text': message.content['text']
    })

# Connected to websocket.disconnect
@channel_session
def chat_disconnect(message):
    Group('chat-%s' % message.channel_session['room']).discard(message.reply_channel)
