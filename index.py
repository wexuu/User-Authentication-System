from tkinter import *



class LogInApp:
    def __init__(self, root):
            self.root = root
            self.root.geometry("800x500")

            self.createLogInTab()
    def createLogInTab(self):
            self.passEntry = StringVar()
            self.title = Label(self.root, text='Log in',font=(20)).pack(side="top",pady=50)
            self.entry1= Entry(self.root,font=(20)).pack(pady=40)
            self.entry2= Entry(self.root,font=20,show="*",textvariable=self.passEntry).pack()
            self.loginbutton = Button(self.root,text="LOG IN",command=self.GetLogInInfo).pack(pady=10)    
            self.registerbutton = Button(self.root,text="Click here to register!").pack(side="bottom",pady=10)
    

    def GetLogInInfo(self):
        t2 = self.passEntry.get()
        print("hihihihi ", t2)
if __name__ == "__main__":
    root = Tk()
    app = LogInApp(root)
    root.mainloop()