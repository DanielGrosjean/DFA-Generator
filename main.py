import tkinter
from tkinter import messagebox
from graphviz import Digraph

# Global Variables
MAINBACKGROUND = "#2C2D2D"
transitionEntries = {}

# ------------------------- GUI HELPER FUNCTIONS -------------------------

def createStandardLabel(parent, text, row, column, sticky = "e"):
    label = tkinter.Label(
        parent,
        text = text,
        fg = "white",
        bg = MAINBACKGROUND,
        font = ("Courier New", 10),
        pady = 10
    )
    label.grid(row = row, column = column, sticky = sticky)
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

def createStandardButton(parent, text, command, row, column):
    button = tkinter.Button(
        parent,
        text = text,
        fg = MAINBACKGROUND,
        bg = "white",
        font = ("Courier New", 10),
        command = command,
    )
    button.grid(row = row, column = column, padx = 20, pady = 10)
    return button

# ------------------------- DFA HELPER FUNCTIONS -------------------------

def generateTransitionTable():
    # Clear previous table
    for widget in transitionTableFrame.winfo_children():
        widget.destroy()

    # Get input values
    states = [s.strip() for s in statesInput.get().split(",") if s.strip()]
    alphabet = [a.strip() for a in alphabetInput.get().split(",") if a.strip()]

    # Validate inputs
    if not states or not alphabet:
        messagebox.showwarning(
            title="ERROR",
            message="You must have at least one state and one alphabet character"
        )
        return
    
    # Top-left empty cell
    tkinter.Label(
        transitionTableFrame,
        text="",
        bg=MAINBACKGROUND
    ).grid(row=0, column=0, padx=5, pady=5)

    # Alphabet headers
    for col, symbol in enumerate(alphabet, start=1):
        header = tkinter.Label(
            transitionTableFrame,
            text=symbol,
            bg=MAINBACKGROUND,
            fg="white",
            font=("Courier New", 10, "bold")
        )
        header.grid(row=0, column=col, padx=5, pady=5)

    # State labels and Entry boxes
    for row, state in enumerate(states, start=1):

        # State label on the left
        label = tkinter.Label(
            transitionTableFrame,
            text=state,
            bg=MAINBACKGROUND,
            fg="white",
            font=("Courier New", 10, "bold")
        )
        label.grid(row=row, column=0, padx=5, pady=5)

        # Transition entries
        for col, symbol in enumerate(alphabet, start=1):
            entry = tkinter.Entry(transitionTableFrame, width=8)
            entry.grid(row=row, column=col, padx=5, pady=5)

            transitionEntries[(state, symbol)] = entry

def getTransitions():
    transitions = {}

    # Create all transition pairs from transition table
    for (state, symbol), entry in transitionEntries.items():
        value = entry.get().strip()
        transitions[(state, symbol)] = value

    return transitions

def generateStateDiagram(states, startState, acceptStates, transitions):
    # Initialize format of state diagram
    dot = Digraph(format="png")
    dot.attr(rankdir="LR")

    # Draw States
    for state in states:
        if state in acceptStates:
            dot.node(state, shape="doublecircle")
        else:
            dot.node(state, shape="circle")

    # Draw Start Arrow
    dot.node("", shape="none")
    dot.edge("", startState)

    # Draw Transitions
    for (state, symbol), next_state in transitions.items():
        dot.edge(state, next_state, label=symbol)

    # Save and show state diagram
    dot.render("dfa", view=True)

# ----------------------------- MAIN FUNCTION -----------------------------

def generateDFA():
    # Verify transition table is completed
    if not transitionEntries:
        messagebox.showwarning(
            title="ERROR",
            message="You must generate and fill in the transition table, first"
        )
        return

    # Retrieve inputs
    states = [s.strip() for s in statesInput.get().split(",") if s.strip()]
    startState = startStateInput.get()
    acceptStates = [f.strip() for f in acceptStatesInput.get().split(",") if f.strip()]
    transitions = getTransitions()

    # Verify start state
    if startState not in states:
        messagebox.showwarning(
            title="ERROR",
            message="The start state must be in your list of states"
        )
        return
    
    # Verify accept states
    for state in acceptStates:
        if state not in states:
            messagebox.showwarning(
                title="ERROR",
                message="All of the accept states must be in your list of states"
            )
            return
        
    # Verify DFA status    
    for _ , val in transitions.items():
        if val == "" or val not in states:
            messagebox.showwarning(
                title="ERROR",
                message="All of the entries in the transition table must be filled and be valid"
            )
            return

    generateStateDiagram(states, startState, acceptStates, transitions)

# ---------------------------------- GUI -----------------------------------

# Initializes main application window
window = tkinter.Tk()
window.title("DFA Generator")
window.geometry("700x800")
window.configure(bg = MAINBACKGROUND)

# Initialize Main Frame
frame = createStandardFrame(window)
frame.pack(fill="both", expand=True, padx = 50, pady = 20)
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
subtitleLabel = createStandardLabel(headerFrame, "Separate characters with commas (,)", 1, 0, sticky = "ew")

# Initialize visual Layout
inputsFrame = createStandardFrame(frame)
inputsFrame.grid(row = 1, column = 0, sticky = "ew")
inputsFrame.columnconfigure(1, weight = 1)

statesLabel = createStandardLabel(inputsFrame, "Input List of States (Q)", 0, 0)
statesInput = createStandardEntry(inputsFrame, 0, 1)

alphabetLabel = createStandardLabel(inputsFrame, "Input Alphabet (Σ)", 1, 0)
alphabetInput = createStandardEntry(inputsFrame, 1, 1)

startStateLabel = createStandardLabel(inputsFrame, "Input Start State (q0)", 2, 0)
startStateInput = createStandardEntry(inputsFrame, 2, 1)

acceptStatesLabel = createStandardLabel(inputsFrame, "Input Accept States (F)", 3, 0)
acceptStatesInput = createStandardEntry(inputsFrame, 3, 1)

transitionTableButton = createStandardButton(frame, "Generate Transition Table (δ)", generateTransitionTable, 2, 0)
transitionTableFrame = createStandardFrame(frame)
transitionTableFrame.grid(row = 4, column = 0)

transitionTableButton = createStandardButton(frame, "Generate DFA", generateDFA, 3, 0)

# Main Loop to continously update GUI
window.mainloop()