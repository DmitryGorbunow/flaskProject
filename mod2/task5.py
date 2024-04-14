from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/max_number/10/2/9/1

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    num_list = numbers.split('/')
    if all(is_integer(num) for num in num_list):
        num_list = list(map(int, num_list))
        max_num = max(num_list)
        return f"Максимальное число: {max_num}"
    else:
        return "Ошибка: Введены некорректные данные. Пожалуйста, убедитесь, что переданные значения являются числами."

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    app.run(debug=True)