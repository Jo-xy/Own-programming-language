# Have access on Interpreter
import MainInterpreter

class Functions:
    @staticmethod
    def splitParameters(expression, items):
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
                if i != ' ':
                    # switch mode
                    if i == '>':
                        value = MainInterpreter.checkTask(value, items)[0]
                        parameters[key] = value
                        key = value = ''

                        mode = 'waiting'
                    # record value
                    else:
                        value += i

        if mode != 'waiting':
            print('Error: Open parameter.')
        
        return [parameters, items]