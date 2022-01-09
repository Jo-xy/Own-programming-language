import MainInterpreter

def checkBool(task, origTask, items):
    # Safety-remove spaces again
    task = task.replace(' ', '')

    # For the case that True AND False were given
    if 'True' in task and 'False' in task:
        print("Error in '{}'.".format(origTask))
        print('Not sure if to convert in bool as True or False.')
        return [None, origTask, items]

    # Return True
    if 'True' in task:
        return [True, origTask, items]
    # Return False
    elif 'False' in task:
        return [False, origTask, items]
    
    # When no Bool can be found
    else:
        print("Error in '{}'.".format(origTask))
        print('Can not find bool value.')
        return [None, origTask, items]


def checkExpression(boolExpression, origTask, items):
    task = boolExpression
    compareMode = None

    if '==' in task:
        task = task.replace(' ', '')
        task = task.split('==')
        compareMode = ['equals']
    elif '<' in task:
        task = task.replace(' ', '')
        task = task.split('<')
        compareMode = ['num', '<']
    elif '>' in task:
        task = task.replace(' ', '')
        task = task.split('>')
        compareMode = ['num', '>']
    elif 'in' in task:
        task = task.replace(' ', '')
        task = task.split('in')
        compareMode = ['str']
    else:
        task = task.replace(' ', '')
    
    # When two values are compared
    if compareMode != None:
        task[0] = MainInterpreter.checkTask(task[0], origTask, items)[0]
        task[1] = MainInterpreter.checkTask(task[1], origTask, items)[0]

        try:
            if compareMode[0] == 'equals':
                if task[0] == task[1]:
                    result = True
                else:
                    result = False

            elif compareMode[0] == 'num':
                if compareMode[1] == '<':
                    result = (task[0] < task[1])
                elif compareMode[1] == '>':
                    result = (task[0] > task[1])

            elif compareMode[0] == 'str':
                if task[0] in task[1]:
                    result = True
                else:
                    result = False

            if result == True or result == False:
                return [result, origTask, items]
            else:
                print("Error in '{}'.".format(origTask))
                print('Can not find bool.')
                return [None, origTask, items]
        
        except ValueError:
            print("Error in '{}'.".format(origTask))
            print('Can not find bool.')
            return [None, origTask, items]

    # When it is only one value
    else:
        # find out this value
        task = MainInterpreter.checkTask(task, origTask, items)[0]

        # Check if it is a bool and return
        if task == True or task == False:
            return [task, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print('Can not find bool.')
            return [None, origTask, items]