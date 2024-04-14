import os

from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/preview/100/app.py

@app.route('/preview/<int:size>/<path:rel_path>')
def preview(size, rel_path):
    abs_path = os.path.abspath(rel_path)
    with open(abs_path, 'r', encoding='utf-8') as file:
        text = file.read(size)

    return f"<b>{abs_path}</b> {len(text)} <br/> {text}"

if __name__ == '__main__':
    app.run(debug=True)