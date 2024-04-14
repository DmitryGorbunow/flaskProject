from flask import Flask

app = Flask(__name__)

@app.route('/hello/world')
def get_hello_world():
    return 'Привет, мир!'

if __name__ == '__main__':
    app.run(debug=True)