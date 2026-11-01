
class TotalOrderSystem:
    def __init__(self, total_processes):
        self.total_processes = total_processes
        self.sequence_number = 0
        self.processes = {
            i: {
                "expected": 1,
                "pending": {},
                "delivered": []
            }
            for i in range(total_processes)
        }

    def broadcast(self, sender, content):
        self.sequence_number += 1

        message = {
            "sender": sender,
            "content": content,
            "sequence": self.sequence_number
        }

        print(
            f"\nP{sender + 1} broadcasts {content} "
            f"with sequence number {self.sequence_number}"
        )

        return message

    def receive(self, process_id, message):
        process = self.processes[process_id]

        seq = message["sequence"]
        process["pending"][seq] = message

        self.deliver_pending(process_id)

    def deliver_pending(self, process_id):
        process = self.processes[process_id]

        while process["expected"] in process["pending"]:
            seq = process["expected"]

            message = process["pending"].pop(seq)

            process["delivered"].append(message["content"])

            print(
                f"P{process_id + 1} delivered "
                f"{message['content']} "
                f"(sequence {seq})"
            )

            process["expected"] += 1
