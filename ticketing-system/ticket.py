from datetime import datetime

class Ticket:
    def __init__(self, ticket_number):
        self.ticket_number = ticket_number
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"Ticket(number={self.ticket_number}, time={self.timestamp.strftime('%H:%M:%S')})"