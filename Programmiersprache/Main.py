
#####################-CTA-######################################################

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
            3.1.2.1. algorithm to find out the amount of arguments given - Done on 23.12.2021 on 15:00
            3.1.2.2. detect automatically if it is an expression (remove 'expression' parameter) - Done on 23.12.2021 on 16:30
                --> handels expressions as normal tasks
    3.2. be able to print Input again - Done on 23.12.2021 on 16:40

4. Solve multiple-parameter problem - Completely done on 26.12.2021 on 13:20

5. Be able to put tasks in as arguments - Done  on 26.12.2021 on 13:20 (May cause Error in future)
    --> still under observation / experimental feature

6. Be able to save numbers, bool, etc... - Completely done on 01.01.2022 on 15:50
    6.1. Detection of numbers - Done on 26.12.2021 on 14:20
    6.2. Detection of bool - Done on 01.01.2022 on 15:45

7. Have a start GUI
    7.1. Have an Input-field, write code there and run it - Done on 01.01.2021 on ~20:00
    7.2. Have a tick-box to import standard modules automatically
    7.3. Load text from existing file
    7.4. Option of running the code multiple times
    7.5. Design the interface

8. More detailed Error messages (with information about what caused the Error) - Completely done on 02.01.2022 on 10:45
    8.1. First fix input-bug that clears all spaces in input-msg - Done on 02.01.2022 on 09:05
         --> fixed. Problem was in 'splitParameters'. ALL spaces were skipped, removed this. Now are spaces between/in parameters no longer allowed.
    8.2. Error massages (always past in the current original task, to print it when an Error happens) - Done on 02.01.2022 on 10:45
         --> saved at index -2 of every returned list. All functions need it now (2. last positional parameter)

9. time module - Done on 02.01.2021 on 20:54
   --> time.time(...), time.date(...), time.calendar()

10. CalculationInterpreter - Done
    10.1. Split Numbers correctly - Done on 04.01.2022 on 17:35
    10.2. Calculation of all types from left to right - Done on 04.01.2022 on 18:00
    10.3. Calculate '.' before '-' - Status on 04.01.2022 20:45: working on it nearly 3 hours and there are still weird bugs...
                                   - Fixed for '.'-calculation on 08.01.2022 on 14:15
                                   - Completely done on  08.01.2022 on 14:25
    
    10.4. Maybe be able to use brackets, probably not so good/possible? check it later!!!

11. If-blocks - Done for the moment on 09.01.2022 on 18:00
    11.1. IfInterpreter detects a CodeBlock and is able to end it - Probably done on 09.01.2022 on 14:10 - Right, Done!
    11.2. Detailed Interpretation of boolExpression given after 'if' - Done on 09.01.2022 on 17:50
    --> Maybe add more options in future

12. Create datatype 'list' - Done 
    12.1. Fix parameter problem and replace the <> functionalities with commas (maybe do it in a seperate module if it is too complex) - Done in Functions on 21.01.2022 on 21:25
        12.1.1. Adapt this a little bit to use it for lists etc... - Check later if it works - Done on 22.01.2022
        12.1.2. Renew or add Error messages for the parameter- or list-splitting system - Done on 22.01.2022
    12.2. After this, it should be easy to introduce lists by [element1, element2] - Done on 22.01.2022 on 13:45
    12.3. Find a way to get values at special indeces - getIndex(variablename, indexnumber) - Done on 22.01.2022 on 18:15
    12.4. Change indeces - setIndex(variablename, indexNumber, newValue) - Done on 23.01.2022 on 13:50
    12.5. Be able to use a constructor to create a list with a special number of spaces inside - Done on 22.01.2022 on 19:15
    --> e.g. [:5] creates a list with 5 times None inside
    12.6. Give the constructor also a value that he has to put in all of those gaps - Done on 22.01.2022 on 19:50
    --> e.g. write [:7:"Hi"] to create a list with seven times the string "Hi" inside
    12.7. Negative indeces - Done on 23.01.2022 on 19:49
    12.8. Bugfixes - Done on 25.01.2022 on 18:30

13. type() function - Done on 29.01.2022 on 14:00

14. String functions/slicing - Started on 30.01.2022 on 14:00 - Done for the moment on 31.01.2022 on 13:00
    14.1. split(element, splitpoint) - Done on 30.01.2022 on 14:30
    14.2. combine(elementList) - Done on 30.01.2022 on 17:45 (worked on it for around 15 minutes)
    14.3. toUpper() and toLower() - Done on 30.01.2022 on 19:00 (worked on it for ~20+ minutes)
    14.4. invertcase() changes uppercase to lowercase and the other way around + capitalize() all lowecase but the first uppercase - Done on 31.01.2022 on 11:30
    14.5. isfirst() and islast() - Done on 31.01.2022 on 11:45
    14.6. remove(obj, ValueToRemove) - Done on 31.01.2022 on 12:55
    14.7. replace(obj, oldValue, newValue) - Done on 31.01.2022 on 13:00

15. len() function - Done on 31.01.2022 on 14:10

16. List functions/slicing - Started on 31.01.2022 on 14:10 - Done for the moment on 31.01.2022 on 17:15
    16.1. Adapt string remove() and replace() to lists - Done on 31.01.2022 on 16:05
    16.2. addIndex() and deleteIndex() and append() and extend() - Done on 31.01.2022 on 17:05
    16.3. searchValue(element, searchedValue) (maybe change functionname in future) - Done on 31.01.2022 on 17:15

17. While-loops 
    .IDEA() - Maybe do not loop through the original task, but first go through the tasks and add them each by each to the tasklist? - NO!! Will not work when user has to do an input!!

18. For-loops

19. Random module/functionalities

20. Text encryption 



Until 1th March:
have a first, simple working interpreter to run a Hello World Program with maybe variables.
'''
import MainInterpreter
import StartGUI

code = StartGUI.Start()

code = code.replace('\n', '')


IfBlocks = []
items = {'IfBlocks': IfBlocks}              # All variables, imports, in future objects, etc... # Also has CodeBlocks in it

# remove last task-splitting-symbol to prevent 'Task not found' Error
if code[-1] == ';':
    code = code[:-1]
# seperate tasks
tasks = code.split(';')


for task in tasks:
    feedback = MainInterpreter.checkTask(task, task, items, code=code)

    # Remove this in Future!
    # Items is updated automatically, but is maybe still usefull (or actually used) as control-thing
    items = feedback[-1]
