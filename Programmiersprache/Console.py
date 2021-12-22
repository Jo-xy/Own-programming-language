def out(output):
    print(output)
    return output

def read(msg = '', datatype='str'):               # msg = info message
    txt = input(msg)                              # txt = user´s input

    if datatype == 'str':
        return txt

    elif datatype == 'int':
        try:
            txt = int(txt)
            return txt
        except ValueError:
            print("Error: Value can not be converted to integer.")
            return "Error: Value can not be converted to integer."

    elif datatype == 'float':
        try:
            txt = float(txt)
            return txt
        except ValueError:
            print("Error: Value can not be converted to float.")
            return "Error: Value can not be converted to float."

    elif datatype == 'bool':
        if 'true' in txt.lower() and 'false' in txt.lower():
            print("Error: Not sure if to convert in bool as True or False.")
            return "Error: Not sure if to convert in bool as True or False."
        elif 'true' in txt.lower():
            return True
        elif 'false' in txt.lower():
            return False
        else:
            print("Error: Can not find bool in input.")
            return "Error: Can not find bool in input."

    else:
        print("Error: No valid datatype.")
        return "Error: No valid datatype."