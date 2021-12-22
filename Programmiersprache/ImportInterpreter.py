def checkImport(task, items):
    toImport = task.split(' ')
    if toImport[1] == 'Console':
        items['Import_Console'] = True

    if toImport[1] == 'Variables':
        items['Import_Variables'] = True

    return items