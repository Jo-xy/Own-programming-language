from Functions import Functions

def length(element, origTask, items):
    try:
        element = element.split('len(')[1]
        newTask = ''
        otherBrackets = 0
        for i in element:
            if i == '(':
                otherBrackets += 1
            if i == ')':
                otherBrackets -= 1
            if otherBrackets == -1:
                break
            newTask += i
        element = newTask

        parameterList = Functions.splitElements(element, origTask, items)[0]

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
        try:
            length = len(parameterList[0])
            return [length, origTask, items]
        except TypeError:
            print("Error in '{}'.".format(origTask))
            print("Element has no length.")
            return [None, origTask, items]

