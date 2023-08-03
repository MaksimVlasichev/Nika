import requests
import random
import time
TOKEN = ""
chat_id = "1139939540"
import keyboardd
time.sleep(3)
# keyboardd.press('space')
message = ""
def code():
    global message
    message = str(random.randint(10,99)) + str(random.randint(10,99))
    print(message)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
    return message