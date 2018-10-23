from app import log
from app.ws import bp
from app.api.auth import token_auth


@bp.route('/echo')
#@token_auth.login_required
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        log.debug("Message Receive %s", message)
        if message:
            ws.send(message)