from tkinter import *
from tkinter import messagebox
def add():
    ab=e.get()
    if ab:
        tlist.insert(END, ab)
        e.delete(0,END)
    else:
         messagebox.showwarning("Warning", "Please enter a task.")

def remove():
    cd= tlist.curselection()
    if cd:
        tlist.delete(cd)
def clear():
    tlist.delete(0, END)
root=Tk()
root.geometry("950x500")
root.title("ToDo List")
root.minsize(400,200)
root.maxsize(600,500)
a=Label(root,text="ToDo List",font="Constantia 25 italic",bg="seagreen",fg="lavender",padx=800,pady=25)
a.pack(pady=5)
ad=Label(root,text="Add Items:",font="cambria 15 bold")
ad.pack()
e=Entry(root,width=38,font="callibri 15 bold",)
e.pack()

b1=Button(root,text="Submit",width="10",bg="palegreen",fg="black",font="cambria 12 bold",command=add)
b1.pack(pady=5)

tlist = Listbox(root, width=50,font="cambria 12 bold")
tlist.pack(pady=5)

remove_button = Button(root, text="Remove Task", width="12",bg="steelblue",fg="black",font="cambria 12 bold",command=remove)
remove_button.pack(side=LEFT,padx=120)

clear_button = Button(root, text="Clear All Tasks",width="15",bg="steelblue",fg="black",font="cambria 12 bold", command=clear)
clear_button.pack(side=LEFT)











root.mainloop()