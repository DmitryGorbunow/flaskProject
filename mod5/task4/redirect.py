import sys
from typing import IO, Optional, Type, TypeVar, Union, ContextManager

T = TypeVar('T', bound=IO)


class RedirectContextManager:
    def __init__(self, stdout: Optional[T] = None, stderr: Optional[T] = None):
        self.stdout = stdout
        self.stderr = stderr
        self._stdout_backup = sys.stdout
        self._stderr_backup = sys.stderr

    def __enter__(self) -> "RedirectContextManager":
        if self.stdout:
            sys.stdout = self.stdout
        if self.stderr:
            sys.stderr = self.stderr
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException],
        exc_val: BaseException,
        exc_tb: Type[BaseException]
    ) -> Optional[bool]:
        sys.stdout = self._stdout_backup
        sys.stderr = self._stderr_backup
        return False

    def redirect_stdout(self, target: T) -> "RedirectContextManager":
        self.stdout = target
        return self

    def redirect_stderr(self, target: T) -> "RedirectContextManager":
        self.stderr = target
        return self


def redirect(
    stdout: Optional[T] = None,
    stderr: Optional[T] = None
) -> RedirectContextManager:
    return RedirectContextManager(stdout, stderr)


if __name__ == "__main__":

    print('Hello stdout')

    with open('stdout.txt', 'w') as stdout_file, open('stderr.txt', 'w') as stderr_file:
        with redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

    print('Hello stdout again')
    raise Exception('Hello stderr')
