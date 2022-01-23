# Have access on Interpreter
import MainInterpreter

class Functions:
    @staticmethod
    def splitOldParameters(expression, origTask, items):
        expression = str(expression)
        parameters = {}
        mode = 'waiting'
        key = ''
        value = ''

        for i in expression:
            # No open parameter
            if mode == 'waiting':
                # if parameter open
                if i == '<':
                    mode = 'searchKey'
            # while recording key
            elif mode == 'searchKey':
                if i != ' ':
                    # switch mode
                    if i == '=':
                        mode = 'searchValue'
                    # record key
                    else:
                        key += i
            # while recording value
            elif mode == 'searchValue':
                # if i != ' ':                  # this deleted all spaces e.g. in input-msg

                # switch mode
                if i == '>':
                    value = MainInterpreter.checkTask(value, origTask, items)[0]
                    parameters[key] = value
                    key = value = ''

                    mode = 'waiting'
                # record value
                else:
                    value += i

        if mode != 'waiting':
            print("Error in '{}'.".format(origTask))
            print('Open parameter.')
        
        return [parameters, origTask, items]





    @staticmethod
    def splitParameters(expression, origTask, items):
        expression = str(expression)
        parameters = {}
        mode = 'searchKey'
        inValue = 0
        inString = -1
        key = ''
        value = ''
        
        for i in expression:
            # print(key, value, inString)
            # while recording key
            if mode == 'searchKey':
                if i != ' ':
                    # switch mode
                    if i == '=':
                        mode = 'searchValue'
                    # record key
                    else:
                        key += i

            # while recording value
            elif mode == 'searchValue':
                if i == "(" or i == "[":
                    inValue += 1
                    continue

                elif i==')' or i == ']':
                    inValue -= 1
                    continue

                elif i == '"':
                    inString *= -1

                elif inValue != 0 or inString == 1:
                    value += i

                elif i != ' ' and inValue == 0 and inString == -1:
                    if i == ',':
                        value = MainInterpreter.checkTask(value, origTask, items)[0]
                        parameters[key] = value
                        key = value = ''

                        mode = 'searchKey'

                    else:
                        value += i



        parameters[key] = value

        if inString == 1:
            print("Error in '{}'.".format(origTask))
            print('String ending not marked.')
            return [None, origTask, items]

        if inValue != 0:
            print("Error in '{}'.".format(origTask))
            print('Open brackets.')
            return [None, origTask, items]

        return [parameters, origTask, items]





    @staticmethod
    def splitElements(expression, origTask, items):
        expression = str(expression)
        elements = []
        element = ''
        inValue = 0
        inString = -1

        for i in expression:
            if i == ',' and (inValue == 0 or inString == 1):
                if element[0] == ' ':
                    element = element.replace(' ', '', 1)

                element = MainInterpreter.checkTask(element, origTask, items)[0]
                elements.append(element)
                element = ''
                continue

            elif i == '"':
                inString *= -1
            elif i == '[' or i == '(':
                inValue += 1
            elif i == ']' or i == ')':
                inValue -= 1
            element += i


        if element != '':
            if element[0] == ' ':
                element = element.replace(' ', '', 1)
            element = MainInterpreter.checkTask(element, origTask, items)[0]
            elements.append(element)

        if inString == 1:
            print("Error in '{}'.".format(origTask))
            print('String ending not marked.')
            return [None, origTask, items]

        if inValue != 0:
            print("Error in '{}'.".format(origTask))
            print('Open brackets.')
            return [None, origTask, items]

        return [elements, origTask, items]