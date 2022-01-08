# Obj to mark empty variables
from Empty import Empty
# Have access to MainInterpreter
import MainInterpreter

def checkVariable(task, origTask, items):
    try:
        task = task.split('var ', 1)[1]
    except IndexError:
        return [None, origTask, items]

    # if variable is just declared and don´t gets any value
    if not '=' in task:
        varName = task.split(' ')[0]
        items['Variable_'+varName] = Empty()
    # giving the var a value
    else:
        # find out value
        varName = task.split('=')[0]
        varName = varName.replace(' ', '')
        task = task.split('=', 1)[1]

        # remove unneeded 'space'
        if task[0] == ' ':
            task = task[1:]
        if task[-1] == ' ':
            task = task[:-1]

        # Giving variable its value
        items['Variable_'+varName] = MainInterpreter.checkTask(task, origTask, items)[0]

    return [items.get('Variable_'+varName), 'Variable_'+varName, origTask, items]
