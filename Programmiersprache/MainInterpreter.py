# A few small algorithms to make interpreting easier

# All the sub-interpreters
import ImportInterpreter
import ConsoleInterpreter
import VariableInterpreter
import StringInterpreter

def checkTask(task, items):
    # If it큦 an import
    if task.startswith('import'):
        items = ImportInterpreter.checkImport(task, items)[0]
        return [items]



    # If it is just a string
    elif task.startswith('"'):
        string = StringInterpreter.checkString(task, items)[0]
        return [string, items]

    

    # If it큦 a variable thing
    elif task.startswith('var'):
        if items.get('Import_Variables') == True:
            content = VariableInterpreter.checkVariable(task, items)[0]
            return [content, items]
        else:
            print("Error: Missing module 'Variables'")



    # If it큦 a console task
    elif task.startswith('Console'):
        if items.get('Import_Console') == True:
            value = ConsoleInterpreter.checkConsole(task, items) # Here is no [0] needed, because not a list is returned
            return [value, items]
        else:
            print("Error: Missing module 'Console'")
    

    # If nothing of this, check if it큦 a variable etc...
    else:
        itemTypes = ['Variable_', 'Import_']
        itemFound = None
        for i in itemTypes:
            if items.get(i+task) != None:
                # Take found value
                itemFound = items.get(i+task)

                #special cases
                if i == 'Import_':
                    return [True, items]

                return [itemFound, items]

        # When no variable etc. was found
        if itemFound == False:
            print("Error: Task or expression not found")
    
    return [items]
