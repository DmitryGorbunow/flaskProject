from datetime import datetime, timedelta

from flask import Flask

app = Flask(__name__)

@app.route('/get_time/future')
def get_time_future():
    current_time = datetime.now()
    future_time = current_time + timedelta(hours=1)
    future_time_str = future_time.strftime("%Y-%m-%d %H:%M:%S")
    return f'Точное время через час будет: {future_time_str}'

if __name__ == '__main__':
    app.run(debug=True)