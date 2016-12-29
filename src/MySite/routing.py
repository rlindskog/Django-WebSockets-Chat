from channels.routing import route, include
from home.consumers import chat_connect, chat_message, chat_disconnect

chat_routing = [
    route('websocket.connect', chat_connect),
    route('websocket.receive', chat_message),
    route('websocket.disconnect', chat_disconnect)
]

# messages...
# from channels.routing import route
# from home.consumers import http_consumer, ws_connect, ws_message, ws_disconnect
#
# channel_routing = [
#     # route('http.request', http_consumer),
#     route('websocket.connect', ws_connect),
#     route('websocket.receive', ws_message),
#     route('websocket.disconnect', ws_disconnect)
# ]
