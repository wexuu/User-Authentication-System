import tkinter as tk

class App:
    def __init__(self, root=None,app=None):
        self.root = root
        self.root.geometry("800x500")
        self.app = app
        self.top_frame = tk.Frame(self.root, width=800, height=450)
        self.top_frame.pack(fill='both', expand=True)

        self.bottom_frame = tk.Frame(self.root, width=800, height=50)
        self.bottom_frame.pack(fill='x')

        self.loginButton = tk.Button(self.bottom_frame, text="Log in", command=self.make_page_login).pack(side='right', padx=5, pady=5)
        self.registerButton = tk.Button(self.bottom_frame, text="Register here", command=self.make_page_register).pack(side='left', padx=5, pady=5)

        self.page_1 = Page_Login(master=self.top_frame, app=self)
        self.page_2 = Page_Register(master=self.top_frame, app=self)

        self.main_page()

    def main_page(self):
        for widget in self.top_frame.winfo_children():
            widget.pack_forget()
        tk.Label(self.top_frame, text='User Authentication System').pack()

    def make_page_login(self):
        for widget in self.top_frame.winfo_children():
            widget.pack_forget()
        for widget in self.bottom_frame.winfo_children():
            if(widget.cget('text') == 'Log in'):
                widget.pack_forget()
        self.page_1.start_page()

    def make_page_register(self):
        for widget in self.top_frame.winfo_children():
            widget.pack_forget()
        for widget in self.bottom_frame.winfo_children():
            if(widget.cget('text') == 'Log in')or (widget.cget('text') == 'Go back'):
                widget.pack_forget()
        self.page_2.start_page()

class Page_Login:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Passed a log in check!').pack()

    def start_page(self):
        tk.Button(self.app.bottom_frame, text='Go back', command=self.go_back).pack(side='right', padx=5, pady=5)
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page() 

        #Clear the goback button and replace it with a login one
        for widget in self.app.bottom_frame.winfo_children():
            if(widget.cget('text') == 'Go back'):
                widget.pack_forget()
        self.loginButton = tk.Button(self.app.bottom_frame, text="Log in", command=self.app.make_page_login).pack(side='right', padx=5, pady=5)

    

class Page_Register:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Register here').pack()
        
        self.textbox = tk.Entry(self.frame, bg="white", width=50, borderwidth=2)
        self.textbox.insert(0, 'Enter your name here')
        self.textbox.pack(pady=20)
        self.textbox.bind("<FocusIn>", self.placeholders)

        self.textbox1 = tk.Entry(self.frame, bg="white", width=50, borderwidth=2)
        self.textbox1.insert(0, 'Enter your password here')
        self.textbox1.pack(pady=20)
        self.textbox1.bind("<FocusIn>", self.placeholders1)

        self.textbox2 = tk.Entry(self.frame, bg="white", width=50, borderwidth=2)
        self.textbox2.insert(0, 'Enter your password again')
        self.textbox2.pack(pady=20)
        self.textbox2.bind("<FocusIn>", self.placeholders2)

    def placeholders(self,l):
        self.textbox.delete(0, 'end')
    def placeholders1(self,l):
        self.textbox1.delete(0, 'end')
    def placeholders2(self,l):
        self.textbox2.delete(0, 'end')

    def start_page(self):
        tk.Button(self.app.bottom_frame, text='Go back', command=self.go_back).pack(side='right', padx=5, pady=5)
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

        #Clear the goback button and replace it with a login one
        for widget in self.app.bottom_frame.winfo_children():
            if(widget.cget('text') == 'Go back'):
                widget.pack_forget()
        self.loginButton = tk.Button(self.app.bottom_frame, text="Log in", command=self.app.make_page_login).pack(side='right', padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()