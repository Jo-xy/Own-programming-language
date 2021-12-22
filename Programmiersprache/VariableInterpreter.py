from Empty import Empty

def checkVariable(task, item):
    task = task.split('var ', 1)[1]

    # if variable is just declared and d`´t gets a value
    if not '=' in task:
        varName = task.split(' ')[0]
        item['Variable_'+varName] = Empty()
    else:
        varName = task.spllit

