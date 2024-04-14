from flask import Flask

app = Flask(__name__)

counter = 0

@app.route('/counter')
def get_counter():
    global counter
    counter = counter + 1
    return str(counter)


if __name__ == '__main__':
    app.run(debug=True)