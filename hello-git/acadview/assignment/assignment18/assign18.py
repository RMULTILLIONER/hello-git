#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.



from tkinter import *
root = Frame()
root.pack()

a = {'RAVINDER':'9999999999','RAVI':'8888888888','RAVINDER_SINGH':'7777777777','RMULTILLIONER':'6666666666','RAVI1':'8888888887','RAVINDER_SINGH1':'7777777778','RMULTILLIONER1':'6666666668'}

ITEM1 = Label(root,text="HEY! WHAT'S YOUR NAME?")
ITEM1.pack(side="top")
ITEM2 = Label(root,text="CLICK YOUR NAME TO GET NO.")
ITEM2.pack(side="top")

def handleList(event):
    NAME = LIST.get(ACTIVE) 
    print(NAME)
    b = a.get(NAME)
    global ITEM1,ITEMt2
    ITEM1.config(text=NAME)
    ITEM2.config(text=b)  

LIST = Listbox(root)
sbar = Scrollbar(root)
sbar.config(command=LIST.yview)
LIST.config(yscrollcommand=sbar.set) 
sbar.pack(side=LEFT, fill=Y) 
LIST.pack(side=RIGHT, expand=YES, fill=BOTH)
LIST.bind('<Double-1>', handleList)

for k,v in a.items():        #ITEM INSERTION
    LIST.insert('end',k)

root.mainloop()



