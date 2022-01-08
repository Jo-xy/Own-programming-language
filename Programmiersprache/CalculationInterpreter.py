def calculate(task, origTask, items):
    ###########--Detection--#########

    # convert all ':' to '/' for system
    task = task.replace(':', '/')
    # remove unneeded spaces
    task = task.replace(' ', '')
    splittableTask = ''

    # list of all allowed operators for checking and splitting
    operators = ['+', '-', '*', '/']
    # list of all found operators
    foundOperators = {}
    opCounter = 0
    # list of all found numbers
    numbers = []

    checking = True

    for i in task:
        add = i
        if i in operators:
            foundOperators[opCounter] = i
            add = '+'
            opCounter += 1
        if i == ',':
            add = '.'
        if add != ' ' and (add.isdigit() or add == '.' or add in operators):
            splittableTask += add

    numbers = splittableTask.split('+')


    ######--Calculation--#########

    # make str values to numbers
    newNumbers = []

    for i in numbers:
        if '.' in i:
            add = float(i)
        else:
            add = int(i)

        newNumbers.append(add)

        
    numbers = newNumbers


    # calc * and / first
    mode = '*/'
    operators = foundOperators
    workingOperator = 0
    while mode == '*/':
        try:
            if operators.get(workingOperator) == '*':
                result = numbers[workingOperator] * numbers[workingOperator + 1]
                numbers[workingOperator] = "empty"
                numbers[workingOperator + 1] = result
                del operators[workingOperator]
            elif operators.get(workingOperator) == '/':
                result = numbers[workingOperator] / numbers[workingOperator + 1]
                numbers[workingOperator] = "empty"
                numbers[workingOperator + 1] = result
                del operators[workingOperator]
            else:
                safetyTest = numbers[workingOperator]

            workingOperator += 1

        except IndexError:
            while True:
                try:
                    numbers.remove("empty")
                except ValueError:
                    break
            mode = '+-'
            workingOperator = 0


    #record op-positions new
    recNum = 0
    newOperators = {}

    for i in operators:
        newOperators[recNum] = operators.get(i)
        recNum += 1

    operators = newOperators


    # at the end calc + and -
    while mode == '+-':
        try:
            if operators.get(workingOperator) == '+':
                result = numbers[workingOperator] + numbers[workingOperator + 1]
                numbers[workingOperator] = "empty"
                numbers[workingOperator + 1] = result
                # del operators[workingOperator]
                # numbers.insert(workingOperator, result)
            elif operators.get(workingOperator) == '-':
                result = numbers[workingOperator] - numbers[workingOperator + 1]
                numbers[workingOperator] = "empty"
                numbers[workingOperator + 1] = result
                # numbers.insert(workingOperator, result)
            else:
                safetyTest = numbers[workingOperator]

            workingOperator += 1

        except IndexError:
            mode = 'finished'




    #####-Finished-######
    return [result, origTask, items]
