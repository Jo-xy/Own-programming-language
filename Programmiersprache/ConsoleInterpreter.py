# Make Console methods usable
import Console
# For checking Parameters
from Functions import Functions
# For detection of strings
import MainInterpreter

def checkConsole(task, origTask, items):
    task = task.split('.', 1)[1]

    if task.startswith('out'):
        task = task.split('(', 1)[1]
        task = task.replace(')', '')

        output = MainInterpreter.checkTask(task, origTask, items)[0]
        if output != None:
            value = Console.out(output, origTask, items)[0]
            return [value, origTask, items]
        

    elif task.startswith('read'):
        task = task.split('(', 1)[1]
        task = task.replace(')', '')

        par = parameters = Functions.splitParameters(task, origTask, items)[0]

        if par.get('msg') and not par.get('datatype'):
            if par.get('msg') != '':
                value = Console.read(origTask, items, msg = par.get('msg'))[0]
                return [value, origTask, items]

        elif par.get('datatype') and not par.get('msg'):
            if par.get('datatype') != '':
                value = Console.read(origTask, items, datatype = par.get('datatype'))[0]
                return [value, origTask, items]

        ###########---Problem of more than one parameter------------##########
        # Have to fix it!!!
        elif par.get('msg') and par.get('datatype'):
            value = Console.read(origTask, items, msg = par.get('msg'), datatype = par.get('datatype'))[0]
            return [value, origTask, items]

        else:
            value = Console.read(origTask, items)[0]
            return [value, origTask, items]
