# Video Link, after 17:20: https://www.youtube.com/watch?v=QH5fw9kxDQA


from typing import Callable, Any
import functools


def send_email(message: str) -> None:
    """
    Send `message` via email to recipents.

    :param message: message to send
    """
    print(f"Sending email: {message}")


def send_sms(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator for sending SMS notification.

    :param func: the function to decorate
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(
            f"Calling `{func.__name__}` from `send_sms` with args: {args} and kwargs: {kwargs}"
        )
        func(*args, **kwargs)
        print(f"Sending SMS: {args[0]}")

    return wrapper


def send_slack(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator for sending SMS notification.

    :param func: the function to decorate
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(
            f"Calling `{func.__name__}` from `send_slack` with args: {args} and kwargs: {kwargs}"
        )
        func(*args, **kwargs)
        print(f"Sending Slack: {args[0]}")

    return wrapper


if __name__ == "__main__":
    mssg = "Welcome to the jungle!"

    # The client code can support simple send...
    print("----------Client: I've got a simple function:-----------")
    send_email(mssg)

    print()

    # ...as well as decorated ones.
    # Note how decorators can wrap not only simple functions but the other decorators as well.
    send_sms_decorator = send_sms(send_email)
    send_slack_decorator = send_slack(send_sms_decorator)
    print("---------Client: Now I've got a decorated function:---------")
    send_slack_decorator(mssg)
