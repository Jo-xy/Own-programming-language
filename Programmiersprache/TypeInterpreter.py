import MainInterpreter

def checkType(task, origTask, items):
    try:
        task = task.split('type(', 1)[1]
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
        print('Missing argument or open brackets.')
        return [None, origTask, items]

    try:
        task = MainInterpreter.checkTask(task, origTask, items)[0]
        datatype = type(task)

        if datatype == int:
            return ["int", origTask, items]

        elif datatype == float:
            return ["float", origTask, items]

        elif datatype == str:
            return ["str", origTask, items]

        elif datatype == bool:
            return ["bool", origTask, items]

        elif datatype == list:
            return ["list", origTask, items]

        else:
            print("Error in '{}'.".format(origTask))
            print("No valid datatype.".format(task))
            return [None, origTask, items]


    # Next part probably not needed (checkTask will sort out wrong things normally), but leave here for the moment
    except NameError:
        print("Error in '{}'.".format(origTask))
        print("No variable called '{}' or no valid datatype.".format(task))
        return [None, origTask, items]
