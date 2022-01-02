import time as t
import datetime as dt

def time(task, origTask, items):
    try:
        task = task.split('"')[1]
    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing positional argument in 'time()'.")
        return ["Error", origTask, items]
    timeString = task

    time = t.ctime()
    hours = time.split(' ')[4].split(':')[0]
    minutes = time.split(' ')[4].split(':')[1]
    sec = time.split(' ')[4].split(':')[1]

    timeString = timeString.replace('%H', hours)
    timeString = timeString.replace('%M', minutes)
    timeString = timeString.replace('%S', sec)

    return [timeString, origTask, items]


def date(task, origTask, items):
    try:
        task = task.split('"')[1]
    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing positional argument in 'date()'.")
        return ["Error", origTask, items]

    timeString = task

    time = str(dt.date.today())
    year = time.split('-')[0]
    month = time.split('-')[1]
    day = time.split('-')[2]

    timeString = timeString.replace('%Y', year)
    timeString = timeString.replace('%M', month)
    timeString = timeString.replace('%D', day)

    return [timeString, origTask, items]


def calendar(task, origTask, items):
    if '"' in task:
        print("Error in '{}'.".format(origTask))
        print("Invalid positional argument in 'calendar()'.")
        return ["Error", origTask, items]

    timeString = t.ctime()

    timeString = timeString.split(' ')
    timeString.remove('')
    timeString.pop(3)
    timeString = ' '.join(timeString)

    return [timeString, origTask, items]


def checkTime(task, origTask, items):
    task = task.split('.', 1)[1]
    if task.startswith('time'):
        timeString = time(task, origTask, items)[0]
    elif task.startswith('date'):
        timeString = date(task, origTask, items)[0]
    elif task.startswith('calendar'):
        timeString = calendar(task, origTask, items)[0]
    else:
        print("Error in '{}'.".format(origTask))
        print("No function called '{}'.".format(task.split('(')[0]))
        return ["Error", origTask, items]
    
    return [timeString, origTask, items]