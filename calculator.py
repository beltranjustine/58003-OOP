from tkinter import*
windows = Tk()
label1 = Label(windows,text = "My First Application",fg = "Red", font ="Verdana",)
label1.place(x=200,y=20)
label2 = Label(windows,text = "Name:",fg = "Light Blue")
label2.place(x=100,y=80)
label3 = Label(windows,text = "Age:", fg = "Light Blue")
label3.place(x=100,y=100)
label4 = Label(windows,text = "Birthdate:", fg = "Light Blue")
label4.place(x=100,y=120)

txtfld1 = Entry(windows,bd=2)
txtfld1.place(x=200,y=80)


windows.geometry("600x400+10+10")
windows.mainloop()