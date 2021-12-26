def checkString(task, items):
    if '"' in task:
        # If there is no second ´"´ to end string
        if task.count('"') == 1:
            print("Error: String ending not marked.")
            return [None, items]
        
        # If there are multiple strings
        elif task.count('"') > 2:
            print("Error: Multiple Strings not accepted.")
            return [None, items]

        # And as usual...
        else:
            # seperate string-text
            string = task.split('"')[1]
            return [string, items]
