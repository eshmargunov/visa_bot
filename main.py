import os
import requests
import logging
from telegram.ext import Updater

logging.basicConfig()

TOKEN = os.environ.get("TOKEN")
URL = "https://www.vfsrussiavisaservices.com/Finland-russia-online/AppScheduling/AppSchedulingGetInfo.aspx?P=PcqAqEGdf4OMbJ1CZgKHSUN3Je9Uumiy6NGhvmhMab7phBf7hKlWsBQNrNze6jyj+86S93yLA0yGdiqvwB5yZg%3d%3d"
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded"
}

users = set()


def get_body():
    body = "__EVENTTARGET=ctl00%24plhMain%24cboVisaCategory" \
           "&__EVENTARGUMENT=" \
           "&__LASTFOCUS=" \
           "&__VIEWSTATE=sGmnphYK%2B8XZNYIrMxTJfnh7eqNFdIgBcbrewSPqPyXItfLJklQ%2FPS7HsKQo0XKnQU945SAZhJzUWtBZMsTnqYo1PIujLliQ3nQ6al93NxkzhWW921fQ%2F%2FdAjnLBCmGl0CJNRJJYomcFcefxsKhc7E%2FIG9z7J3OlK4P9AyAuNn9rn44GjAP8g6qndiP%2BhmoNzMK2fKLgHC5liWjNE%2BlOaGc%2FbtWT95q3QL1wN3X18eds0%2BxL4%2F1Dl4PoxM5PI3xKdwj3AWQ2TWFzWe5X2pcf3zJz0aKyZgvjujlEm6vxHoTwAYvUFgiUjotkqTLI5OoOZRQfCQOKIImGF7BS%2BF8AXh%2Fx947KfAKNknD59tj97SgmTZxl8HyUg7K81P2vfALvptbYSwTUipjtmptcWAOQSF1eBIugLO4YHstMrggdCO%2Bh4m6%2F2eXNHnciQCQdrqY2ZNSdso7QlbiJcWWzZ5xbNsUg%2B11QF6jqRVB82PpattGmL3uFlJcRX0TmaIISw596ViEQyPDB97OpK22mx2nlu%2F8Yft282b0txCiOfWbnQIxllAi11hhEfpBJ7qEkPI%2F8rZINjQdnGSOPtXPdje%2B2qFzqPOFr%2FtScCb5TP7FrovfWdvkhAIgdxlqjiKJDEE30z8vt11%2B7WbMAZQuQZ9GOcN5ugk124zIM%2FEU1EWz6w464HTeLchyEZ1KTLxSSPc4Cbu1mzONk23DRbXbZwIUh%2BDX73RS3XMSD%2F99SN6lXLsbXPXZCwWueA341SVLhGlD%2FJ05xG42CgZyQqoO6P2cB5W7sWu%2B8TvCd%2FOYDOPbfJLgZ0Zi6MV8l9WXZpz4WCqmteuVeaXc59X6BPiAZfFJlD3yOaCd8MILYR%2BJ7Bw4ORFpa1%2B2vrtDAS3vw5eUTE5ugKOoj1C8iN3YlCmLRULly42cpYEwyueoDMoXbvq0rf%2FWOXjalY%2Bfa%2FtGpxQIlF0CewhsLukglU0fS2KWtB%2FCfjomRTUEiiyLF%2FariUgsp6rX%2BdGAtSTvn%2BhHDXCBQ6AjM1LOelQeuBqbHj0kQHxPhJ%2BJBdIdjs4YxoiUkS64X0Fff0tCM%2Fm6k8RdWtLkzcoIDWnzS%2BwORg9PKBCA8YpM5jz8hV9A3vyEiR5aGN35hwLm74aOdKHeI4s8s%2BaiO2EhfKX7s1Yo6qIOP%2FGfWtkrppuYp6YV9dUuKuYOtvxNB%2BQDKSaSMRIQKcSZAKv6Y4POD%2Fy1voiWbiMTVkNFzRzEUWoDYnY3PjxGRREWzpWmPLldj6%2FyfPZ%2FOyyhQ05OMEPcT%2Bgmk6iXH6WIBjQvIUXqTR5XHN5yTNazmOaon8XPdTSoKER7gf5YPI6gdRD3KopzqH2BNP83SG%2BgCDFKg5yghQaq0AGpJBLi1aOfHeWgIy6Mwl6cFiNyDylz%2F9BcoTdKX6cWviI3sNk8ISLRhEIp887moi5Fcr096ARCD8ChOmm7dNKq1jD%2FP9ZGTBbcE3R3XN6%2B6xWHk6V32KOZJMStoZxheSZv1VdHnh3JUnbe8RXQfiMYoVBhNyq5hftc9Woxm80I88lMvnuxOn%2BQ4IOcjGgIsEA4me0eG0elow3VzV5XBNl234fslp3mLSYce89sKNh0w2QYYkJIoTmgNEZwu5M0o3ZO4d7TjNL0LBImaperDjD7fn%2FQUiIQq0x8SLtBC%2B0%2BlUT7pON%2Fabg7TJ4KzzAuu6Bnp2VDxkDVs8ms3BPdXEchfFfu2T49ox4Ln9tbUfNRcs%2F6e8xiVOfunFoUsR5PeOnpi08iy7t3vmXEj%2F%2FhQsqDhZy0EsBe%2BPhmbMSVZh0aMCqZm4pZe995Msyc5XfH3QS8NWriWIPQmk1kjvPxccatqBXCuU66JyrJKtMPfCAphdrExX1KKXo32DTCVfapVf4%2BxWKIkm7w6mpTH7DhPS4L3%2B3IiIuGbaLkQwYhtjzM1U4wZAkAxu%2BrxdKIaapHLTCOt56GVzozUOu%2FEzKWCDPvIGD0WS%2Fel%2FkQJcliflVaVuyz0V1JP46Qo3bC%2FG6TWVHszoXklhFZpw2qIMYZm51VJiO4Wq0PSlFTz10MSS0dlISS6P1crhfyW1u7v%2FeFyfL1B1XcDe%2FkEle2e%2FFX6nN3t5wE2giwN5NG%2FzkTPWF7E3XvlQy%2BOpphmrQpDO1Sp0IbFUKU16duAtU03fueUPzf3nX0pGfCE9wrbvF%2BlasSQY58N%2BPvQkoDlxQfIyrdBJdOXLFpMJC8AcpAPSoabK8IdwV8t1gQF0FyZ%2FV%2BGiuuZ%2BXru81ygppjWvZPeY30gU%2FTnZs0sH%2Foc5A2Ke%2BMt%2FwCESP13tIVBJi8%3D&____Ticket=4&__EVENTVALIDATION=qVWF3lKQVFXKgN77FrmSt5zF%2FmWcHMNmL%2BMCmQo4anb0nreItr6u89dMvOKAdcSrnfeGirScVAZsRpnN6xUTWgT4XKQCBEAkc58QL2vG9gsvhdgFCw705UqAetWOoEq1fI2Q6zxkKq%2F1teZBH3y8yqr42zy8dGlYPS%2BEagYurUhRSlWPfda3iGH4wpxcvfR6pIvxVqgGKEBZWwbhN8xsoggffZIlP6VBb8my8eqbpKxC%2BCo8XG27dDuldSI%3D" \
           "&ctl00%24plhMain%24tbxNumOfApplicants=2&ctl00%24plhMain%24cboVisaCategory=11" \
           "&ctl00%24plhMain%24MyCaptchaControl1="
    return body


def get_status_from_visa():
    body = get_body()
    request = requests.post(url=URL, data=body, headers=HEADERS)
    return request.status_code


def is_reserve_open():
    status = get_status_from_visa()
    return status != 200


def status(bot, update):
    request = requests.post(url=URL, data=get_body(), headers=HEADERS)
    bot.sendMessage(update.message.chat_id, text=request.status_code)


def unknown_command(bot, update):
    bot.sendMessage(update.message.chat_id, text="Unknown command")


def subscribe(bot, update):
    users.add(update.message.chat_id)
    bot.sendMessage(update.message.chat_id, text="Subscribed!")


def unsubscribe(bot, update):
    chat_id = update.message.chat_id
    if chat_id in users:
        users.remove(chat_id)
        bot.sendMessage(chat_id, text="Unsubscribed!")
    else:
        bot.sendMessage(chat_id, text="You are not subscribed!")


# Get status from server every n second. It's a job queue.
def job_open_reserve(bot):
    if is_reserve_open():
        # Make copy of users set to avoid "Set changed size during iteration" error
        subscribed_users = users.copy()
        for user in subscribed_users:
            bot.sendMessage(user, text="OPEN!")
            # TODO: Need refactor!
            users.remove(user)
            bot.sendMessage(user, text="You unsubscribed!")

        del subscribed_users


def main():
    updater = Updater(TOKEN)
    job_queue = updater.job_queue

    job_queue.put(job_open_reserve, 30)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for Telegram messages
    dp.addTelegramCommandHandler("status", status)
    dp.addTelegramCommandHandler("subscribe", subscribe)
    dp.addTelegramCommandHandler("unsubscribe", unsubscribe)
    dp.addUnknownTelegramCommandHandler(unknown_command)

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
