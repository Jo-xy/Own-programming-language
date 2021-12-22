
#####################-This will be my own Programming language-#################

#####################-Project started: 19.12.2021-##############################



#####################-Todolist-#################################################
'''
1. Hello World Program - Done on 19.12.2021 15:00
2. Working input function. - Done on 19.12.2021 17:00
3. Variables to save input.
4. Print Input again

Until 1th March:
have a first, simple working interpreter to run a Hello Worl Program with maybe variables.
'''
import MainInterpreter


code = '''
import Console;
import Variables;
var Working;
Console.out("Hallo Welt");
'''
code = code.replace('\n', '')



items = {}              # All variables, imports, in future objects, etc...

# remove last task-splitting-symbol to prevent 'Task not found' Error
if code[-1] == ';':
    code = code[:-1]
# seperate tasks
tasks = code.split(';')

for task in tasks:
    feedback = MainInterpreter.checkTask(task, items)
    items = feedback[0]