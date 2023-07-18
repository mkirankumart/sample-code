import math
import os
import sys

import requests

# print(sys.version)
print(sys.executable)


def greet(whotogreet):
    greeting = "hello,{}".format(whotogreet)
    return greeting


r = requests.get("https://youtube.com")
print(r.status_code)

na  me = input("your name?")
print("hello,", name)
