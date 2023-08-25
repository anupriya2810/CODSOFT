from tkinter import *
import string
import random
import pyperclip
def generate():
    sm=string.ascii_lowercase
    cap=string.ascii_uppercase
    num=string.digits
    spc=string.punctuation
    all=sm+cap+num+spc
    pass_l=int(e2.get())
    x=random.sample(all,pass_l)
    e3.insert(0,x)

def copy():
   user=e1.get()
   pasd=e3.get()
   pyperclip.copy(user)
   pyperclip.copy(pasd)

def reset():
    # s.set=("")
    # e1.update()
    # e3.update()
    e3.delete(0,'end')
    sm=string.ascii_lowercase
    cap=string.ascii_uppercase
    num=string.digits
    spc=string.punctuation
    all=sm+cap+num+spc
    pass_l=int(e2.get())
    x=random.sample(all,pass_l)
    e3.insert(0,x)

def Accept():
    e1.delete(0,'end')
    e3.delete(0,'end')



root=Tk()
root.geometry("600x500")
root.title("Password Generator")
root.minsize(400,500)
root.maxsize(600,500)
ab=IntVar()
s=StringVar
s.set=""
a=Label(root,text="Password Generator",font="Arial 25 bold",fg="green")
a.pack()
name=Label(root,text="Enter User Name:",font="cambria 10 bold")
name.pack(pady=10)
e1=Entry(root,width=30)
e1.pack()
pas=Label(root,text="Enter Password Length:",font="cambria 10 bold")
pas.pack(pady=10)

e2=Spinbox(root,from_=5,to_=12,width=30)
e2.pack(padx=10)

e3=Entry(root,width=20,font="callibri 15 bold",bd=2)
e3.pack(pady=20)

b1=Button(root,text="Generate Password",width="25",bg="green",fg="black",font="cambria 12 bold",command=generate)
b1.pack()

b2=Button(root,text="Copy",fg="black",bg="blue",width="20",font="cambria 12 bold",command=copy)
b2.pack(pady=25)

b3=Button(root,text="Accept",fg="black",width=20,font="cambria 12 bold",command=Accept)
b3.pack(pady=10,side=LEFT,padx=70)
b3=Button(root,text="Reset",fg="black",width=20,font="cambria 12 bold",command=reset)
b3.pack(pady=10,padx=0,side=LEFT)




root.mainloop()