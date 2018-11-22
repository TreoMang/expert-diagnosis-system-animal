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
        
        # cb = Checkbutton(self,)
        # frame1 = Frame()
        # frame1.pack(fill=X)
        # label1 = Label(self,text="Chọn những đặc điểm của loài vật bạn muốn biết")
        # label1.pack(fill = X)
        # Checkbutton(self, text = "Lông", command = lambda: self.onClick(1)).place(x = 50, y = 50)
        # Checkbutton(self, text = "Lông vũ", command = lambda: self.onClick(2)).place(x = 50, y = 80)
        # Checkbutton(self, text = "Trứng",command = lambda: self.onClick(3)).place(x = 50, y = 110)
        # Checkbutton(self, text = "Có thể bay",command = lambda: self.onClick(4)).place(x = 50, y = 140)
        # Checkbutton(self, text = "Có thể sống dưới nước",command = lambda: self.onClick(5)).place(x = 50, y = 170)
        # Checkbutton(self, text = "Ăn thịt", command = lambda: self.onClick(6)).place(x = 50, y = 200) 
        # Checkbutton(self, text = "Răng",command = lambda: self.onClick(7)).place(x = 50, y = 230)
        # Checkbutton(self, text = "Vây", command = lambda: self.onClick(8)).place(x = 50, y = 260)
        # Checkbutton(self, text = "Chân", command = lambda: self.onClick(9)).place(x = 50, y = 290)

        label1 = Label(self,text="Chọn những đặc điểm của loài vật bạn muốn biết")
        label1.pack(fill = X)
        Radiobutton(self,text = "Có",command = lambda: self.onClick(1)).place(x = 50, y = 50)
        Radiobutton(self,text = "Không",command = lambda: self.onClick(1)).place(x = 50, y = 70)
        Radiobutton(self,text = "Không biết",command = lambda: self.onClick(1)).place(x = 50, y = 90)

        # label2 = Label(self,text = "1. Nó có lông không ?")
        # label2.pack(fill = X)
        # Radiobutton(self,text = "Có",command = lambda: self.onClick(1)).place(x = 50, y = 50)

        # label3 = Label(self,text = "2. Nó có lông vũ không ?")
        # label3.pack(fill = X)

        # label4 = Label(self,text = "3. Nó có đẻ trứng không ?")
        # label4.pack(fill = X)

        # label5 = Label(self,text = "4. Nó có thể bay không ?")
        # label5.pack(fill = X)

        # label6 = Label(self,text = "5. Nó có thể sống dưới nước không ?")
        # label6.pack(fill = X)

        # label7 = Label(self,text = "6. Nó có ăn thịt không ?")
        # label7.pack(fill = X)

        # label8 = Label(self,text = "7. Nó có răng không ?")
        # label8.pack(fill = X)

        # label9 = Label(self,text = "8. Nó có thể xương không ?")
        # label9.pack(fill = X)

        # label5 = Label(self,text = "9. Nó có vây không ?")
        # label5.pack(fill = X)

        # label5 = Label(self,text = "10. Nó có mấy chân ?")
        # label5.pack(fill = X)


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