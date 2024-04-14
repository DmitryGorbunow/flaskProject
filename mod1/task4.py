import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'Точное время: {current_time}'

if __name__ == '__main__':
    app.run(debug=True)