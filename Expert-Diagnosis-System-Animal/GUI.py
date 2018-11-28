from tkinter import Tk, Frame, BOTH, X, IntVar
from tkinter.ttk import Button, Label, Radiobutton
import animal
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
        label = Label(self,text="Chọn những đặc điểm của loài vật bạn muốn biết", font = "Helvetica 12 bold italic")
        label.pack(fill = X)

        v = []
        label = []
        for i in range(11):
            v.append(IntVar())
            label.append(Label())
        self.question = {
            1 : "1. Nó có lông không ?",
            2 : "2. Nó có răng không ?",
            3 : "3. Nó có xương không ?",
            4 : "4. Nó có đuôi không ?",
            5 : "5. Nó có đẻ trứng không ?",
            6 : "6. Nó có lông vũ không ?",
            7 : "7. Nó có thể bay không ?",
            8 : "8. Nó có thể sống dưới nước không ?",
            9 : "9. Nó có vây không ?",
            10 : "10. Nó có mấy chân ?",
            11 : "11. Nó có ăn thịt không ?"
        }

        j = 50
        xx = 50
        for i in range(11):
            if i == 6:
                xx = 300
                j = 50
            if i == 10:
                j = j + 60
            label[i] = Label(self,text = self.question[i+1], foreground = "blue", font ="Helvetica 10 bold italic")
            label[i].place(x = xx, y = j -20)
            j = j + 80

        j = 50
        xx = 50
        for i in range(11):
            if i == 6:
                xx = 300
                j = 50
            if i == 9:
                Radiobutton(self, value=0, text="0", variable=v[i]).place(x=xx,y=j)  # , command=lambda: self.onClick(1,1)
                Radiobutton(self, value=2, text="2", variable=v[i]).place(x=xx, y=j + 20)
                Radiobutton(self, value=4, text="4", variable=v[i]).place(x=xx, y=j + 40)
                Radiobutton(self, value=6, text="6", variable=v[i]).place(x=xx, y=j + 60)
                Radiobutton(self, value=8, text="8", variable=v[i]).place(x=xx, y=j + 80)
                j = j + 140
                continue

            Radiobutton(self, value = 1, text="Có", variable  = v[i]).place(x=xx, y= j ) #, command=lambda: self.onClick(1,1)
            Radiobutton(self, value = 0, text="Không", variable  = v[i]).place(x=xx, y=j+20) #, command=lambda: self.onClick(1,0)
            j = j + 80


        #Sau khi tick het thi an Button OK hay gi do, roi chay if else cho moi variable, xet neu value la 1, 2 hay 3 thi thuc hien
        # cau lenh nao! = )) oK nhe :3

        button = Button(self,text = "Done",command = lambda : self.onClick(v,button))
        button.pack(fill = X)
        button.place(x = 50, y = 500)
        
    def onClick(self,value,button):
        p = animal.Process(value)

        label = Label(self,text = p.call_again(),foreground = "orange", font = "Helvetica 18 italic").place(x = 50, y = 545)



            
    
    


root = Tk()
root.geometry("550x600+300+100")
app = Example(root)
root.mainloop()