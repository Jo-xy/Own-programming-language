import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
   


def Start():
    root = tk.Tk()
    root.geometry("800x650")


    # Show logo
    image = Image.open('Logo.png')         #.resize((195, 110))
    photo = ImageTk.PhotoImage(image)
    logoLbl = ttk.Label(root, image=photo, text="Console tasks automation", compound="top", font=("Arial", 12))
    logoLbl.pack(padx=10)


    #Entry field
    from tkinter.scrolledtext import ScrolledText
    entry = ScrolledText(root, wrap=tk.WORD, font=('Arial', 10), width=100, relief="sunken", borderwidth=10)
    entry.pack()
    entry.insert(tk.INSERT, "Enter your code here")


    # status information 
    buttonMsg = tk.StringVar()
    buttonMsg.set("Waiting for input...")
    running = True
    def runCode():
        global code, running
        # save code
        code = entry.get('1.0', 'end-1c')

        # shut down
        running = False

        # reset status
                                                                                               # entry.delete('1.0', tk.END)
        buttonMsg.set("You can close this window now. Your code is running.")                  # entry.insert(tk.INSERT, "You can close this window now. Your code is running.")

        tk.Tk.quit(root)

    runButton = ttk.Button(textvariable=buttonMsg, command=runCode, state='disabled')
    runButton.pack(fill="x", padx=100, pady=20)


    # define permanantly running function for checking 
    def update():
        global running
        # change status-button
        if entry.get('1.0', 'end-1c') != 'Enter your code here':
            try:
                if running == True:
                    buttonMsg.set('Run')
                    runButton['state'] = 'normal'
            except NameError:
                buttonMsg.set('Run')
                runButton['state'] = 'normal'
        else:
            buttonMsg.set('Waiting for input...')
            runButton['state'] = 'normal'
        
        try:
            if running == True:
                root.after(100, update)
        except NameError:
            root.after(100, update)

    # make 'update' running permanantly
    after_id = root.after(100, update)

    # Open window
    root.mainloop()

    # end loop
    root.after_cancel(after_id)

    # return the code to main-script
    try:
        return code
    except NameError:
        return " "
    

'''
import Console;
import Variables;

var Test = True;
var TXT = Console.read(<msg="Bitte Bool eingeben: "><datatype="bool">);

Console.out(Test);
Console.out(TXT);
'''
