# Flask-WebsocketChat

This python Flask app will interact with the websocket server.

* This app supports registered users send their message or files to the backend websocket server. Now, the websocket just ehcoes the message back, later it can support more functions.
* The app uses BluePrint to separate view functions and application, which makes it more flexible to change the endpoints without
the alteration of the application.
* The concurrency is achieved by coroutine library ``gevent``
* Websocket server is implemented by ``gevent-websocket``
* ``Flask-Sockets`` simply wraps the low-level ``gevent-websocket`` details. 
The websocket interface that is passed into your routes is provided by gevent-websocket. The basic methods are fairly straightforward — ``send``, ``receive``, ``send_frame``, and ``close``.
* The app uses json format wraps the messages transfered between client and server.
```
{
"type":"message/byte",
"text":"actual messages",
"id":"some ID",
"date":unix_timestamp
}
``` 
To install the dependencies, using the provided ``requirements,txt``
```
pip install -r requirements.txt
```

Then, in order to launch the server, the gunicorn is used to support websoket & gevent.
```
gunicorn -k flask_sockets.worker wschat:app
```
