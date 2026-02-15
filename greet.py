from datetime import datetime

def greet():
    am_pm = datetime.now().strftime("%p")
    print(am_pm)
    time= datetime.now().strftime("%I %M %p")

    if am_pm == "PM":
        return "Good evening sir"
    else:
        return "Good morning sir"