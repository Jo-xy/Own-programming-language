def checkNumber(number, origTask, items):
    # When it is a float...
    if '.' in number:
        return [float(number), origTask, items]
    # Or just an integer
    else:
        return [int(number), origTask, items]
