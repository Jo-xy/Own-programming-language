def checkImport(task, origTask, items):
    toImport = task.split(' ')[1]
    if toImport == 'Console':
        items['Import_Console'] = True

    elif toImport == 'Variables':
        items['Import_Variables'] = True

    else:
        print("Error in '{}'.".format(origTask))
        print("No module named '{}'".format(toImport))

    return [origTask, items]