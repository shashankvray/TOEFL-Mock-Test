from tkinter import *
from speak import Speaking
from write import Writing

class MainWindow:
    def startTest(self):
        if not self.spk and not self.lis:
            lblz = Label(window, text = "Select at least one section", font=("Helvetica", 10))
            lblz.place(relx=.3, rely=0.7, anchor = CENTER)

    def saveProgress(self, event):
        pass

    def __init__(self):
        window = Tk()
        window.title("TOEFL Mock Test")
        window.geometry("400x300+300+200")
        
        # Section choice Label
        lblx = Label(window, text = "Choose the section(s) for your test", font=("Helvetica", 10))
        lblx.place(x=30, y=28)

        # Checkbox
        self.spk = IntVar()
        self.lis = IntVar()
        C1 = Checkbutton(window, text = "Speaking", variable = self.spk)
        C2 = Checkbutton(window, text = "Listening", variable = self.lis)
        C1.place(x=40, y=50)
        C2.place(x=40, y=70)

        # Note Label
        lbly = Label(window, text = "Note: Cannot save your results after closing", fg = 'red', font = ("Helvetica", 9))
        lbly.place(relx=.3, rely=0.95, anchor = CENTER)

        # Start Test Button
        btns = Button(window, text = "Start TEST", fg = 'black', command = self.startTest)
        btns.place(relx=0.35, rely=0.8, anchor = CENTER)
        #          relx=0.25, rely=0.8

        # End Test Button
        btne = Button(window, text = "Close TEST", fg = 'black', command = window.destroy)
        btne.place(relx=0.65, rely=0.8, anchor = CENTER)
        #          relx=0.75, rely=0.8


        '''
        # Save Results Button
        btnv = Button(window, text = "Save my Results", fg = 'black', command = saveProgress)
        btnv.place(relx=0.5, rely=0.8, anchor = CENTER)

        # Multi Line Text Box
        # T = Text(window, height = 6, width = 30) 
        # T.place(x=40, y=100)
        '''
        
        window.mainloop()


if __name__ == '__main__':
    Obj = MainWindow()
    