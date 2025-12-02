import tkinter

# Constant variables
BCKGRND = "#2C2D2D"

# Initializes main application window
window = tkinter.Tk()
window.title("DFA Generator")
window.geometry("600x400")
window.configure(bg = BCKGRND)

# Initialize Main Frame
frame = tkinter.Frame(
    window,
    bg = BCKGRND
)

frame.pack()

# Initialize Header
headerFrame = tkinter.Frame(
    frame, 
    bg = BCKGRND
)

titleLabel = tkinter.Label(
    headerFrame, 
    text = "DFA GENERATOR", 
    fg = "white", 
    bg = BCKGRND, 
    font = ("Courier New", 20, "bold"),
    pady = 10
)

subtitleLabel = tkinter.Label(
    headerFrame,
    text = "Separate characters with commas (,)",
    fg = "white",
    bg = BCKGRND,
    font = ("Courier New", 10)
)

headerFrame.grid(row = 0, column = 0)
titleLabel.grid(row = 0, column = 0)
subtitleLabel.grid(row = 1, column = 0)

# Initialize Formal Inputs Section
inputsFrame = tkinter.Frame(
    frame,
    bg = BCKGRND
)

statesLabel = tkinter.Label(
    inputsFrame,
    text = "Input List of States",
    fg = "white",
    bg = BCKGRND,
    font = ("Courier New", 10),
    pady = 10
)

statesInput = tkinter.Entry(inputsFrame)

alphabetLabel = tkinter.Label(
    inputsFrame,
    text = "Input Alphabet",
    fg = "white",
    bg = BCKGRND,
    font = ("Courier New", 10),
    pady = 10
)

alphabetInput = tkinter.Entry(inputsFrame)

startStateLabel = tkinter.Label(
    inputsFrame,
    text = "Input Start State",
    fg = "white",
    bg = BCKGRND,
    font = ("Courier New", 10),
    pady = 10
)

startStateInput = tkinter.Entry(inputsFrame)

inputsFrame.grid(row = 1, column = 0)
statesLabel.grid(row = 0, column = 0)
statesInput.grid(row = 0, column = 1)
alphabetLabel.grid(row = 1, column = 0)
alphabetInput.grid(row = 1, column = 1)
startStateLabel.grid(row = 1, column = 2)
startStateInput.grid(row = 1, column = 3)

window.mainloop()