from flask import Flask, render_template, request, redirect, session
from modules.money import Money
from modules.user import User
from modules.database import Database
app = Flask(__name__)
app.secret_key = "kevin@test.com"
Database.initialize()


@app.route("/")
def home():
    moneydict, position = Money.search_data()
    return render_template("home.html", moneydict=moneydict)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['InputName']
        email = request.form['InputEmail']
        password = request.form['InputPassword']
        result = User.register_user(name, email, password)
        if result is True:
            session['email'] = email
            session['name'] = name
            return redirect("/")
        else:
            message = "This email is already existed"
            return render_template("register.html", message=message)
    else:
        return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['InputEmail']
        password = request.form['InputPassword']
        result = User.check_user(email, password)
        if result is True:
            session['email'] = email
            session['name'] = User.find_user_data(email)['name']
            return redirect("/")
        else:
            message = "Input email or password is incorrect"
            return render_template("login.html", message=message)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session['email'] = None
    session['name'] = None
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=4101)