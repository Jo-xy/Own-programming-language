# get access to Interpreter
import MainInterpreter
from Functions import Functions

def setIndex(task, origTask, items):
    try:
        task = task.split('setIndex(')[1]
        newTask = ''
        otherBrackets = 0
        for i in task:
            if i == '(':
                otherBrackets += 1
            if i == ')':
                otherBrackets -= 1
            if otherBrackets == -1:
                break
            newTask += i
        task = newTask
    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing arguments or open brackets.")
        return [None, origTask, items]

    varName = task.split(',')[0]
    parameterList = Functions.splitElements(task, origTask, items)[0]
    try:
        items['Variable_'+varName][parameterList[1]] = parameterList[2]
        return [parameterList[2], origTask, items]
    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Not able to use indeces for this object or index out of range.")
        return [None, origTask, items]
    except TypeError:
        print("Error in '{}'.".format(origTask))
        print("Indeces must be int.")
        return [None, origTask, items]

def getIndex(task, origTask, items):
    try:
        task = task.split('getIndex(')[1]
        newTask = ''
        otherBrackets = 0
        for i in task:
            if i == '(':
                otherBrackets += 1
            if i == ')':
                otherBrackets -= 1
            if otherBrackets == -1:
                break
            newTask += i
        task = newTask
    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing arguments or open brackets.")
        return [None, origTask, items]
    
    varName = task.split(',')[0]
    parameterList = Functions.splitElements(task, origTask, items)[0]

    try:
        value = items.get('Variable_'+str(varName))[int(parameterList[1])]
        return [value, origTask, items]

    except TypeError:
        print("Error in '{}'.".format(origTask))
        print("Indeces must be int.")
        return [None, origTask, items]

    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Not able to use indeces for this object or index out of range.")
        return [None, origTask, items]