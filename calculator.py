from tkinter import *
import tkinter.messagebox
root= Tk()
root.title("parag's computer")
root.geometry("350x450")

def myclick(number):
	e.insert(END, number)

def equal():
	try:
		y = str(eval(e.get()))
		e.delete(0, END)
		e.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Error")

		 
def clear():
    e.delete(0,END)
a = Frame(master=root,background="skyblue")
a.pack( side=RIGHT, fill=BOTH, expand=True,)
c = Label(a , text="BASIC CALCULATOR", bg="skyblue", relief=RIDGE , font=bool,borderwidth="7")
c.pack(pady=30)

p= Frame(a, bg="skyblue")
p.pack()

e= Entry(p)
e.grid (columnspan=4)

f= Button(p, text="1", width="10", command=lambda :myclick(1))
f.grid(pady=5, column=1, row=1)

f1= Button(p, text="2", width="10", command=lambda :myclick(2))
f1.grid(pady=5, column=2, row=1)

f2= Button(p, text="3", width="10", command=lambda :myclick(3))
f2.grid(pady=5, column=3, row=1)


f3= Button(p, text="4", width="10", command=lambda :myclick(4))
f3.grid(pady=5, column=1, row=2)

f4= Button(p, text="5", width="10", command=lambda :myclick(5))
f4.grid(pady=5, column=2, row=2)

f5= Button(p, text="6", width="10", command=lambda :myclick(6))
f5.grid(pady=5, column=3, row=2)

f6= Button(p, text="7", width="10", command=lambda :myclick(7))
f6.grid(pady=5, column=1, row=3)

f7= Button(p, text="8", width="10", command=lambda :myclick(8))
f7.grid(pady=5, column=2, row=3)

f8= Button(p, text="9", width="10", command=lambda :myclick(9))
f8.grid(pady=5, column=3, row=3)

f9= Button(p, text="0", width="10", command=lambda :myclick(0))
f9.grid(pady=5, column=2, row=4)

f10= Button(p, text="clear", width="10", command=lambda :clear())
f10.grid(pady=5, column=2, row=5)

f11= Button(p, text="equal", width="10", command=lambda :equal())
f11.grid(pady=5, column=2, row=6)

f12= Button(p, text="+", width="10", command=lambda :myclick('+'))
f12.grid(pady=5, column=1, row=7)

f13= Button(p, text="-", width="10", command=lambda :myclick('-'))
f13.grid(pady=5, column=2, row=7)

f14= Button(p, text="*", width="10", command=lambda :myclick('*'))
f14.grid(pady=5, column=3, row=7)

f15= Button(p, text="/", width="10", command=lambda :myclick('/'))
f15.grid(pady=5, column=2, row=8)

root.mainloop()
