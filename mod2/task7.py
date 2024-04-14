from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/add/20240404/437
# http://127.0.0.1:5000/calculate/2024
# http://127.0.0.1:5000/calculate/2024/04


expenses = {}

@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    # if len(date) != 8:
    #     raise ValueError("Invalid date format")
    year = int(date[:4])
    month = int(date[4:6])
    expenses.setdefault(year, {}).setdefault(month, 0)
    expenses[year][month] += number
    return f'Расход в размере {number} рублей на дату {date} добавлен успешно.'


@app.route('/calculate/<int:year>')
def calculate_year(year):
    total_expenses = sum(expenses.get(year, {}).values())
    return f'Суммарные траты за {year} год: {total_expenses} рублей.'


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    total_expenses = expenses.get(year, {}).get(month, 0)
    return f'Суммарные траты за {month}/{year}: {total_expenses} рублей.'


if __name__ == '__main__':
    app.run(debug=True)
