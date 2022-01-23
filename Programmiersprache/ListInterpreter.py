# Have access on Interpreter
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


