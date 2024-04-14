from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/hello_world/Дима

@app.route('/hello_world/<name>')
def hello_world(name) -> str:
    from datetime import datetime
    weekday = datetime.today().weekday()
    weekday_name = get_weekday_name(weekday)
    return f"Привет, {name}, {weekday_name}!"

def get_weekday_name(weekday):
    weekdays = {
        0: 'хорошего понедельника',
        1: 'хорошего вторника',
        2: 'хорошей среды',
        3: 'хорошего четверга',
        4: 'хорошей пятницы',
        5: 'хорошей субботы',
        6: 'хорошего воскресенья'
    }

    return weekdays.get(weekday)

if __name__ == '__main__':
    app.run(debug=True)