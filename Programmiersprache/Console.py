import ListInterpreter

def out(output, origTask, items):
    print(output)
    return [output, origTask, items]

def read(origTask, items, msg = '', datatype='str'):               # msg = info message
    txt = input(msg)                              # txt = user´s input

    if datatype == 'str':
        return [txt, origTask, items]

    elif datatype == 'int':
        try:
            txt = int(txt)
            return [txt, origTask, items]
        except ValueError:
            print("Error in '{}'.".format(origTask))
            print("Value can not be converted to integer.")
            return [None, origTask, items]

    elif datatype == 'float':
        try:
            txt = float(txt)
            return [txt, origTask, items]
        except ValueError:
            print("Error in '{}'.".format(origTask))
            print("Value can not be converted to float.")
            return [None, origTask, items]

    elif datatype == 'bool':
        if 'True' in txt and 'False' in txt:
            print("Error in '{}'.".format(origTask))
            print("Not sure if to convert in bool as True or False.")
            return [None, origTask, items]
        elif 'True' in txt:
            return [True, origTask, items]
        elif "False" in txt:
            return [False, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Can not find bool in input.")
            return [None, origTask, items]

    elif datatype == 'list':
        if txt.startswith('['):
            inputList = ListInterpreter.checkList(txt, origTask, items)[0]
            if inputList != None:
                return [inputList, origTask, items]
            else:
                print("Error in '{}'.".format(origTask))
                print("Can not find list in input.")
                return [None, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Can not find list in input.")
            return [None, origTask, items]

    else:
        print("Error in '{}'.".format(origTask))
        print("No valid datatype.")
        return ["Error", origTask, items]