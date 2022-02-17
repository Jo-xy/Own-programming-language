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
import IfInterpreter
import ListInterpreter
import IndexInterpreter
import TypeInterpreter
import LenInterpreter
import WhileInterpreter

def checkTask(task, origTask, items, code=None, tasknum=None, tasks=None):
    # When you are inside a IfBlock
    if items.get('IfBlocks') != []:
        # When the ending of the Block is marked
        if task.startswith('end '):
            try:
                endedBlock = task.split('end ')[1]
                items['IfBlocks'].remove(endedBlock)
                return [None, origTask, items]

            except IndexError:
                print("Error in '{}'.".format(origTask))
                print('Missing Argument.')
                return [None, origTask, items]

            #except ValueError:
            #    return [None, origTask, items]

        return [None, origTask, items]

    


    # At the end of While-block: decide if to do again
    if items.get('WhileBlocks') != {}:
        if task.startswith('end '):
            endedBlock = task.split('end ')[1]
            goto = items['WhileBlocks'].get(endedBlock)
            # print(goto)

            if goto != None and type(goto) == int:
                goto = "###gotoline " + str(goto)
                return [goto, origTask, items]
            else:
                return [None, origTask, items]


    # while-blocks
    if task.startswith('while'):
        if tasknum != None:
            safetyFeedback = WhileInterpreter.checkWhileBlock(task, tasknum, origTask, items)
            return safetyFeedback
        else:
            print("Error in '{}'.".format(origTask))
            print("Loop 'while' can only be used as main task..")
            return [None, origTask, items]




    # If it큦 an import
    elif task.startswith('import'):
        items = ImportInterpreter.checkImport(task, origTask, items)[-1]
        return [origTask, items]



    # If it is just a string
    elif task.startswith('"'):
        string = StringInterpreter.checkString(task, origTask, items)[0]
        return [string, origTask, items]

    ##String-module##
    elif task.startswith('split('):
        splittedString = StringInterpreter.splitString(task, origTask, items)[0]
        return [splittedString, origTask, items]

    elif task.startswith('combine('):
        combinedString = StringInterpreter.combineListElementsToString(task, origTask, items)[0]
        return [combinedString, origTask, items]

    elif task.startswith('toUpper('):
        uppercaseString = StringInterpreter.toUpper(task, origTask, items)[0]
        return [uppercaseString, origTask, items]

    elif task.startswith('toLower('):
        lowercaseString = StringInterpreter.toLower(task, origTask, items)[0]
        return [lowercaseString, origTask, items]

    elif task.startswith('invertcase('):
        invertedString = StringInterpreter.invertcase(task, origTask, items)[0]
        return [invertedString, origTask, items]

    elif task.startswith('capitalize('):
        capitalizedString = StringInterpreter.capitalize(task, origTask, items)[0]
        return [capitalizedString, origTask, items]

    elif task.startswith('isFirst('):
        isFirst = StringInterpreter.isFirst(task, origTask, items)[0]
        return [isFirst, origTask, items]

    elif task.startswith('isLast('):
        isLast = StringInterpreter.isLast(task, origTask, items)[0]
        return [isLast, origTask, items]

    # later also used for lists
    elif task.startswith('remove('):
        shortedElement = StringInterpreter.remove(task, origTask, items)[0]
        return [shortedElement, origTask, items]

    # later also used for lists
    elif task.startswith('replace('):
        modifiedElement = StringInterpreter.replace(task, origTask, items)[0]
        return [modifiedElement, origTask, items]
    ##-|-<End of String-module>-|-##


    ##List-module##
    elif task.startswith('addIndex('):
        newList = ListInterpreter.addIndex(task, origTask, items)[0]
        return [newList, origTask, items]

    elif task.startswith('deleteIndex('):
        newList = ListInterpreter.deleteIndex(task, origTask, items)[0]
        return [newList, origTask, items]

    elif task.startswith('append('):
        newList = ListInterpreter.appendIndex(task, origTask, items)[0]
        return [newList, origTask, items]

    elif task.startswith('extend('):
        newList = ListInterpreter.extendList(task, origTask, items)[0]
        return [newList, origTask, items]

    elif task.startswith('searchValue'):
        listOfIndeces = ListInterpreter.searchValue(task, origTask, items)[0]
        return [listOfIndeces, origTask, items]
    ##-|-<End of List-module>-|-##


    # If it is a number
    elif task.replace('.', '', 1).replace('-', '', 1).isdigit():
        number = NumberInterpreter.checkNumber(task, origTask, items)[0]
        return [number, origTask, items]


    # If it is a boolean
    elif task.startswith('True') or task.startswith('False'):
        value = BoolInterpreter.checkBool(task, origTask, items)[0]
        return [value, origTask, items]


    # If it큦 a list
    elif task.startswith('['):
        listElements = ListInterpreter.checkList(task, origTask, items)[0]
        return [listElements, origTask, items]


    # If it큦 a variable thing
    elif task.startswith('var '):
        content = VariableInterpreter.checkVariable(task, origTask, items)[0]
        return [content, origTask, items]


    # Set Indeces
    elif task.startswith('setIndex('):
        newValue, origTask, items = IndexInterpreter.setIndex(task, origTask, items)
        return [newValue, origTask, items]

    # Get indeces
    elif task.startswith('getIndex('):
        value = IndexInterpreter.getIndex(task, origTask, items)[0]
        return [value, origTask, items]


    # type() function
    elif task.startswith('type('):
        datatype = TypeInterpreter.checkType(task, origTask, items)[0]
        return [datatype, origTask, items]


    # len() function
    elif task.startswith('len('):
        length = LenInterpreter.length(task, origTask, items)[0]
        return [length, origTask, items]


    # If it is a calculation
    elif task.startswith('calc'):
        # check if there is something to calculate
        try:
            task = task.split('calc ')[1]
            result = CalculationInterpreter.calculate(task, origTask, items)[0]
            return [result, origTask, items]
        except IndexError:
            return [None, origTask, items]


    # if-blocks
    elif task.startswith('if'):
        safetyFeedback = IfInterpreter.checkIfBlock(task, origTask, items)
        return safetyFeedback


    # If it큦 a console task
    elif task.startswith('Console'):
        value = ConsoleInterpreter.checkConsole(task, origTask, items)[0]
        return [value, origTask, items]


    # time module
    elif task.startswith('time'):
        if items.get('Import_time') == True:
            value = TimeInterpreter.checkTime(task, origTask, items)[0]
            return [value, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Missing module 'time'.")
    


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
                    return [True, origTask, items]

                return [itemFound, origTask, items]

        # When no variable etc. was found
        if itemFound == False:
            print("Error in '{}'.".format(origTask))
            print("Task or expression not found")
    
    return [None, origTask, items]
