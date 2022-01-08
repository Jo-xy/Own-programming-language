# A few small algorithms to make interpreting easier

# All the sub-interpreters
import ImportInterpreter
import ConsoleInterpreter
import VariableInterpreter
import StringInterpreter
import NumberInterpreter
import BoolInterpreter
import TimeInterpreter
import CalculationInterpreter

def checkTask(task, origTask, items):
    # If it�s an import
    if task.startswith('import'):
        items = ImportInterpreter.checkImport(task, origTask, items)[-1]
        return [origTask, items]



    # If it is just a string
    elif task.startswith('"'):
        string = StringInterpreter.checkString(task, origTask, items)[0]
        return [string, origTask, items]

    # If it is a number
    elif task.replace('.', '', 1).isdigit():
        number = NumberInterpreter.checkNumber(task, origTask, items)[0]
        return [number, origTask, items]

    # If it is a boolean
    elif task.startswith('True') or task.startswith('False'):
        value = BoolInterpreter.checkBool(task, origTask, items)[0]
        return [value, origTask, items]

    # If it�s a variable thing
    elif task.startswith('var'):
        if items.get('Import_Variables') == True:
            content = VariableInterpreter.checkVariable(task, origTask, items)[0]
            return [content, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Missing module 'Variables'.")

    # If it is a calculation
    elif task.startswith('calc'):
        if items.get('Import_Calculations') == True:
            # check if there is something to calculate
            try:
                task = task.split('calc ')[1]
                result = CalculationInterpreter.calculate(task, origTask, items)[0]
                return [result, origTask, items]
            except IndexError:
                return [None, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Missing module 'Calculations'.")

    # If it�s a console task
    elif task.startswith('Console'):
        if items.get('Import_Console') == True:
            value = ConsoleInterpreter.checkConsole(task, origTask, items)[0]
            return [value, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Missing module 'Console'.")

    elif task.startswith('time'):
        if items.get('Import_time') == True:
            value = TimeInterpreter.checkTime(task, origTask, items)[0]
            return [value, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Missing module 'time'.")
    

    # If nothing of this, check if it�s a variable etc...
    else:
        itemTypes = ['Variable_', 'Import_']
        itemFound = None
        for i in itemTypes:
            if items.get(i+task) != None:
                # Take found value
                itemFound = items.get(i+task)

                #special cases
                if i == 'Import_':
                    return [True, origTask, items]

                return [itemFound, origTask, items]

        # When no variable etc. was found
        if itemFound == False:
            print("Error in '{}'.".format(origTask))
            print("Task or expression not found")
    
    return [origTask, items]
