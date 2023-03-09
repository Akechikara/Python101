from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมตารางสูตรคูณ')
GUI.geometry('600x600')

L1 = Label(GUI,text='ตารางสูตรคูณแม่สอง',fg='green')
L1.place(x=20,y=20)

def Button1():
    text = 'แม่สอง' messagebox.showinfo('ท่องสูตรคูณ',text)

FB1 = LabelFrame(GUI,text='') FB1.place(x=50,y=50) B1 =
ttk.Button(FB1,text='สูตรคูณแม่สองมาท่องสูตรคูณกัน',command=Button1)
B1.pack(ipadx=10,ipady=10)

# 2x2
def Button2():
    text = '4'
    messagebox.showinfo('มีค่าเท่ากับ',text)

B2 = ttk.Button(GUI,text='2x2',command=Button2)
B2.pack(ipadx=10,ipady=10)

# 2x3
def Button3():
    text = '6'
    messagebox.showinfo('มีค่าเท่ากับ',text)

B3 = ttk.Button(GUI,text='2x3',command=Button3)
B3.pack(ipadx=10,ipady=10)

# 2x4
def Button4():
    text = '8'
    messagebox.showinfo('มีค่าเท่ากับ',text)

B4 = ttk.Button(GUI,text='2x4',command=Button4)
B4.pack(ipadx=10,ipady=10)

# 2x5
def Button5():
    text = '10'
    messagebox.showinfo('มีค่าเท่ากับ',text)

B5 = ttk.Button(GUI,text='2x5',command=Button5)
B5.pack(ipadx=10,ipady=10)

