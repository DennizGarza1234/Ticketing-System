import time
import random
from ticket import Ticket
from ticket_queue import TicketQueue

def generate_tickets(queue, number_of_tickets):
    print("\n--- Generating Tickets ---")
    for i in range(1, number_of_tickets + 1):
        ticket = Ticket(i)
        queue.enqueue(ticket)
        print(f"Generated {ticket}")
        time.sleep(random.uniform(0.2, 0.6))

def process_tickets(queue):
    print("\n--- Processing Tickets ---")
    while not queue.is_empty():
        ticket = queue.dequeue()
        print(f"Serving {ticket}")
        time.sleep(random.uniform(0.5, 1.0))

if __name__ == "__main__":
    queue = TicketQueue()

    generate_tickets(queue, 5)
    process_tickets(queue)

    print("\nAll tickets processed.")