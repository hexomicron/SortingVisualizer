from tkinter import *
from tkinter import ttk

# We need to create a random array.
import random

# Importing colors 
from colors import *

# Creating a basic window
window = Tk()
window.title("Sorting Algorithm Visualizer")
window.maxsize(1000, 700)
window.config(bg = WHITE) # Essential for dark mode users.

algorithm_name = StringVar()
algo_list = ['Bubble Sort']

# speed
speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

# Random values aka sample data
data = []

# draw the data on the canvas
def drawData(data, colorArray):
    pass

# generate array with random values
def generate():
    pass

# set sorting speed
def set_speed():
    pass

# trigger the selected algorithm and start sorting
def sort():
    pass


# UI here
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select algorithm
l1  = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# sort button
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

# button for generating array
b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=1, padx=5, pady=5)

# canvas to draw the array
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()
