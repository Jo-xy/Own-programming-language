from Functions import Functions
import MainInterpreter

def checkString(task, origTask, items):
    # If there is no second ´"´ to end string
    if task.count('"') == 1:
        print("Error in '{}'.".format(origTask))
        print("String ending not marked.")
        return [None, origTask, items]
        
    # If there are multiple strings
    elif task.count('"') > 2:
        print("Error in '{}'.".format(origTask))
        print("Multiple Strings not accepted.")
        return [None, origTask, items]

    # And as usual...
    else:
        # seperate string-text
        string = task.split('"')[1]
        return [string, origTask, items]



def splitString(task, origTask, items):
    try:
        task = task.split('split(')[1]
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

        if type(parameterList[1]) == int:
            counter = 0
            splittedString = []
            currentString = ""
            for i in parameterList[0]:
                currentString += i
                counter += 1
                if counter == parameterList[1]:
                    splittedString.append(currentString)
                    currentString = ""
                    counter = 0
                    print("Now")
            if currentString != "":
                splittedString.append(currentString)

            return [splittedString, origTask, items]


        elif type(parameterList[1]) == str:
            splittedString = parameterList[0].split(parameterList[1])
            return [splittedString, origTask, items]

    except IndexError:
        print("Error in '{}'.".format(origTask))
        print("Missing arguments or open brackets.")
        return [None, origTask, items]


def combineListElementsToString(task, origTask, items):
    try:
        task = task.split('combine(')[1]
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

    if len(parameterList) > 1:
        print("Error in '{}'.".format(origTask))
        print("Invalid arguments.")
        return [None, origTask, items]

    elif len(parameterList) == 0:
        print("Error in '{}'.".format(origTask))
        print("Missing argument.")
        return [None, origTask, items]

    else:
        combinedString = ""
        for i in parameterList[0]:
            combinedString += str(i)

        return [combinedString, origTask, items]


def toUpper(task, origTask, items):
     try:
        task = task.split('toUpper(')[1]
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

     if len(parameterList) > 1:
         print("Error in '{}'.".format(origTask))
         print("Invalid arguments.")
         return [None, origTask, items]

     elif len(parameterList) == 0:
         print("Error in '{}'.".format(origTask))
         print("Missing argument.")
         return [None, origTask, items]

     else:
         element = MainInterpreter.checkTask(task, origTask, items)[0]
         if type(element) == str:
             uppercaseString = element.upper()
             return [uppercaseString, origTask, items]
         else:
             print("Error in '{}'.".format(origTask))
             print("Argument must be datatype 'str'.")
             return [None, origTask, items]


def toLower(task, origTask, items):
     try:
        task = task.split('toLower(')[1]
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

     if len(parameterList) > 1:
         print("Error in '{}'.".format(origTask))
         print("Invalid arguments.")
         return [None, origTask, items]

     elif len(parameterList) == 0:
         print("Error in '{}'.".format(origTask))
         print("Missing argument.")
         return [None, origTask, items]
      
     else:
         element = MainInterpreter.checkTask(task, origTask, items)[0]
         if type(element) == str:
             lowercaseString = element.lower()
             return [lowercaseString, origTask, items]
         else:
             print("Error in '{}'.".format(origTask))
             print("Argument must be datatype 'str'.")
             return [None, origTask, items]


def invertcase(task, origTask, items):
     try:
        task = task.split('invertcase(')[1]
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

     if len(parameterList) > 1:
         print("Error in '{}'.".format(origTask))
         print("Invalid arguments.")
         return [None, origTask, items]

     elif len(parameterList) == 0:
         print("Error in '{}'.".format(origTask))
         print("Missing argument.")
         return [None, origTask, items]
      
     else:
         element = MainInterpreter.checkTask(task, origTask, items)[0]
         if type(element) == str:
             invertedString = element.swapcase()
             return [invertedString, origTask, items]
         else:
             print("Error in '{}'.".format(origTask))
             print("Argument must be datatype 'str'.")
             return [None, origTask, items]


def capitalize(task, origTask, items):
     try:
        task = task.split('capitalize(')[1]
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

     if len(parameterList) > 1:
         print("Error in '{}'.".format(origTask))
         print("Invalid arguments.")
         return [None, origTask, items]

     elif len(parameterList) == 0:
         print("Error in '{}'.".format(origTask))
         print("Missing argument.")
         return [None, origTask, items]
      
     else:
         element = MainInterpreter.checkTask(task, origTask, items)[0]
         if type(element) == str:
             capitalizedString = element.capitalize()
             return [capitalizedString, origTask, items]
         else:
             print("Error in '{}'.".format(origTask))
             print("Argument must be datatype 'str'.")
             return [None, origTask, items]


def isFirst(task, origTask, items):
     try:
        task = task.split('isFirst(')[1]
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
         print("Missing argument(s).")
         return [None, origTask, items]
      
     else:
         element = parameterList[0]
         checkfor = parameterList[1]
         if type(element) == str and type(checkfor) == str:
             isFirst = element.startswith(checkfor)
             return [isFirst, origTask, items]
         else:
             print("Error in '{}'.".format(origTask))
             print("Arguments must be datatype 'str'.")
             return [None, origTask, items]


def isLast(task, origTask, items):
     try:
        task = task.split('isLast(')[1]
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
         print("Missing argument(s).")
         return [None, origTask, items]
      
     else:
         element = parameterList[0]
         checkfor = parameterList[1]
         if type(element) == str and type(checkfor) == str:
             isLast = element.endswith(checkfor)
             return [isLast, origTask, items]
         else:
             print("Error in '{}'.".format(origTask))
             print("Arguments must be datatype 'str'.")
             return [None, origTask, items]


def remove(task, origTask, items):
     try:
        task = task.split('remove(')[1]
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
         print("Missing argument(s).")
         return [None, origTask, items]
      
     else:
         element = parameterList[0]
         toRemove = parameterList[1]
         if type(element) == str and type(toRemove) == str:
             shortedString = element.replace(toRemove, '')
             return [shortedString, origTask, items]
         elif type(element) == list:
             while toRemove in element:
                element.remove(toRemove)
             return [element, origTask, items]
         else:
             print("Error in '{}'.".format(origTask))
             print("Arguments must be datatype 'str' (or the first one 'list).")
             return [None, origTask, items]


def replace(task, origTask, items):
     try:
        task = task.split('replace(')[1]
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
         oldValue = parameterList[1]
         newValue = parameterList[2]

         if type(element) == str and type(oldValue) == str and type(newValue) == str:
             modifiedString = element.replace(oldValue, newValue)
             return [modifiedString, origTask, items]
         elif type(element) == list:
             newlist = []
             for i in element:
                 if i == oldValue:
                     newlist.append(newValue)
                 else:
                     newlist.append(i)
             return [newlist, origTask, items]

         else:
             print("Error in '{}'.".format(origTask))
             print("Arguments must be datatype 'str' (or the first one 'list).")
             return [None, origTask, items]