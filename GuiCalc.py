from tkinter import *
import re
equation=''
prev=0
root=Tk()
root.geometry('1000x1000')
root.title("calculator")
f1=Frame(root,bg="grey",height=500,borderwidth=8,relief=SUNKEN,padx=80,pady=100)
f1.grid(padx=70,pady=70)
l1=Label(f1,text="SIMPLE CALCULATOR",height="5",width="25",borderwidth=5,relief=RIDGE,font="lucida 20 bold")
l1.grid(row=0,column=1,pady=10)

def enter(n):
    global equation
    equation+=str(n)
    s1.set(equation)
    e1.update()
def clear():
    global equation
    equation=''
    s1.set(equation)
def result():
    global prev
    global equation
    if equation=="" or equation[0]=="/" or equation[0]=="*" or equation[0]=="+" or equation[0]=="-" :
       Button(f1,text="Click to continue",font="lucida 15 bold",command=quit() ).grid(row=0,column=1,pady=10)
    equation=re.sub(r'\b0+(\d)', r'\1', equation)
    print(equation)
    prev=eval(equation)
    equation=str(prev)
    s1.set(prev)

s1=StringVar()
s1.set("")
e1=Entry(f1,textvariable=s1,width="30",font="montserat 15 bold")
e1.grid(row=2,column=1,padx=10,pady=20)
b1=Button(f1,text="9",command=lambda :enter(9),height=2,width=10,font="lucida 15 bold")
b1.grid(row=5,column=0)
b2=Button(f1,text="8",command=lambda :enter(8),height=2,width=10,font="lucida 15 bold")
b2.grid(row=5,column=1)
b3=Button(f1,text="7",command=lambda :enter(7),height=2,width=10,font="lucida 15 bold")
b3.grid(row=5,column=2)
b11=Button(f1,text="*",command=lambda :enter('*'),height=2,width=10,font="lucida 15 bold")
b11.grid(row=11,column=0,pady=20)
b4=Button(f1,text="6",command=lambda :enter(6),height=2,width=10,font="lucida 15 bold")
b4.grid(row=6,column=0)
b5=Button(f1,text="5",command=lambda :enter(5),height=2,width=10,font="lucida 15 bold")
b5.grid(row=6,column=1)
b6=Button(f1,text="4",command=lambda :enter(4),height=2,width=10,font="lucida 15 bold")
b6.grid(row=6,column=2)
b12=Button(f1,text="/",command=lambda :enter('/'),height=2,width=10,font="lucida 15 bold")
b12.grid(row=11,column=1)
b7=Button(f1,text="3",command=lambda :enter(3),height=2,width=10,font="lucida 15 bold")
b7.grid(row=7,column=0)
b8=Button(f1,text="2",command=lambda :enter(2),height=2,width=10,font="lucida 15 bold")
b8.grid(row=7,column=1)
b9=Button(f1,text="1",command=lambda :enter(1),height=2,width=10,font="lucida 15 bold")
b9.grid(row=7,column=2)
b13=Button(f1,text="+",command=lambda :enter('+'),height=2,width=10,font="lucida 15 bold")
b13.grid(row=11,column=2)
b10=Button(f1,text="0",command=lambda :enter(0),height=2,width=10,font="lucida 15 bold")
b10.grid(row=8,column=2)
b3=Button(f1,text="-",command=lambda :enter('-'),height=2,width=10,font="lucida 15 bold")
b3.grid(row=12,column=0)
b3=Button(f1,text=".",command=lambda :enter('.'),height=2,width=10,font="lucida 15 bold")
b3.grid(row=8,column=0)
b11=Button(f1,text="=",command=result,height=2,width=10,font="lucida 15 bold")
b11.grid(row=12,column=2)
b14=Button(f1,text="CLEAR",command=lambda :clear(),height=2,width=10,font="lucida 15 bold")
b14.grid(row=12,column=1)
root.mainloop()