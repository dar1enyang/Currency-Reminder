from flask import Flask, render_template, request, redirect, session
from modules.money import Money
from modules.user import User
from modules.database import Database
from modules.all_alert import All_alert
from modules.job_check import check_alert
from apscheduler.schedulers.background import BackgroundScheduler



app = Flask(__name__)
app.secret_key = "kevin@test.com"


@app.before_first_request
def initialize():
    Database.initialize()
    session['email'] = session.get('email')
    session['name'] = session.get('name')

    scheduler = BackgroundScheduler()
    scheduler.add_job(check_alert, "cron", day_of_week="0-4", hour="16", minute=30)
    scheduler.start()


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


@app.route("/change_email", methods=['GET', 'POST'])
def change_email():
    if session['email']:
        if request.method == 'POST':
            new_email = request.form['InputNewEmail']
            password = request.form['InputPassword']
            result = User.check_user(session['email'], password)
            if result is True:
                User.update_user_email(session['email'], new_email)
                session['email'] = new_email
                message = "Your new email is {}".format(new_email)
                return render_template("change_email.html", message=message)
            else:
                message = "Input password is incorrect"
                return render_template("change_email.html", message=message)
        else:
            return render_template("change_email.html")
    else:
        return redirect("/login")


@app.route("/logout")
def logout():
    session['email'] = None
    session['name'] = None
    return redirect("/")


@app.route("/new_alert", methods=["GET", "POST"])
def new_alert():
    if session['email']:
        moneydict, position = Money.search_data()
        if request.method == 'POST':
            input_currency = request.form['input_currency']
            rate_exchange = request.form['rate_exchange']
            bank_buy = request.form['bank_buy']
            bank_sale = request.form['bank_sale']
            result = All_alert.create_alert(session['email'], input_currency, rate_exchange, [bank_buy, bank_sale])
            if result is True:
                message = "Your notification setting is created successfully!"
                currency_msg = "幣別: {}".format(input_currency)
                exchange_msg = "匯率: {}".format("現金匯率" if rate_exchange == "cash" else "即期匯率")
                buy_msg = "銀行買入通知價格: ${}".format(bank_buy)
                sale_msg = "銀行賣出通知價格: ${}".format(bank_sale)
                return render_template("new_alert.html", moneydict=moneydict, message=message,
                                       currency_msg=currency_msg, exchange_msg=exchange_msg, buy_msg=buy_msg,
                                       sale_msg=sale_msg)
            else:
                message = "You alread created the notification. (每個幣別只能對應兩種匯率)Please add a new one!"
                currency_msg = "幣別: {}".format(input_currency)
                exchange_msg = "匯率: {}".format("現金匯率" if rate_exchange == "cash" else "即期匯率")
                buy_msg = "銀行買入通知價格: ${}".format(bank_buy)
                sale_msg = "銀行賣出通知價格: ${}".format(bank_sale)
                return render_template("new_alert.html", moneydict=moneydict, message=message,
                                       currency_msg=currency_msg, exchange_msg=exchange_msg, buy_msg=buy_msg,
                                       sale_msg=sale_msg)
        else:
            return render_template("new_alert.html", moneydict=moneydict)
    else:
        return redirect("/login")


@app.route("/cash_alert")
def cash_alert():
    if session['email']:
        cash_data = All_alert.find_user_alert(session['email'], 'cash')
        return render_template("cash_alert.html", cash_data=cash_data)
    else:
        return redirect("/login")


@app.route("/sign_alert")
def sign_alert():
    if session['email']:
        sign_data = All_alert.find_user_alert(session['email'], 'sign')
        return render_template("sign_alert.html", sign_data=sign_data)
    else:
        return redirect("/login")


@app.route("/update_alert", methods=["POST"])
def update_alert():
    if request.method == "POST":
        bank_buy = request.form['bank_buy']
        bank_sale = request.form['bank_sale']
        currency = request.form['currency']
        rate_exchange = request.form['rate_exchange']
        if rate_exchange == "cash":
            All_alert.update_user_alert(session['email'], currency, rate_exchange, [bank_buy, bank_sale])
            return redirect("/cash_alert")
        else:
            All_alert.update_user_alert(session['email'], currency, rate_exchange, [bank_buy, bank_sale])
            return redirect("/sign_alert")


@app.route("/delete_alert", methods=["POST"])
def delete_alert():
    if request.method == "POST":
        currency = request.form['currency']
        rate_exchange = request.form['rate_exchange']
        if rate_exchange == "cash":
            All_alert.delete_user_alert(session['email'], currency, rate_exchange)
            return redirect("/cash_alert")
        else:
            All_alert.delete_user_alert(session['email'], currency, rate_exchange)
            return redirect("/sign_alert")


if __name__ == "__main__":
    app.run(debug=True, port=4101)
