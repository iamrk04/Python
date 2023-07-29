# Example taken from: https://refactoring.guru/design-patterns/decorator

from abc import ABC, abstractmethod


class Notifier(ABC):
    """The Notifier interface declares a set of methods for sending notifications."""

    @abstractmethod
    def send(self, message: str) -> None:
        """
        Send `message` to recipents.

        :param message: message to send
        """
        pass


class EmailNotifier(Notifier):
    """The Email Notifier class for sending notification via email."""

    def send(self, message: str) -> None:
        """
        Send `message` via email to recipents.

        :param message: message to send
        """
        print(f"Sending email: {message}")


class BaseNotifierDecorator(Notifier):
    """The Base Notifier Decorator class for sending notification."""

    def __init__(self, notifier: Notifier) -> None:
        """
        Initialize the BaseNotifierDecorator.

        :param notifier: the notifier to decorate
        """
        self._notifier = notifier

    def send(self, message: str) -> None:
        """
        Send `message` to recipents.

        :param message: message to send
        """
        self._notifier.send(message)


class SMSNotifier(BaseNotifierDecorator):
    """The SMS Notifier Decorator class for sending notification via SMS."""

    def send(self, message: str) -> None:
        """
        Send `message` via SMS to recipents.

        :param message: message to send
        """
        super().send(message)
        print(f"Sending SMS: {message}")


class SlackNotifier(BaseNotifierDecorator):
    """The Slack Notifier Decorator class for sending notification via Slack."""

    def send(self, message: str) -> None:
        """
        Send `message` via Slack to recipents.

        :param message: message to send
        """
        super().send(message)
        print(f"Sending Slack: {message}")


if __name__ == "__main__":
    mssg = "Welcome to the jungle!"

    # The client code can support simple components...
    email_notifier = EmailNotifier()
    print("Client: I've got a simple component:")
    email_notifier.send(mssg)

    print()

    # ...as well as decorated ones.
    # Note how decorators can wrap not only simple components but the other decorators as well.
    sms_notifier = SMSNotifier(email_notifier)
    slack_notifier = SlackNotifier(sms_notifier)
    print("Client: Now I've got a decorated component:")
    slack_notifier.send(mssg)
