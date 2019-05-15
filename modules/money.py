import pandas


class Money(object):
    def __init__(self, currency, currency_cht, cash_in, cash_out, sign_in, sign_out):
        self.currency = currency
        self.currency_cht = currency_cht
        self.cash_in = cash_in
        self.cash_out = cash_out
        self.sign_in = sign_in
        self.sign_out = sign_out

    @staticmethod
    def search_data():
        data = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")[0]
        currency_table = data.iloc[:, 0:5]
        currency_table.columns = ["幣別", "現金匯率-買入", "現金匯率-賣出", "即期匯率-買入", "即期匯率-賣出"]
        currency_cht = currency_table["幣別"].str.extract("(\w+)", expand=True)
        currency_table["幣別"] = currency_table["幣別"].str.extract("\((\w+)\)", expand=True)
        moneydict = {}
        position = {}

        for i in range(0, 19):
            dollar = currency_table.values[i]
            moneydict[i] = Money(dollar[0], currency_cht.values[i][0], dollar[1], dollar[2], dollar[3], dollar[4])
            position[currency_cht.values[i][0]] = i

        return moneydict, position



# moneydict, position = Money.search_data()
# for i in range(0, 19):
#     print(moneydict[i].currency)
#     print(moneydict[i].currency_cht)
#     print(moneydict[i].cash_in)
#     print(moneydict[i].cash_out)
#     print(moneydict[i].sign_in)
#     print(moneydict[i].sign_out)
#     print("------")