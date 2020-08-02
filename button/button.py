from tkinter import *
root = Tk()
root.geometry("500x500")
def something():
    print("Button Successful")

b = Button(text="Click me", command=something)
b.pack()
root.mainloop
