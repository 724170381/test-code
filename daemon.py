import requests
import pprint
import os
import crypt
from daemon import runner

def Add():
    url = 'https://database.company.com/devices/<hostname>/allowedUsers'
    get_values = requests.get(url)
    get_values_json = get_values.json()
    allow_users = get_values_json('allowedUsers')
    for user in allow_users:
        password = "admin123" #default password
        encPass = crypt.crypt(password, "22")
        os.system("sudo useradd -p" + encPass + " " + user)
        os.system("sudo usermod -aG wheel " + user)

add = Add()
daemon_runner = runner.DaemonRunner(add)
daemon_runner.do_action()



