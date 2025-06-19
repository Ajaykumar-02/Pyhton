from tkinter import*
import tkinter as tk


a=tk.Tk()
a.title("Simple Calculator")
# a.geometry("400x600+10+9")

def clear():
    entry.delete(0,END)
    

entry = tk.Entry(a, font=("Arial", 20), bd=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=2, pady=2)
def numb(x):
    value = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(value)+str(x))


def add():
    global add
    add=entry.get()
    entry.delete(0,END)
    global oper
    oper ="+"

def sub():
    global sub
    sub=entry.get()
    entry.delete(0,END)
    global oper
    oper ="-"
def multi():
    global multi
    multi=entry.get()
    entry.delete(0,END)
    global oper
    oper ="x"
def div():
    global div
    div=entry.get()
    entry.delete(0,END)
    global oper
    oper ="/"
def per():
    global per
    per=entry.get()
    entry.delete(0,END)
    global oper
    oper ="%"
def bre():
    global bre
    bre=entry.get()
    entry.delete(0,END)
    global oper
    oper ="()"
def dot():
    global dot
    dot=entry.get()
    entry.delete(0,END)
    global oper
    oper ="."
def equal():
    second_num = float(entry.get())
    entry.delete(0, END)
    if oper == "+":
        entry.insert(0,int (add) + int(second_num))
    elif oper == "-":
        entry.insert(0, int(sub) - int(second_num))
    elif oper == "x":
        entry.insert(0, int(multi) * int (second_num))
    elif oper == "/":
        if second_num != 0:
            entry.insert(0,int (div) / int (second_num))
        else:
            entry.insert(0, "Error")
    elif oper == "%":
        entry.insert(0, int(per)% second_num)
   
b =tk.Button(a,text="C",font=20,height=2,width=5 , command=clear).grid(row=1,column=0)
c=tk.Button(a,text="()",font=20,height=2,width=5,command=bre).grid(row=1,column=1)
d=tk.Button(a,text="%",font=20,height=2,width=5,command=per).grid(row=1,column=2)
e=tk.Button(a,text="/",font=20,height=2,width=5,command= div).grid(row=1,column=3)

f=tk.Button(a,text="7",font=20,height=2,width=5,command=lambda:numb("7")).grid(row=2,column=0)
g=tk.Button(a,text="8",font=20,height=2,width=5,command=lambda:numb("8")).grid(row=2,column=1)
h=tk.Button(a,text="9",font=20,height=2,width=5,command=lambda:numb("9")).grid(row=2,column=2)
i=tk.Button(a,text="x",font=20,height=2,width=5 , command=multi).grid(row=2,column=3)

j=tk.Button(a,text="4",font=20,height=2,width=5,command=lambda:numb("4")).grid(row=3,column=0)
k=tk.Button(a,text="5",font=20,height=2,width=5,command=lambda:numb("5")).grid(row=3,column=1)
l=tk.Button(a,text="6",font=20,height=2,width=5,command=lambda:numb("6")).grid(row=3,column=2)
m=tk.Button(a,text="-",font=20,height=2,width=5 , command=sub).grid(row=3,column=3)


r=tk.Button(a,text="1",font=20,height=2,width=5,command=lambda:numb("1")).grid(row=4,column=0)
s=tk.Button(a,text="2",font=20,height=2,width=5,command=lambda:numb("2")).grid(row=4,column=1)
t=tk.Button(a,text="3",font=20,height=2,width=5,command=lambda:numb("3")).grid(row=4,column=2)
u=tk.Button(a,text="+",font=20,height=2,width=5,command=add).grid(row=4,column=3)

v=tk.Button(a,text="00",font=20,height=2,width=5,command=lambda:numb("00")).grid(row=5,column=0)
w=tk.Button(a,text="0",font=20,height=2,width=5,command=lambda:numb("0")).grid(row=5,column=1)
y=tk.Button(a,text=".",font=20,height=2,width=5,command=lambda:numb(".")).grid(row=5,column=2)
z=tk.Button(a,text="=",font=20,height=2,width=5,command=equal ).grid(row=5,column=3)





a.mainloop()