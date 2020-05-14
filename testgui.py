from tkinter import *
r = Tk() 
r.title('example window')
label = Label(r, text="Hello, press exit! ", fg="black", bg="white")
label.pack()
button = Button(r, text='exit', width=50, command=r.destroy) 
button.pack()

r.mainloop()