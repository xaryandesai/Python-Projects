import tkinter as tk

t = tk.Tk()
t.title('Leap Year Checker')
t.geometry("300x300")

first_label = tk.Frame(t, height=300, width=150)
first_label.pack(expand=True, fill=tk.BOTH)
entry = tk.Text(first_label, width=15, height=1)
entry.place(x=25, y=37)

def leap_year():
    leap_year_check = int(entry.get("1.0",'end'))
    try:
        if (leap_year_check % 400 == 0) or (leap_year_check % 4 == 0 and leap_year_check%100!=0):
                final.delete("1.0", 'end')
                final.insert("1.0", f'{leap_year_check} ''is a leap year!')
        else:
                final.delete("1.0", 'end')
                final.insert("1.0", f'{leap_year_check} is not a leap year!')
    except :
        final.insert("1.0")
        
button = tk.Button(first_label, text='enter',command=leap_year)
button.place(x=150, y=30)
final = tk.Text(first_label, width=35, height=10, wrap='word')
final.place(x=20, y=85)

t.mainloop()
