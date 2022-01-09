def checkImport(task, origTask, items):
    toImport = task.split(' ')[1]
    if toImport == 'Console':
        items['Import_Console'] = True

    elif toImport == 'Variables':
        items['Import_Variables'] = True

    elif toImport == 'Calculations':
        items['Import_Calculations'] = True

    elif toImport == 'If':
        items['Import_If'] = True

    elif toImport == 'time':
        items['Import_time'] = True

    else:
        print("Error in '{}'.".format(origTask))
        print("No module named '{}'".format(toImport))

    return [origTask, items]