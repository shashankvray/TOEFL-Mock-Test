from tkinter import *
from speak import Speaking
window = Tk()
window.title("TOEFL Mock Test")
window.geometry("400x300+300+200")

def startTest():
    pass

def saveProgress():
    pass


# Label
lbl = Label(window, text = "Choose the section(s) for your test", font=("Helvetica", 10))
lbl.place(x=30, y=28)

# Start Test Button
btns = Button(window, text = "Start TEST", fg = 'black', command = startTest)
btns.place(relx=0.25, rely=0.8, anchor = CENTER)
# btns.bind('<Button-1>', startTest)

# Save Results Button
btnv = Button(window, text = "Save my Results", fg = 'black', command = saveProgress)
btnv.place(relx=0.5, rely=0.8, anchor = CENTER)

# End Test Button
btne = Button(window, text = "Close TEST", fg = 'black', command = window.destroy)
btne.place(relx=0.75, rely=0.8, anchor = CENTER)

# Checkbox
spk = IntVar()
lis = IntVar()
C1 = Checkbutton(window, text = "Speaking", variable = spk)
C2 = Checkbutton(window, text = "Listening", variable = lis)
C1.place(x=40, y=50)
C2.place(x=40, y=70)

# Text Box for questions
# T = Text(window, height = 6, width = 53) 

window.mainloop()