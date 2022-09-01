import tkinter
from tkinter import ttk
window=tkinter.Tk()
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
list=['Python','C++','Java','Javascript']
list_items=tkinter.StringVar(value=list)
list_items=tkinter.Listbox(window,height=10,width=10,listvariable=list_items)
list_items.grid(column=0,row=0,sticky=tkinter.W)
label1=tkinter.Label(window,text="Lenguajes de programación",bg="blue",fg="white")
label1.grid(column=3,row=0,sticky=tkinter.N,padx=10,pady=10)







window.mainloop()