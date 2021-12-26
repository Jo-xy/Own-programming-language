def checkImport(task, items):
    toImport = task.split(' ')[1]
    if toImport == 'Console':
        items['Import_Console'] = True

    elif toImport == 'Variables':
        items['Import_Variables'] = True

    else:
        print("No module named '" + toImport + "'")

    return [items]