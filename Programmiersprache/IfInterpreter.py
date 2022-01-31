import BoolInterpreter

def checkIfBlock(expression, origTask, items):
    try:
        expression = expression.split('if ')[1]

        # Find out if the statement is true or False
        boolExpression = expression.split('(', 1)[1]

        newTask = ''
        otherBrackets = 0
        for i in boolExpression:
            if i == '(':
                otherBrackets += 1
            if i == ')':
                otherBrackets -= 1
            if otherBrackets == -1:
                break
            newTask += i
        boolExpression = newTask

        isTrue, origTask, items = BoolInterpreter.checkExpression(boolExpression, origTask, items)

        # codeBlock name/identifier, to mark ending: 'end name'
        name = expression.split(')')[1]
        name = name.replace(' ', '')

        if isTrue == True:
            return [True, origTask, items]
        else:
            items['IfBlocks'].append(name)
            return [False, origTask, items]


    except IndexError:
        print("Error in '{}'.".format(origTask))
        print('Missing arguments.')