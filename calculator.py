from tkinter import *
import math


def click(event):
    global s
    text=event.widget.cget("text")
    
    if text== "=":
        if s.get().isdigit():
            value=int(s.get())
        else:
            try:
                value=eval(sc.get())
            except Exception as e:
                print(e)
                value="Error"
        
        s.set(value)
        sc.update()
    
    elif text=="C":
        s.set("")
        sc.update()
    
    
    else:
        s.set(s.get() + text)
        sc.update()


root=Tk()
root.geometry("400x500")
root.title("Calcolator")
root.minsize(400,500)
root.maxsize(400,500)

s=StringVar()
s.set("")
sc=Entry(root,textvar=s,font="xenara 25 bold")
sc.pack(fill=X,ipadx=5,pady=5,padx=5)
f=Frame(root,)
b=Button(f,text="C",padx=55,pady=15,font="cambria 10 bold")
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b1=Button(f,text="%",padx=15,pady=15,font="cambria 10 bold")
b1.pack(side=LEFT,padx=15,pady=15)
b1.bind("<Button-1>",click)


b3=Button(f,text=".",padx=15,pady=15,font="cambria 10 bold")
b3.pack(side=LEFT,padx=5,pady=5)
b3.bind("<Button-1>",click)
f.pack()

f=Frame(root,)
b=Button(f,text="7",padx=15,pady=15,font="cambria 10 bold")
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b1=Button(f,text="8",padx=15,pady=15,font="cambria 10 bold")
b1.pack(side=LEFT,padx=15,pady=15)
b1.bind("<Button-1>",click)

b2=Button(f,text="9",padx=15,pady=15,font="cambria 10 bold")
b2.pack(side=LEFT,padx=15,pady=15)
b2.bind("<Button-1>",click)

b3=Button(f,text="*",padx=15,pady=15,font="cambria 10 bold")
b3.pack(side=LEFT,padx=15,pady=15)
b3.bind("<Button-1>",click)
f.pack()


f=Frame(root,)
b=Button(f,text="4",padx=15,pady=15,font="cambria 10 bold")
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b1=Button(f,text="5",padx=15,pady=15,font="cambria 10 bold")
b1.pack(side=LEFT,padx=15,pady=15)
b1.bind("<Button-1>",click)

b2=Button(f,text="6",padx=15,pady=15,font="cambria 10 bold")
b2.pack(side=LEFT,padx=15,pady=15)
b2.bind("<Button-1>",click)

b3=Button(f,text="-",padx=15,pady=15,font="cambria 10 bold")
b3.pack(side=LEFT,padx=15,pady=15)
b3.bind("<Button-1>",click)
f.pack()

f=Frame(root,)
b=Button(f,text="1",padx=15,pady=15,font="cambria 10 bold")
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b1=Button(f,text="2",padx=15,pady=15,font="cambria 10 bold")
b1.pack(side=LEFT,padx=15,pady=15)
b1.bind("<Button-1>",click)

b2=Button(f,text="3",padx=15,pady=15,font="cambria 10 bold")
b2.pack(side=LEFT,padx=15,pady=15)
b2.bind("<Button-1>",click)

b3=Button(f,text="+",padx=15,pady=15,font="cambria 10 bold")
b3.pack(side=LEFT,padx=15,pady=15)
b3.bind("<Button-1>",click)
f.pack()

f=Frame(root,)
b=Button(f,text="00",padx=15,pady=15,font="cambria 8 bold")
b.pack(side=LEFT,padx=15,pady=15)
b.bind("<Button-1>",click)

b1=Button(f,text="0",padx=15,pady=15,font="cambria 10 bold")
b1.pack(side=LEFT,padx=15,pady=15)
b1.bind("<Button-1>",click)

b2=Button(f,text="/",padx=15,pady=15,font="cambria 10 bold")
b2.pack(side=LEFT,padx=15,pady=15)
b2.bind("<Button-1>",click)

b3=Button(f,text="=",padx=15,pady=15,font="cambria 10 bold")
b3.pack(side=LEFT,padx=15,pady=15)
b3.bind("<Button-1>",click)
f.pack()




root.mainloop()

