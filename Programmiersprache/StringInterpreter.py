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
