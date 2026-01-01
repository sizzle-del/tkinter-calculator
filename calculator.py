import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
 
def btn_1_isclicked():
	global val
	val = val + "1"
	data.set(val)
	
def btn_2_isclicked():
	global val
	val = val + "2"
	data.set(val)

def btn_3_isclicked():
	global val
	val = val + "3"
	data.set(val)
	
def btn_4_isclicked():
	global val
	val = val + "4"
	data.set(val)
	
def btn_5_isclicked():
	global val
	val = val + "5"
	data.set(val)
	
def btn_6_isclicked():
	global val
	val = val + "6"
	data.set(val)
	
def btn_7_isclicked():
	global val
	val = val + "7"
	data.set(val)
	
def btn_8_isclicked():
	global val
	val = val + "8"
	data.set(val)
	
def btn_9_isclicked():
	global val
	val = val + "9"
	data.set(val)
	
def btn_0_isclicked():
	global val
	val = val + "0"
	data.set(val)

def btn_plus_isclicked():
	global val
	val += "+"
	data.set(val)


def btn_minus_isclicked():
	global val
	val += "-"
	data.set(val)

def btn_mult_isclicked():
	global val
	val += "*"
	data.set(val)
	
def btn_div_isclicked():
	global val
	val += "/"
	data.set(val)

def btn_c_isclicked():
	global val
	val = ""
	data.set(val)
	
def result():
	global val 
	try :
		c = eval(val)
		data.set(c)
		val = str(c)
	except ZeroDivisionError:
		messagebox.showerror("error, divison by zero is invalid")
		val =""
		data.set(val)
	except :
		messagebox.showerror("error, invalid expression")
		val =""
		data.set(val)
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(100,100)
root.title("Calculator")



data = StringVar()
lbl = Label(root,text = "Label", anchor = SE,font = ("Digital-7",25),textvariable = data,background ="#ffffff",fg = "#000000" )
lbl.pack(expand = True,fill = "both")



btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand = True, fill = "both",)


btnrow2 = Frame(root)
btnrow2.pack(expand = True,fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True,fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True,fill = "both")


#row 1
btn1 = Button(btnrow1,text = "1",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_1_isclicked)
btn1.pack(side = LEFT,expand = True,fill = "both",)

btn2 = Button(btnrow1,text = "2",font = ("Digital-7",30),relief =  GROOVE,border = 0,command = btn_2_isclicked)
btn2.pack(side = LEFT,expand = True,fill = "both")

btn3 = Button(btnrow1,text = "3",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_3_isclicked)
btn3.pack(side = LEFT,expand = True,fill = "both")

btn4 = Button(btnrow1,text = "+",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_plus_isclicked)
btn4.pack(side = LEFT,expand = True,fill = "both")


#row 2
btn1 = Button(btnrow2,text = "4",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_4_isclicked)
btn1.pack(side = LEFT,expand = True,fill = "both")

btn2 = Button(btnrow2,text = "5",font = ("Digital-7",30),relief = GROOVE,border = 0,command =btn_5_isclicked )
btn2.pack(side = LEFT,expand = True,fill = "both")

btn3 = Button(btnrow2,text = "6",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_6_isclicked)
btn3.pack(side = LEFT,expand = True,fill = "both")

btn4 = Button(btnrow2,text = "-",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_minus_isclicked)
btn4.pack(side = LEFT,expand = True,fill = "both")


#row 3
btn1 = Button(btnrow3,text = "7",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_7_isclicked)
btn1.pack(side = LEFT,expand = True,fill = "both")

btn2 = Button(btnrow3,text = "8",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_8_isclicked)
btn2.pack(side = LEFT,expand = True,fill = "both")

btn3 = Button(btnrow3,text = "9",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_9_isclicked)
btn3.pack(side = LEFT,expand = True,fill = "both")

btn4 = Button(btnrow3,text = "*",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_mult_isclicked)
btn4.pack(side = LEFT,expand = True,fill = "both")


#row 4
btn1 = Button(btnrow4,text = "C",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_c_isclicked)
btn1.pack(side = LEFT,expand = True,fill = "both")

btn2 = Button(btnrow4,text = "0",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_0_isclicked)
btn2.pack(side = LEFT,expand = True,fill = "both")

btn3 = Button(btnrow4,text = "=",font = ("Digital-7",30),relief = GROOVE,border = 0,command = result)
btn3.pack(side = LEFT,expand = True,fill = "both")

btn4 = Button(btnrow4,text = "/",font = ("Digital-7",30),relief = GROOVE,border = 0,command = btn_div_isclicked)
btn4.pack(side = LEFT,expand = True,fill = "both")

root.mainloop()
	
			
		
		
 
	    
	