"""
Example of how to use domain-events in your project.
"""

from dataclasses import dataclass

from domain_events.base import DomainEvent
from domain_events.system import DomainEventSystem


# 1. Define YOUR project-specific events
@dataclass(frozen=True)
class UserRegisteredEvent(DomainEvent):
    event_type: str = "user.registered"  # Each project defines its own types
    user_id: int
    email: str


@dataclass(frozen=True)
class OrderCreatedEvent(DomainEvent):
    event_type: str = "order.created"
    order_id: int
    amount: float


# 2. Define YOUR project-specific handlers
def send_welcome_email(event: UserRegisteredEvent):
    print(f"📧 Sending welcome email to: {event.email}")


def process_payment(event: OrderCreatedEvent):
    print(f"💳 Processing payment: {event.amount}")


def track_analytics(event: DomainEvent):
    print(f"📊 Tracking event: {event.event_type}")


# 3. Configure the system with YOUR events
def setup_my_events(system: DomainEventSystem):
    """Project-specific configuration."""
    system.register_event(
        "user.registered",
        UserRegisteredEvent,
        [
            (send_welcome_email, {"async": True}),
            (track_analytics, {"async": False}),
        ],
    )

    system.register_event(
        "order.created",
        OrderCreatedEvent,
        [
            (process_payment, {"async": False}),
            (track_analytics, {"async": True}),
        ],
    )


# 4. Usage in your application
if __name__ == "__main__":
    system = DomainEventSystem()
    setup_my_events(system)

    # Publish events
    user_event = UserRegisteredEvent(user_id=1, email="test@example.com")
    system.publish(user_event)

    order_event = OrderCreatedEvent(order_id=123, amount=99.99)
    system.publish(order_event)

    print("✅ System configured successfully")
