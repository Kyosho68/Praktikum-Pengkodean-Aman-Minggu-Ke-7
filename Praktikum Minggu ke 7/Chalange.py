from enum import Enum, auto


class TransferStatus(Enum):
    CREATED = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()


class SecureTransfer:

    def __init__(self, sender, receiver, amount):
        # Validasi saat objek dibuat
        if sender == receiver:
            raise ValueError("Sender dan receiver tidak boleh sama")

        if amount <= 0:
            raise ValueError("Amount harus lebih dari 0")

        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.status = TransferStatus.CREATED

    def transition(self, expected, next_status):
        if self.status != expected:
            raise ValueError(
                f"Invalid transition "
                f"{self.status.name} -> {next_status.name}"
            )

        old = self.status
        self.status = next_status

        print(f"{old.name} -> {self.status.name}")

    def process(self):
        self.transition(
            TransferStatus.CREATED,
            TransferStatus.PROCESSING
        )

    def complete(self):
        self.transition(
            TransferStatus.PROCESSING,
            TransferStatus.COMPLETED
        )

    def fail(self):
        self.transition(
            TransferStatus.PROCESSING,
            TransferStatus.FAILED
        )


print("=== SUCCESS CASE ===")

transfer = SecureTransfer(
    sender="alice",
    receiver="bob",
    amount=100000
)

transfer.process()
transfer.complete()

print(vars(transfer))


print("\n=== FAILURE CASE 1 ===")

try:
    bad_transfer = SecureTransfer(
        sender="alice",
        receiver="alice",
        amount=100000
    )
except ValueError as error:
    print("BLOCKED:", error)


print("\n=== FAILURE CASE 2 ===")

try:
    bad_transfer = SecureTransfer(
        sender="alice",
        receiver="bob",
        amount=-100000
    )
except ValueError as error:
    print("BLOCKED:", error)


print("\n=== FAILURE CASE 3 ===")

try:
    transfer2 = SecureTransfer(
        sender="alice",
        receiver="bob",
        amount=50000
    )

    # Langsung selesai tanpa diproses
    transfer2.complete()

except ValueError as error:
    print("BLOCKED:", error)