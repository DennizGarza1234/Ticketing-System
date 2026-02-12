# Ticketing System Flowchart

```mermaid
flowchart TD

    A[Start] --> B[Create TicketQueue]

    B --> C[Generate Tickets Phase]

    C --> D[Create Ticket Object]
    D --> E[Enqueue Ticket]
    E --> F{More Tickets?}

    F -- Yes --> D
    F -- No --> G[Process Tickets Phase]

    G --> H{Queue Empty?}
    H -- No --> I[Dequeue Ticket]
    I --> J[Display Ticket Details]
    J --> H

    H -- Yes --> K[End]