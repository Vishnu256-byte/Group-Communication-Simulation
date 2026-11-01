
class Message:
    def __init__(self, sender, content, timestamp):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp


class CausalProcess:
    def __init__(self, process_id, total_processes):
        self.process_id = process_id
        self.clock = [0] * total_processes
        self.pending = []
        self.delivered = []

    def send_message(self, content):
        self.clock[self.process_id] += 1

        message = Message(
            self.process_id,
            content,
            self.clock.copy()
        )

        self.delivered.append(message)
        return message

    def can_deliver(self, message):
        sender = message.sender
        timestamp = message.timestamp

        # Sender's next message must be received
        if timestamp[sender] != self.clock[sender] + 1:
            return False

        # All causal dependencies must already be received
        for i in range(len(self.clock)):
            if i != sender and timestamp[i] > self.clock[i]:
                return False

        return True

    def receive_message(self, message):
        self.pending.append(message)
        self.process_pending()

    def process_pending(self):
        progress = True

        while progress:
            progress = False

            for message in self.pending[:]:
                if self.can_deliver(message):
                    for i in range(len(self.clock)):
                        self.clock[i] = max(
                            self.clock[i],
                            message.timestamp[i]
                        )

                    self.delivered.append(message)
                    self.pending.remove(message)

                    print(
                        f"P{self.process_id + 1} delivered "
                        f"{message.content}"
                    )

                    progress = True
