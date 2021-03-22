from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/zad1', methods=('GET', 'POST'))
def zad1():
    return 'You said:{}'.format(request.form['freetext'])


@app.route('/zad2', methods=('GET', 'POST'))
def zad2():
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
    elif char == 'dzielenie' and b != 0:
        result = a / b
    elif char == 'dzielenie' and b == 0:
        result = 'error'

    return str(result)


@app.route('/zad3', methods=('GET', 'POST'))
def zad3():
    correctpass = "abc"
    writtenlog = request.form['login']
    writtenpass = request.form['pass']
    if correctpass == writtenpass:
        return render_template('index2.html')
    else:
        return render_template('index.html', value=writtenlog, value1='Incorrect Password')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
