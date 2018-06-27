#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

from tkinter import *

window = Tk()
window.title("GUI USING TKINTER")
window.geometry('500x350')
lbl = Label(window, text=" Hello World ")
lbl.grid(column=10, row=0)
btn = Button(window, text="Exit",command=window.destroy)
btn.grid(column=10, row=15)


#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.

def clicked():
    lbl = Label(window, text="HELLO SURPRISE")
    lbl.grid(column=10, row=12)
    
btn = Button(window, text="Just check me also", command=clicked)
btn.grid(column=10, row=10)
window.mainloop()




#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text. 

root = Tk()
root.title("SURPRISE AGAIN Q3")
#text what we want
disp = Label(root, text='YOU KNOW THAT! ')              
disp.pack()

def change_text():
    disp.config(text="YOU HAD DONE THIS")                                  

button = Button(root, text='ARE YOU SURE', command=change_text )
button.pack()                                               
exit_button = Button(root, text='EXIT', width=30, command=root.destroy)
exit_button.pack()
root.mainloop()




# Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.

root0 = Tk()
#window geometry 600x400 at (200,200)
root0.geometry("600x400+100+100")

# Create single line text entry box
entry = Entry(root0)
entry.pack()

entry.insert(INSERT, "INPUT PLEASE ! ")
def print_input():
    print(entry.get())

# TO PRINT BY FOLLOWING BUTTON
button = Button(root0, text='CLICK HERE TO PRINT', command=print_input)
button.pack()

exit_button = Button(root0, text='CLICK TO EXIT', command=root0.destroy)
exit_button.pack()
root0.mainloop()
