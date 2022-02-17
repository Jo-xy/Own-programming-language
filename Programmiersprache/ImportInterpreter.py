def checkImport(task, origTask, items):
    toImport = task.split(' ')[1]
 
    if toImport == 'time':
        items['Import_time'] = True

    else:
        print("Error in '{}'.".format(origTask))
        print("No module named '{}'".format(toImport))

    return [origTask, items]