from tkinter import *
from currency_converter import CurrencyConverter
tk=Tk()
tk.title("welcome to currency conversion")
tk.geometry("300x200")

lbl1=Label(tk,text="Amount to be converted: ")
lbl1.pack()
inp1=Entry(tk)
inp1.pack()
lbl2=Label(tk,text="Base Currency: ")
lbl2.pack()
inp2=Entry(tk)
inp2.pack()
lbl1=Label(tk,text="Conversion Currency: ")
lbl1.pack()

inp3=Entry(tk)
inp3.pack()

def fun1():
    inp4.delete("0",END)
    a=CurrencyConverter()
    amount=inp1.get()
    to_currency=inp2.get()
    from_currency=inp3.get()
    
    result=a.convert(amount,to_currency,from_currency)
    inp4.insert("0", result)

btn1=Button(tk,text="submit",command=fun1)
btn1.pack()

inp4=Entry(tk)
inp4.pack()

tk.mainloop()












