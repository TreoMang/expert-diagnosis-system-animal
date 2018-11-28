from tkinter import * #If you get an error here, try Tkinter not tkinter

def Dialog1Display():
    Dialog1 = Toplevel(height=100, width=100) #Here

def Dialog2Display():
    Dialog2 = Toplevel(height=1000, width=1000) #Here

master=Tk()

Button1 = Button(master, text="Small", command=Dialog1Display)
Button2 = Button(master, text="Big", command=Dialog2Display)

Button1.pack()
Button2.pack()
master.mainloop()