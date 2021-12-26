# Make Console methods usable
import Console
# For checking Parameters
from Functions import Functions
# For detection of strings
import MainInterpreter

def checkConsole(task, items):
    task = task.split('.', 1)[1]

    if task.startswith('out'):
        task = task.split('(', 1)[1]
        task = task.replace(')', '')

        output = MainInterpreter.checkTask(task, items)[0]
        if output != None:
            return Console.out(output)
        

    elif task.startswith('read'):
        task = task.split('(', 1)[1]
        task = task.replace(')', '')

        par = parameters = Functions.splitParameters(task, items)[0]

        if par.get('msg') and not par.get('datatype'):
            if par.get('msg') != '':
                return Console.read(msg = par.get('msg')+' ')

        elif par.get('datatype') and not par.get('msg'):
            if par.get('datatype') != '':
                return Console.read(datatype = par.get('datatype'))

        ###########---Problem of more than one parameter------------##########
        # Have to fix it!!!
        elif par.get('msg') and par.get('datatype'):
            return Console.read(msg = par.get('msg') + ' ', datatype = par.get('datatype'))

        else:
            return Console.read()
