from tkinter import *
class MyWindow:
    def __init__(self,win):

        self.lbl1 = Label(win,text="1st No.")
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text= "2nd No.")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100,y=150)
        self.txt1 = Entry(win,bd=2)
        self.txt1.place(x=200,y=50)
        self.txt2 = Entry(win,bd=2)
        self.txt2.place(x=200,y=100)
        self.txt3 = Entry(win,bd=2)
        self.txt3.place(x=200,y=150)
        self.btnadd = Button(win,text="Addition", fg= "Blue")
        self.btnadd.place(x=100,y=200)
        self.btnadd.bind('<Button-1>', self.add)
        self.btnsub = Button(win,text="Subtraction", fg = "Violet")
        self.btnsub.place(x=170,y=200)
        self.btnsub.bind('<Button-1>', self.sub)
        self.btndiv = Button(win,text="Division", fg = "Orange")
        self.btndiv.place(x=350, y=200)
        self.btndiv.bind('<Button-1>',self.div)
        self.btnmul = Button(win, text="Multiplication", fg = "Green")
        self.btnmul.place(x=250, y=200)
        self.btnmul.bind('<Button-1>', self.mul)
        self.btnclr = Button(win, text="Clear", fg = "Red")
        self.btnclr.place(x=350, y=100)
        self.btnclr.bind('<Button-1>', self.clr)

    def add(self,add):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END,str(result))

    def sub(self,sub):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1-num2
        self.txt3.insert(END, str(result))

    def div(self,div):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1/num2
        self.txt3.insert(END, str(result))

    def mul(self, Mul):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1*num2
        self.txt3.insert(END, str(result))

    def clr(self, clr):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()