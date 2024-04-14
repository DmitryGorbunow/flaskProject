import os
import signal
import subprocess

from flask import Flask
app = Flask(__name__)


def check():
    process = subprocess.Popen(["lsof", "-i", f":5000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, error = process.communicate()

    to_kill = None

    for line in output.splitlines():
        parts = line.decode().split()
        if parts[0] == 'Python':
            to_kill = int(parts[1])

    if to_kill is not None:
        return to_kill
    else:
        return None


def kill(pid):
    os.kill(pid, signal.SIGKILL)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":

    if check() is not None:
        kill(check())
    app.run()
