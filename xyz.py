import time
from datetime import datetime

while True:
    if datetime.now().strftime("%H") == "17":
        robot.say(vocabulary)
