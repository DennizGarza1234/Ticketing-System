# Ticketing-System

## Overview
This project simulates a service center ticketing system using a Queue (FIFO).

---

Customers:
1. Take a ticket
2. Wait in queue
3. Are served in order

---

## Features
- Ticket class with number and timestamp
- Queue implementation using deque
- Randomized ticket arrival and service time
- Unit tests (normal and edge cases)
- Flowchart diagram included

---

## How to Run

### Run Simulation
python main.py

### Run Tests
```
python -m unittest discover tests
```
---

## Time Complexity
- Enqueue: O(1)
- Dequeue: O(1)
- Overall: O(n)

## Space Complexity
- O(n)

---

## Youtube
