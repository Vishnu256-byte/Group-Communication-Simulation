# Group-Communication-Simulation
Simulation of causal ordering and total ordering in distributed systems using Python

# Group Communication Simulation

## Project Description

This project demonstrates group communication
among multiple distributed processes using:

1. Causal Ordering
2. Total Ordering

The simulation is implemented using Python.

## Algorithms Used

### 1. Causal Ordering

Causal ordering ensures that messages are delivered
according to their causal dependencies.

Vector clocks are used to track message dependencies.

### 2. Total Ordering

Total ordering ensures that all distributed
processes deliver messages in the same order.

A centralized sequencer assigns sequence numbers
to the messages.

## Technologies Used

- Python
- Visual Studio Code
- Git
- GitHub

## Project Structure

Group-Communication-Simulation/
- main.py
- causal_order.py
- total_order.py
- README.md
- requirements.txt

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Execute:

```bash
python main.py
```

## Expected Result

The simulation demonstrates that:

- Causal dependencies are maintained.
- All processes deliver messages in the same total order.

## Conclusion

This project demonstrates two important
group communication ordering techniques
used in distributed systems.

