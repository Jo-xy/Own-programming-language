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