from tkinter import *
from time import strftime

def update_time():
    time = strftime('%I:%M:%S %p') # Format: HH:MM:SS AM/PM
    lbl.config(text = time)
    lbl.after(1000, update_time) # Update every 1 second (1000 milliseconds)


root = Tk()
root.title("Digital clock")

color1 = "#f8aaf6"
color2 = "#970c93"

lbl = Label(root, font=('Times New Roman',50, 'bold'), bg = color1, fg = color2)
lbl.pack(padx=20, pady=20) # Set padding around the label widget

update_time() # Start the clock

root.mainloop()
