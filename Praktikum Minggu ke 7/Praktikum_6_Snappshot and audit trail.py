from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class AuditRecord:
    time: str
    actor: str
    old_state: str
    new_state: str


ALLOWED_TRANSITIONS = {
    "CREATED": ["PENDING"],
    "PENDING": ["PAID"],
    "PAID": ["SETTLED"],
}


class Payment:

    def __init__(self):
        self.state = "CREATED"
        self.audit_log = []

    def change_state(self, new_state, actor):

        allowed = ALLOWED_TRANSITIONS.get(self.state, [])

        if new_state not in allowed:
            raise ValueError(
                f"Invalid transition "
                f"{self.state} -> {new_state}"
            )

        record = AuditRecord(
            time=datetime.now().isoformat(timespec="seconds"),
            actor=actor,
            old_state=self.state,
            new_state=new_state
        )

        self.audit_log.append(record)

        self.state = new_state


print("=== SUCCESS CASE ===")

payment = Payment()

payment.change_state("PENDING", "backend-api")
payment.change_state("PAID", "payment-gateway")
payment.change_state("SETTLED", "settlement-service")

print("Final state:", payment.state)

print("\n=== FAILURE CASE ===")

bad_payment = Payment()

try:
    bad_payment.change_state(
        "SETTLED",
        "admin"
    )
except ValueError as error:
    print("BLOCKED:", error)

print("\nAudit log:")

for log in payment.audit_log:
    print(log)
