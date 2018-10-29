import gevent
from gevent.queue import Queue
from app import log


class ChatRoom(object):

    def __init__(self):
        self.users = set()
        self.queue = Queue()

    def backlog(self, size=25):
        return self.queue[-size:]

    def subscribe(self, user):
        self.users.add(user)

    def add(self, message):
        self.queue.put(message, block=True, timeout=1)

    def run(self):
        """Listens for new messages in Redis, and sends them to clients."""
        while True:
            for message in self.queue:
                for client in self.users:
                    gevent.spawn(self.send, client, message)
                    log.debug("sending %s, msg: %s", client, message)
            gevent.sleep(0.1)

    def send(self, client, data):
        """Send given data to the registered client.
        Automatically discards invalid connections."""
        try:
            client.send(data)
        except Exception:
            self.users.remove(client)

    def start(self):
        """BackGround Chat Send"""
        gevent.spawn(self.run)
