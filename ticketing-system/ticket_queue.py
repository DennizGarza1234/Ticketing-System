from collections import deque

class TicketQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, ticket):
        self.queue.append(ticket)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty queue.")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)