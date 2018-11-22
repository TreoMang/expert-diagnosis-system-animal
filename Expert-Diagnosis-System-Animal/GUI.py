from tkinter import Tk, Frame, BOTH, X, IntVar, LEFT, W
from tkinter.ttk import Button, Label, Radiobutton, Checkbutton
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        """
        self.attributes = [
            ("Hair",1),("Feathers",2),("Eggs",3),("Airborne",4),("Domestic",5),("Predator",6),
            ("Toothed",7),("Fins",8),("0 Leg",9),("2 Legs",91),("4 Legs",92),("6 Legs",93),("8 Legs",94),("Tail",10)
        ]
        """
        self.attributes = [
            "Hair","Feathers","Eggs","Airborne","Domestic","Predator",
            "Toothed","Fins","0 Leg""2 Legs","4 Legs","6 Legs","8 Legs","Tail"
        ]
        
        cb = Checkbutton(self,)
        frame1 = Frame()
        frame1.pack(fill=X)
        label1 = Label(self,text="Chọn những đặc điểm của loài vật bạn muốn biết")
        label1.pack(fill = X)
        Checkbutton(self, text = "Lông", command = lambda: self.onClick(1)).place(x = 50, y = 50)
        Checkbutton(self, text = "Lông vũ", command = lambda: self.onClick(2)).place(x = 50, y = 80)
        Checkbutton(self, text = "Trứng",command = lambda: self.onClick(3)).place(x = 50, y = 110)
        Checkbutton(self, text = "Có thể bay",command = lambda: self.onClick(4)).place(x = 50, y = 140)
        Checkbutton(self, text = "Có thể sống hoàn toàn dưới nước",command = lambda: self.onClick(5)).place(x = 50, y = 170)
        Checkbutton(self, text = "Ăn thịt", command = lambda: self.onClick(6)).place(x = 50, y = 200) 
        Checkbutton(self, text = "Răng",command = lambda: self.onClick(7)).place(x = 50, y = 230)
        Checkbutton(self, text = "Vây", command = lambda: self.onClick(8)).place(x = 50, y = 260)
        Checkbutton(self, text = "Chân", command = lambda: self.onClick(9)).place(x = 50, y = 290)

        button = Button(self,text = "Done",command = self.quit)
        button.pack(fill = X)
        button.place(x = 50, y = 320)
        
    def onClick(self,key):
        for k, attribute in enumerate(self.attributes):
            if k == (key-1):
                print(attribute)
                break

            
    
    


root = Tk()
root.geometry("500x400+300+300")
app = Example(root)
root.mainloop()