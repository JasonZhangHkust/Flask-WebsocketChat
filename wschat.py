#!/usr/bin/env python

import os
from app import create_app, db
from app.models import User, Post
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    WsServer = pywsgi.WSGIServer(('', 8000), app, handler_class=WebSocketHandler)
    WsServer.serve_forever()

