__author__ = 'Troshin A. 2019'
from tkinter import *
from tkinter import messagebox

def plus():
    out.delete(0,END)
    out.insert(0,'Ответ: {}'.format(float(text_st.get()) + float(text_nd.get())))
    return
def minus():
    out.delete(0,END)
    out.insert(0,'Ответ: {}'.format(float(text_st.get()) - float(text_nd.get())))
    return
def division():
    try:
        out.delete(0,END)
        out.insert(0,'Ответ: {}'.format(float(text_st.get()) / float(text_nd.get())))
        return
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'На ноль делить нельзя')
        out.insert(0, 'На ноль делить нельзя')
def multiply():
    out.delete(0,END)
    out.insert(0,'Ответ: {}'.format(float(text_st.get()) * float(text_nd.get())))
    return
def clear_():
    text_entry.delete(0, END)
    text_entry2.delete(0, END)
    out.delete(0, END)
    
toolbar = Frame(bd=1)
toolbar.grid(row=2)

b0 = Button(toolbar, text='+', command=plus)
b0.grid(row=2, sticky='e')
b2 = Button(toolbar, text='-', command=minus)
b2.grid(row=2, sticky="e", column=15)
b3 = Button(toolbar, text='/', command=division)
b3.grid(row=2, sticky="e", column=10)
b4 = Button(toolbar, text='*', command=multiply)
b4.grid(row=2, sticky='e', column=5)
clear = Button(toolbar, text='Очистить', command=clear_)
clear.grid(row=2, column=20)

text_st = StringVar()
text_nd = StringVar()
text_entry = Entry(textvariable=text_st)
text_entry.grid(row=0, columnspan=20)
text_entry2 = Entry(textvariable=text_nd)
text_entry2.grid(row=1, columnspan=20)

out = Entry(fg='green')
out.grid(row=3)
mainloop()