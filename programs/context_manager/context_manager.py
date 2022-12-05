class LoggingContextManager:

    def __enter__(self):
        print("LoggingContextManager.__enter__()")
        return "You are in a with-block"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("LoggingContextManger.__exit__(): "
                  "normal exit detected")
        else:
            print("LoggingContextManager.__exit__(): "
                  "Exception detected! "
                "type={}, value={}, traceback={}".format(
                    exc_type, exc_val, exc_tb))
        # return True
        return False


if __name__ == "__main__":
    with LoggingContextManager() as x:
        print(x)
    
    print("----------------------------------------")

    with LoggingContextManager() as x:
        raise ValueError(x)

