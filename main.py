# ini biar bisa ngetes aja :v

from login import login
from register import register
from help import help

role = ""
user_input = input(">>> ")
while (user_input != "exit"):
    if (user_input == "login"):
        role = login() # nyimpen role user
    elif (user_input == "register"):
        register(role)
    elif (user_input == "help"):
        help(role)
    user_input = input(">>> ")
