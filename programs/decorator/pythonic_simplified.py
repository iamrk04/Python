# Video Link, after 17:20: https://www.youtube.com/watch?v=QH5fw9kxDQA


from typing import Callable, Any
import functools


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
        # call the function
        func(*args, **kwargs)
        # do something extra after the function call
        print(f"Sending Slack: {args[0]}")

    return wrapper


# Execution order of decorators is from top to bottom.
@send_slack
@send_sms
def send_email(message: str) -> None:
    """
    Send `message` via email to recipents.

    :param message: message to send
    """
    print(f"Sending email: {message}")


if __name__ == "__main__":
    mssg = "Welcome to the jungle!"

    # The client code can support simple send...
    print("----------Client: I've got a decorated function:-----------")
    send_email(mssg)
