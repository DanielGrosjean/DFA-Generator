import tkinter

# Constant variables
MAINBACKGROUND = "#2C2D2D"

# Helper Functions
def createStandardLabel(parent, text, row, column):
    label = tkinter.Label(
        parent,
        text = text,
        fg = "white",
        bg = MAINBACKGROUND,
        font = ("Courier New", 10),
        pady = 10
    )
    label.grid(row = row, column = column, sticky = "w")
    return label

def createStandardEntry(parent, row, column):
    entry = tkinter.Entry(parent)
    entry.grid(row = row, column = column, sticky = "ew", padx = 10)
    return entry

def createStandardFrame(parent):
    frame = tkinter.Frame(
        parent,
        bg = MAINBACKGROUND
    )
    return frame

# Initializes main application window
window = tkinter.Tk()
window.title("DFA Generator")
window.geometry("600x400")
window.configure(bg = MAINBACKGROUND)

# Initialize Main Frame
frame = createStandardFrame(window)
frame.pack(fill="both", expand=True)
frame.columnconfigure(0, weight=1)

# Initialize Header
headerFrame = createStandardFrame(frame)

titleLabel = tkinter.Label(
    headerFrame, 
    text = "DFA GENERATOR", 
    fg = "white", 
    bg = MAINBACKGROUND, 
    font = ("Courier New", 20, "bold"),
    pady = 5
)

headerFrame.grid(row = 0, column = 0)
titleLabel.grid(row = 0, column = 0)
subtitleLabel = createStandardLabel(headerFrame, "Separate characters with commas (,)", 1, 0)

# Initialize Formal Inputs Section
inputsFrame = createStandardFrame(frame)

inputsFrame.grid(row = 1, column = 0, sticky = "ew")
inputsFrame.columnconfigure(1, weight = 1)

statesLabel = createStandardLabel(inputsFrame, "Input List of States", 0, 0)
statesInput = createStandardEntry(inputsFrame, 0, 1)

alphabetLabel = createStandardLabel(inputsFrame, "Input Alphabet", 1, 0)
alphabetInput = createStandardEntry(inputsFrame, 1, 1)

startStateLabel = createStandardLabel(inputsFrame, "Input Start State", 2, 0)
startStateInput = createStandardEntry(inputsFrame, 2, 1)

acceptStatesLabel = createStandardLabel(inputsFrame, "Input Accept States", 3, 0)
acceptStatesEntry = createStandardEntry(inputsFrame, 3, 1)

window.mainloop()