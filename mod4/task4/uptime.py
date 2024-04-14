import subprocess

from flask import Flask

app = Flask(__name__)


def get_system_uptime():
    uptime_process = subprocess.Popen(["uptime"], stdout=subprocess.PIPE)
    uptime_output, _ = uptime_process.communicate()
    uptime_str = uptime_output.decode().strip()
    uptime = uptime_str.split("up ")[1].split(",")[0]
    return uptime


@app.route('/uptime')
def uptime():
    return f"Current uptime is {get_system_uptime()}"


if __name__ == "__main__":
    app.run(debug=True)
