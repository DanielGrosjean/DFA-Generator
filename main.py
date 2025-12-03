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

# Initializes main application window
window = tkinter.Tk()
window.title("DFA Generator")
window.geometry("600x400")
window.configure(bg = MAINBACKGROUND)

# Initialize Main Frame
frame = tkinter.Frame(
    window,
    bg = MAINBACKGROUND
)

frame.pack(fill="both", expand=True)
frame.columnconfigure(0, weight=1)

# Initialize Header
headerFrame = tkinter.Frame(
    frame, 
    bg = MAINBACKGROUND
)

titleLabel = tkinter.Label(
    headerFrame, 
    text = "DFA GENERATOR", 
    fg = "white", 
    bg = MAINBACKGROUND, 
    font = ("Courier New", 20, "bold"),
    pady = 4
)

subtitleLabel = tkinter.Label(
    headerFrame,
    text = "Separate characters with commas (,)",
    fg = "white",
    bg = MAINBACKGROUND,
    font = ("Courier New", 10)
)

headerFrame.grid(row = 0, column = 0)
titleLabel.grid(row = 0, column = 0)
subtitleLabel.grid(row = 1, column = 0)

# Initialize Formal Inputs Section
inputsFrame = tkinter.Frame(
    frame,
    bg = MAINBACKGROUND
)

statesInput = tkinter.Entry(inputsFrame)

alphabetInput = tkinter.Entry(inputsFrame)

startStateInput = tkinter.Entry(inputsFrame)

inputsFrame.grid(row = 1, column = 0, sticky = "ew")
inputsFrame.columnconfigure(1, weight = 1)

statesLabel = createStandardLabel(inputsFrame, "Input List of States", 0, 0)
statesInput.grid(row = 0, column = 1, sticky = "ew", padx = 10)

alphabetLabel = createStandardLabel(inputsFrame, "Input Alphabet", 1, 0)
alphabetInput.grid(row = 1, column = 1, sticky="ew", padx=10)

startStateLabel = createStandardLabel(inputsFrame, "Input Start State", 2, 0)
startStateInput.grid(row = 2, column = 1, sticky="ew", padx=10)

window.mainloop()