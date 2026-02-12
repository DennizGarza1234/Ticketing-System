import unittest
from ticket_queue import TicketQueue
from ticket import Ticket


class TestTicketQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = TicketQueue()
        ticket = Ticket(1)
        queue.enqueue(ticket)
        self.assertEqual(queue.size(), 1)

    def test_dequeue(self):
        queue = TicketQueue()
        ticket = Ticket(1)
        queue.enqueue(ticket)
        removed = queue.dequeue()
        self.assertEqual(removed.ticket_number, 1)

    def test_fifo_order(self):
        queue = TicketQueue()
        queue.enqueue(Ticket(1))
        queue.enqueue(Ticket(2))
        self.assertEqual(queue.dequeue().ticket_number, 1)
        self.assertEqual(queue.dequeue().ticket_number, 2)

    def test_dequeue_empty_queue(self):
        queue = TicketQueue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_peek_empty_queue(self):
        queue = TicketQueue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_size_empty_queue(self):
        queue = TicketQueue()
        self.assertEqual(queue.size(), 0)


if __name__ == "__main__":
    unittest.main()
