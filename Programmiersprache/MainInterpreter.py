import ImportInterpreter
import ConsoleInterpreter
import VariableInterpreter

def checkTask(task, items):
    # If it´s an import
    if task.startswith('import'):
        items = ImportInterpreter.checkImport(task, items)
        return [items]

    # If it´s a console task
    elif task.startswith('Console'):
        if items.get('Import_Console') == True:
            value = ConsoleInterpreter.checkConsole(task, items)
            return [items, value]
        else:
            print("Error: Missing module 'Console'")
    
    # If it´s a variable thing
    elif task.startswith('var'):
        if items.get('Import_Variables') == True:
            content = VariableInterpreter.checkVariable(task, items)
            return [items, content]
        else:
            print("Error: Missing module 'Variables'")
    
    else:
        print("Error: Task not found")
    
    return [items, 0]
