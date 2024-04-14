from contextlib import contextmanager


class BlockErrors:
    def __init__(self, ignored_errors):
        self.ignored_errors = ignored_errors

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            if exc_type in self.ignored_errors:
                return True
            else:
                return False
        else:
            return True  

if __name__ == '__main__':
    err_types = {ZeroDivisionError, TypeError}
    with BlockErrors(err_types):
        a = 1 / 0
    print('Выполнено без ошибок')