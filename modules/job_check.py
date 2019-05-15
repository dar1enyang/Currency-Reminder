from modules.money import Money
from modules.database import Database
import requests

def check_alert():
    moneydict, position = Money.search_data()
    all_user = []
    data = Database.find_all(collection="users")
    for user in data:
        all_user.append(user["email"])
    for user in all_user:
        print(user)
        message = []
        user_all_alert = Database.find(collection="all_alert", query={"email": user})
        for user_alert in user_all_alert:
            if user_alert["rate_exchange"] == "cash":
                if moneydict[position[user_alert["currency"]]].cash_in != "-":
                    if float(user_alert["price"][0]) >= float(moneydict[position[user_alert["currency"]]].cash_in):
                        if user_alert["currency"] not in message:
                            message.append(user_alert["currency"])
                        else:
                            pass
                    elif moneydict[position[user_alert["currency"]]].cash_out != "-":
                        if float(user_alert["price"][0]) <= float(moneydict[position[user_alert["currency"]]].cash_out):
                            if user_alert["currency"] not in message:
                                message.append(user_alert["currency"])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                elif moneydict[position[user_alert["currency"]]].cash_out != "-":
                    if float(user_alert["price"][0]) <= float(moneydict[position[user_alert["currency"]]].cash_out):
                        if user_alert["currency"] not in message:
                            message.append(user_alert["currency"])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

            if user_alert["rate_exchange"] == "sign":
                if moneydict[position[user_alert["currency"]]].sign_in != "-":
                    if float(user_alert["price"][1]) >= float(moneydict[position[user_alert["currency"]]].sign_in):
                        if user_alert["currency"] not in message:
                            message.append(user_alert["currency"])
                        else:
                            pass
                    elif moneydict[position[user_alert["currency"]]].sign_out != "-":
                        if float(user_alert["price"][1]) <= float(moneydict[position[user_alert["currency"]]].sign_out):
                            if user_alert["currency"] not in message:
                                message.append(user_alert["currency"])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                elif moneydict[position[user_alert["currency"]]].sign_out != "-":
                    if float(user_alert["price"][1]) <= float(moneydict[position[user_alert["currency"]]].sign_out):
                        if user_alert["currency"] not in message:
                            message.append(user_alert["currency"])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        print(user,":",message)
        requests.post(

            "https://api.mailgun.net/v3/sandboxcf0f0204481f4e5db32ca491987d150f.mailgun.org/messages",
            auth=("api", "b7288f39ae1c25d533325c5181e0eada-4a62b8e8-809b3b07"),
            data={"from": "Mailgun Sandbox <postmaster@sandboxcf0f0204481f4e5db32ca491987d150f.mailgun.org>",
                  "to": user,
                  "subject": "外幣通知",
                  "text": "目前符合調的外幣為:{},請盡快至關網查看!".format(str(message).strip("[]"))})


