from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/example', methods=('GET', 'POST'))
def example():
    a = float(request.form['firstnumber'])
    b = float(request.form['secondnumber'])
    char = (request.form['znaki'])
    result = 0

    if char == 'dodawanie':
        result = a + b
    elif char == 'odejmowanie':
        result = a - b
    elif char == 'mnozenie':
        result = a * b
    elif char == 'dzielenie':
        result = a / b

    return str(result)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
