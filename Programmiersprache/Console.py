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
            return ["Error", origTask, items]

    elif datatype == 'float':
        try:
            txt = float(txt)
            return [txt, origTask, items]
        except ValueError:
            print("Error in '{}'.".format(origTask))
            print("Value can not be converted to float.")
            return ["Error", origTask, items]

    elif datatype == 'bool':
        if 'True' in txt and 'False' in txt:
            print("Error in '{}'.".format(origTask))
            print("Not sure if to convert in bool as True or False.")
            return ["Error", origTask, items]
        elif 'True' in txt:
            return [True, origTask, items]
        elif "False" in txt:
            return [False, origTask, items]
        else:
            print("Error in '{}'.".format(origTask))
            print("Can not find bool in input.")
            return ["Error", origTask, items]

    else:
        print("Error: No valid datatype.")
        return ["Error", origTask, items]