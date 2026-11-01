
from causal_order import CausalProcess
from total_order import TotalOrderSystem


def causal_simulation():
    print("\n========== CAUSAL ORDERING ==========\n")

    processes = [
        CausalProcess(i, 3)
        for i in range(3)
    ]

    # P1 sends M1
    m1 = processes[0].send_message("M1")

    # P2 receives M1 and then sends M2
    processes[1].receive_message(m1)
    m2 = processes[1].send_message("M2")

    # P3 receives M2 before M1
    print("\nP3 receives M2 first:")
    processes[2].receive_message(m2)

    print("\nP3 receives M1:")
    processes[2].receive_message(m1)

    # P1 also receives M2
    processes[0].receive_message(m2)

    print("\nFinal causal delivery order:")

    for process in processes:
        print(
            f"P{process.process_id + 1}: "
            f"{[m.content for m in process.delivered]}"
        )


def total_simulation():
    print("\n========== TOTAL ORDERING ==========\n")

    system = TotalOrderSystem(3)

    # Three processes broadcast messages
    m1 = system.broadcast(0, "M1")
    m2 = system.broadcast(1, "M2")
    m3 = system.broadcast(2, "M3")

    messages = [m1, m2, m3]

    # Simulate different network arrival orders
    arrival_orders = [
        [m3, m1, m2],
        [m2, m3, m1],
        [m1, m3, m2]
    ]

    for process_id in range(3):
        print(f"\nMessages arriving at P{process_id + 1}:")

        for message in arrival_orders[process_id]:
            print(
                f"Received {message['content']} "
                f"(sequence {message['sequence']})"
            )

            system.receive(process_id, message)

    print("\nFinal total delivery order:")

    for process_id, process in system.processes.items():
        print(
            f"P{process_id + 1}: "
            f"{process['delivered']}"
        )


if __name__ == "__main__":
    causal_simulation()
    total_simulation()
