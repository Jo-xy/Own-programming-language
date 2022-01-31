# Have access on Interpreter
from typing_extensions import ParamSpec
import MainInterpreter
from Functions import Functions

def checkList(elements, origTask, items):
    elements = elements.split('[')[1]
    newElements = ''
    otherBrackets = 0
    for i in elements:
        if i == '[':
            otherBrackets += 1
        if i == ']':
            otherBrackets -= 1

        if otherBrackets == -1:
            break
        
        newElements += i

    elements = newElements

    # When a constructor is used
    if elements.startswith(':'):
        if elements.count(':') == 1:
            try:
                elements = elements.split(':')[1]
            except IndexError:
                print("Error in '{}'.".format(origTask))
                print("Missing argument.")
                return [None, origTask, items]

            if elements.isdigit():
                constructedList = []
                for i in range(int(elements)):
                    constructedList.append(None)
                return [constructedList, origTask, items]
            else:
                print("Error in '{}'.".format(origTask))
                print("Invalid parameter '{}'. Must be int.".format(elements))
                return [None, origTask, items]


        else:
            try:
                value = elements.split(':')[2]
                elements = elements.split(':')[1]
            except IndexError:
                print("Error in '{}'.".format(origTask))
                print("Missing argument.")
                return [None, origTask, items]
            value = MainInterpreter.checkTask(value, origTask, items)[0]
            if elements.isdigit():
                constructedList = []
                for i in range(int(elements)):
                    constructedList.append(value)
                return [constructedList, origTask, items]
            else:
                print("Error in '{}'.".format(origTask))
                print("Invalid parameter '{}'. Must be int.".format(elements))
                return [None, origTask, items]

    # If there is no constructor
    else:
        elementList = Functions.splitElements(elements, origTask, items)[0]

    return [elementList, origTask, items]



def addIndex(task, origTask, items):
    try:
        task = task.split('addIndex(')[1]
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

        parameterList = Functions.splitElements(task, origTask, items)[0]

    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing argument or open brackets.")
        return [None, origTask, items]

    if len(parameterList) > 3:
        print("Error in '{}'.".format(origTask))
        print("Invalid arguments.")
        return [None, origTask, items]

    elif len(parameterList) < 3:
        print("Error in '{}'.".format(origTask))
        print("Missing arguments.")
        return [None, origTask, items]
      
    else:
        element = parameterList[0]
        index = parameterList[1]
        newValue = parameterList[2]
        if type(element) == list and type(index) == int:
            element.insert(index, newValue)
            return [element, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("First two arguments must be datatype 'list' and 'int'.")
            return [None, origTask, items]


def deleteIndex(task, origTask, items):
    try:
        task = task.split('deleteIndex(')[1]
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

        parameterList = Functions.splitElements(task, origTask, items)[0]

    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing argument or open brackets.")
        return [None, origTask, items]

    if len(parameterList) > 2:
        print("Error in '{}'.".format(origTask))
        print("Invalid arguments.")
        return [None, origTask, items]

    elif len(parameterList) < 2:
        print("Error in '{}'.".format(origTask))
        print("Missing arguments.")
        return [None, origTask, items]
      
    else:
        element = parameterList[0]
        index = parameterList[1]
        if type(element) == list and type(index) == int:
            element.pop(index)
            return [element, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Arguments must be datatype 'list' and 'int'.")
            return [None, origTask, items]


def appendIndex(task, origTask, items):
    try:
        task = task.split('append(')[1]
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

        parameterList = Functions.splitElements(task, origTask, items)[0]

    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing argument or open brackets.")
        return [None, origTask, items]

    if len(parameterList) > 2:
        print("Error in '{}'.".format(origTask))
        print("Invalid arguments.")
        return [None, origTask, items]

    elif len(parameterList) < 2:
        print("Error in '{}'.".format(origTask))
        print("Missing arguments.")
        return [None, origTask, items]
      
    else:
        element = parameterList[0]
        newValue = parameterList[1]
        if type(element) == list:
            element.append(newValue)
            return [element, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("First Argument must be datatype 'list'.")
            return [None, origTask, items]


def extendList(task, origTask, items):
    try:
        task = task.split('extend(')[1]
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

        parameterList = Functions.splitElements(task, origTask, items)[0]

    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing argument or open brackets.")
        return [None, origTask, items]

    if len(parameterList) > 2:
        print("Error in '{}'.".format(origTask))
        print("Invalid arguments.")
        return [None, origTask, items]

    elif len(parameterList) < 2:
        print("Error in '{}'.".format(origTask))
        print("Missing arguments.")
        return [None, origTask, items]
      
    else:
        element = parameterList[0]
        listToAdd = parameterList[1]
        if type(element) == list and type(listToAdd) == list:
            element.extend(listToAdd)
            return [element, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Arguments must be datatype 'list'.")
            return [None, origTask, items]


def searchValue(task, origTask, items):
    try:
        task = task.split('searchValue(')[1]
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

        parameterList = Functions.splitElements(task, origTask, items)[0]

    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing argument or open brackets.")
        return [None, origTask, items]

    if len(parameterList) > 2:
        print("Error in '{}'.".format(origTask))
        print("Invalid arguments.")
        return [None, origTask, items]

    elif len(parameterList) < 2:
        print("Error in '{}'.".format(origTask))
        print("Missing arguments.")
        return [None, origTask, items]
      
    else:
        element = parameterList[0]
        searchFor = parameterList[1]
        if type(element) == list:
            indexcounter = 0
            foundValuesAt = []
            for i in element:
                if i == searchFor:
                    foundValuesAt.append(indexcounter)
                indexcounter += 1
            return [foundValuesAt, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("First argument must be datatype 'list'.")
            return [None, origTask, items]