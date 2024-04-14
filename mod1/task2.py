from flask import Flask

app = Flask(__name__)

cars = 'Chevrolet, Renault, Ford, Lada.'

@app.route('/cars')
def get_cars():
    return cars

if __name__ == '__main__':
    app.run(debug=True)