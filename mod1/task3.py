import random

from flask import Flask

app = Flask(__name__)

cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

@app.route('/cats')
def get_cats():
    random_cat = random.choice(cats)
    return random_cat


if __name__ == '__main__':
    app.run(debug=True)