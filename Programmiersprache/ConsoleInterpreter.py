import Console

def checkConsole(task, items):
    task = task.split('.', 1)[1]

    if task.startswith('out'):
        output = task.split('"')[1]
        return Console.out(output)
        

    elif task.startswith('read'):
        task = task.split('(', 1)[1]

        if 'msg' in task and not 'datatype' in task:
            task = task.split('"')[1]
            return Console.read(msg = task)

        elif 'datatype' in task and not 'msg' in task:
            task = task.split('"')[1]
            return Console.read(datatype = task)

        elif 'msg' in task and 'datatype' in task:
            if task.find('msg') < task.find('datatype'):
                msg = task.split('=')[1]
                msg = msg.split('"')[1]
                datatype = task.split('=')[2]
                datatype = datatype.split('"')[1]
                return Console.read(msg = msg, datatype = datatype)
            else:
                datatype = task.split('=')[1]
                datatype = datatype.split('"')[1]
                mag = task.split('=')[2]
                msg = msg.split('"')[1]
                return Console.read(msg = msg, datatype = datatype)

        else:
            return Console.read()
