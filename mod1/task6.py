import random
import string

from flask import Flask

app = Flask(__name__)

@app.route('/get_random_word')
def get_random_word():
    random_word = random.choice(read_war_and_peace())
    return f'Случайное слово из "Войны и мира": {random_word}'

def read_war_and_peace():
    with open('files/war_and_peace.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    table = str.maketrans('', '', string.punctuation)
    words = [word.translate(table) for word in words]

    words = [word for word in words if word]

    return words


if __name__ == '__main__':
    app.run(debug=True)