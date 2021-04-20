from flask import Flask, render_template

app = Flask(__name__)
USERS = [
    ("uzytkownik1",1),
    ("uzytkownik2",2),
    ("uzytkownik3",3),
]


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/calculator/<string:char>/<int:a>/<int:b>', methods=('GET', 'POST'))
def calculator(char,a,b):
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


@app.route("/user/<int:user_id>")
def user(user_id):
    x = [x for x in USERS if x[1]==user_id]
    if x:
        return str(x[0])
    else:
        return "Brak uzytkownika w bazie!"


if __name__ == '__main__':
    app.run()
