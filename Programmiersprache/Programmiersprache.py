
#####################-This will be my own Programming language-#################

#####################-Project started: 19.12.2021-##############################



#####################-To-do-list-#################################################
'''
1. Hello World Program - Done on 19.12.2021 15:00
2. Working input function. - Done on 19.12.2021 17:00
3. Variables to save input. - partly done on 22.12.2021 18:00 - Done for the moment on 23.12.2021 on 16:40 
    3.1. Improve MainInterpreter to fit to variables - Completed on 23.12.2021 on 16:30
        3.1.1. set up a basic StringInterpreter - Done on 22.12.2021 on 19:20
        3.1.2. use StringInterpreter now in the other interpreters - Completed on 23.12.2021 on 16:30
            3.1.2.1. algorithm to find out the amount of parameters given - Done on 23.12.2021 on 15:00
            3.1.2.2. detect automatically if it is an expression (remove 'expression' parameter) - Done on 23.12.2021 on 16:30
                --> handels expressions as normal tasks
    3.2. be able to print Input again - Done on 23.12.2021 on 16:40
4. Solve multiple-parameter problem - Completely done on 26.12.2021 on 13:20
5. Be able to put tasks in as parameters - Done  on 26.12.2021 on 13:20 (May cause Error in future)
    --> still under observation / experimental feature
6. Be able to save numbers, bool, etc...

Until 1th March:
have a first, simple working interpreter to run a Hello World Program with maybe variables.
'''
import MainInterpreter


code = '''
import Console;
import Variables;

var Test = Console.read(<msg=Console.read()>);

Console.out(Test);

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
    items = feedback[-1]