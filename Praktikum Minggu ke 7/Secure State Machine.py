from enum import Enum, auto


class OrderState(Enum):
    CREATED = auto()
    PAID = auto()
    SHIPPED = auto()
    DELIVERED = auto()


class Order:

    def __init__(self):
        self.state = OrderState.CREATED

    def transition(self, expected, next_state):

        if self.state != expected:
            raise ValueError(
                f"Invalid transition "
                f"{self.state.name} -> {next_state.name}"
            )

        old = self.state
        self.state = next_state

        print(f"{old.name} -> {self.state.name}")

    def pay(self):
        self.transition(OrderState.CREATED, OrderState.PAID)

    def ship(self):
        self.transition(OrderState.PAID, OrderState.SHIPPED)

    def deliver(self):
        self.transition(OrderState.SHIPPED, OrderState.DELIVERED)


print("=== SUCCESS CASE ===")

order = Order()

order.pay()
order.ship()
order.deliver()

print("Final state:", order.state.name)

print("\n=== FAILURE CASE ===")

bad_order = Order()

try:
    bad_order.deliver()
except ValueError as error:
    print("BLOCKED:", error)

print("Current state:", bad_order.state.name)
