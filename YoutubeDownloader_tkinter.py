import tkinter as tk
from pytube import YouTube
root=tk.Tk()
root.title("python")
root.geometry("400x300")
link= tk.StringVar()
lb1=tk.Label(root,text="url :")
lb1.pack()
entry=tk.Entry(root,width=50,textvariable=link)
entry.pack()
def python():
    a=YouTube(str(link.get()))
    video= a.streams.first()
    video.download()
    b=tk.Label(root,text="sucessfully downloaded")
    b.pack()


bt1=tk.Button(root,text="click for download",command=python)
bt1.pack()
root.mainloop()
