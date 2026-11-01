
# GROUP COMMUNICATION SIMULATION
# Causal Ordering and Total Ordering
# Using Vector Clocks and Lamport Logical Clocks

class Process:
    def __init__(self, process_id, total_processes):
        self.process_id = process_id
        self.vector_clock = [0] * total_processes
        self.lamport_clock = 0

    def send_message(self, message):
        self.lamport_clock += 1
        self.vector_clock[self.process_id] += 1

        return {
            "message": message,
            "sender": f"P{self.process_id + 1}",
            "lamport": self.lamport_clock,
            "vector": self.vector_clock.copy()
        }

    def receive_message(self, msg):
        self.lamport_clock = max(
            self.lamport_clock, msg["lamport"]
        ) + 1

        for i in range(len(self.vector_clock)):
            self.vector_clock[i] = max(
                self.vector_clock[i], msg["vector"][i]
            )

        self.vector_clock[self.process_id] += 1

    def show_clock(self):
        print(
            f"{self.process_id + 1}: "
            f"Lamport={self.lamport_clock}, "
            f"Vector={self.vector_clock}"
        )


def happens_before(v1, v2):
    """Check whether vector clock v1 causally precedes v2."""
    less_or_equal = all(a <= b for a, b in zip(v1, v2))
    strictly_less = any(a < b for a, b in zip(v1, v2))
    return less_or_equal and strictly_less


# Create three distributed processes
p1 = Process(0, 3)
p2 = Process(1, 3)
p3 = Process(2, 3)

processes = [p1, p2, p3]
messages = []

print("===== GROUP COMMUNICATION SIMULATION =====")

# STEP 1: P1 sends the first message
m1 = p1.send_message("Exam date announced")
messages.append(m1)

# STEP 2: P3 sends an independent message
m2 = p3.send_message("Project submission reminder")
messages.append(m2)

# STEP 3: P2 receives P1's message
p2.receive_message(m1)

# STEP 4: P2 sends a message depending on M1
m3 = p2.send_message("I will start preparing")
messages.append(m3)

# Display generated messages
print("\n===== GENERATED MESSAGES =====")

for msg in messages:
    print(
        f'{msg["sender"]} | {msg["message"]} | '
        f'Lamport: {msg["lamport"]} | '
        f'Vector: {msg["vector"]}'
    )

# CAUSAL ORDERING
print("\n===== CAUSAL ORDERING =====")

if happens_before(m1["vector"], m3["vector"]):
    print("M1 causally precedes M3.")
    print("M1 must be delivered before M3.")

print("\nCausal message order:")

causal_order = sorted(
    messages,
    key=lambda msg: (sum(msg["vector"]), msg["sender"])
)

for msg in causal_order:
    print(f'{msg["sender"]}: {msg["message"]}')

# TOTAL ORDERING
print("\n===== TOTAL ORDERING =====")

total_order = sorted(
    messages,
    key=lambda msg: (msg["lamport"], msg["sender"])
)

print("\nGlobal delivery order:")

for index, msg in enumerate(total_order, start=1):
    print(
        f'{index}. {msg["sender"]}: '
        f'{msg["message"]} '
        f'(Timestamp: {msg["lamport"]})'
    )

# Every process receives the same global order
print("\n===== DELIVERY AT EACH PROCESS =====")

for process in processes:
    print(f"\nProcess P{process.process_id + 1} receives:")

    for msg in total_order:
        print(f'  {msg["message"]}')

print("\n===== SIMULATION COMPLETED =====")
