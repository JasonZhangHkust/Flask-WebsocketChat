import gevent
from app import log
from app.ws import bp
from app.api.auth import token_auth
from app.ChatBackend import ChatRoom


chatRoom = ChatRoom()


@bp.route('/echo')
#@token_auth.login_required
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        log.debug("Message Receive %s", message)
        if message:
            ws.send(message)


@bp.route('/submit')
def inbox(ws):
    """Receives incoming chat messages, inserts them into Redis."""
    while not ws.closed:
        # Sleep to prevent *constant* context-switches.
        gevent.sleep(0.1)
        message = ws.receive()
        log.debug(u'Inserting message: {}'.format(message))
        if message:
            chatRoom.add(message)


@bp.route('/receive')
def outbox(ws):
    chatRoom.subscribe(ws)
    while not ws.closed:
        gevent.sleep(0.1)