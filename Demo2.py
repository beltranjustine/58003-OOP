from tkinter import *

win=Tk()
win.geometry("400x300+10+10")
win.title("Grid Manager")
#begin placing your wigets here

txt1 = Entry(bd=2)
txt1.grid(row=0,column=0, sticky=N)
txt1.insert(0,"row 0" " column 0")

txt2 = Entry(bd=2)
txt2.grid(row=0,column=1, sticky=S)
txt2.insert(0,"row 0" " column 1")

txt3 = Entry(bd=2)
txt3.grid(row=0,column=2, sticky=S)
txt3.insert(0,"row 0" " column 2")

txt4 = Entry(bd=2)
txt4.grid(row=1,column=0, sticky=S)
txt4.insert(0,"row 1" " column 0")

txt5 = Entry(bd=2)
txt5.grid(row=1,column=1, sticky=S)
txt5.insert(0,"row 1" " column 1")

txt6 = Entry(bd=2)
txt6.grid(row=1,column=2, sticky=S)
txt6.insert(0,"row 1" " column 2")

txt7 = Entry(bd=2)
txt7.grid(row=2,column=0, sticky=S)
txt7.insert(0,"row 2" " column 0")

txt8 = Entry(bd=2)
txt8.grid(row=2,column=1, sticky=S)
txt8.insert(0,"row 2" " column 1")

txt9 = Entry(bd=2)
txt9.grid(row=2,column=2, sticky=S)
txt9.insert(0,"row 1" " column 2")

win.mainloop()