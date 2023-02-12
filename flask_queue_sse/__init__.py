#
#  A simple implementation of Server-Sent Events for Flask
#  that doesn't require Redis pub/sub.
#  Created On 21 November 2022
#

from re import search
from json import dumps
from queue import Queue, Full
from flask import Response


class ServerSentEvents:
    """A simple implementation of Server-Sent Events for Flask."""

    msg_id: int = 0
    listeners: list[Queue] = []

    def response(self):
        """Returns a response which can be passed to Flask server."""

        def stream():
            has_finished = False

            queue = Queue(5)
            self.listeners.append(queue)

            while has_finished == False:
                msg = queue.get()
                yield msg

                if search("event: end", msg) or search("event: error", msg):
                    has_finished = True

        return Response(stream(), mimetype="text/event-stream")

    def send(self, payload: dict = None, event: str = "data"):
        """Sends a new event to the opened channel."""

        self.msg_id = self.msg_id + 1

        msg_str = dumps(payload) if payload else "{}"
        msg = f"id: {self.msg_id}\nevent: {event}\ndata: {msg_str}\n\n"

        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except Full:
                del self.listeners[i]

        return self
