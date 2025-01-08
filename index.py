import tkinter as tk


class App:
    def __init__(self, root=None):

        self.root = root
        self.root.geometry("800x500")
        self.frame = tk.Frame(self.root,width=800,height=500)
        self.frame.pack()

        self.frame1 = tk.Frame(self.root, relief='raised', borderwidth=1).pack(fill='both', expand=True)
        loginButton = tk.Button(self.root, text="Log in",command=self.make_page_login).pack(side='right', padx=5, pady=5)
        registerButton = tk.Button(self.root,text=("Register here"),command=self.make_page_register).pack(side='left',padx=5,pady=5)

        tk.Label(self.frame, text='Log in').pack()
        self.page_1 = Page_Login(master=self.root, app=self)
        self.page_2 = Page_Register(master=self.root, app=self)
    def main_page(self):
        self.frame.pack()

    def make_page_login(self):
        self.frame.pack_forget()
        self.page_1.start_page()

    def make_page_register(self):
        self.frame.pack_forget()
        self.page_2.start_page()

class Page_Login:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Page 1').pack()
        tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page(self)

class Page_Register:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Page 2').pack()
        tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()