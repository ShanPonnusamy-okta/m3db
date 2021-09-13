import requests
import time

while 1 < 2:
    r = requests.get('http://localhost:8080/greeting')
    time.sleep(5)
