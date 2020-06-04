import tkinter as tk
import main_window
import mongo_con
from PIL import ImageTk, Image

window = None



class Login(object):

    def __init__(self, master=None, width=300, height=300, title="Login Page"):
        self.master = master
        self.width = width
        self.height = height
        self.title = title
        self.access = False
        self.skip = True

        if not self.skip:
            self.master.title(title)
            self.center_window()

        self.frame = tk.Frame(self.master, bg="#3B444B")

        # self.img = ImageTk.PhotoImage(Image.open("assets/cbg.jpg"))
        # self.panel = tk.Label(self.master, image=self.img)

        self.login_label = tk.Label(self.frame, text="Login Page", anchor='ne')
        self.user_message = tk.Message(self.frame, text=None, bg="#3B444B", width=200)

        self.login_button = tk.Button(self.frame, text="Login", anchor='s', command=self.login)
        self.register_button = tk.Button(self.frame, text="Register", anchor='s', command=self.register_button)

        self.username_entry = tk.Entry(self.frame, text="Username...", width=25)
        self.password_entry = tk.Entry(self.frame, text="Password...", width=25)

        self.password_entry.bind("<Return>", self.login)
        self.username_entry.bind("<Return>", self.login)
        self.username_entry.focus_set()

    def init_login(self):
        self.frame.place(relwidth=1.0, relheight=1.0)
        self.login_label.pack(pady=20)
        self.place_entry_boxes()
        self.place_login_buttons()
        self.user_message.place(relx=0.5, rely=0.9, anchor='c')

        self.master.mainloop()

    @staticmethod
    def create_window():
        global window

        window = main_window.Window(720, 720, "Ruby")
        window.init_widgets()

    def place_login_buttons(self):
        self.login_button.pack(pady=5)
        self.register_button.pack(pady=5)

    def place_entry_boxes(self):
        self.username_entry.pack(pady=5)
        self.password_entry.pack(pady=5)


    def center_window(self):
        w = self.width
        h = self.height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def register_button(self):
        u = mongo_con.create_user(self.username_entry.get().strip(), "black@gmail.com",
                                  self.password_entry.get().strip())
        if u is not None:
            self.user_message.config(
                text="User {0} created with password {1}".format(self.username_entry.get(), self.password_entry.get()))

    def login(self, event=None):
        if (len(self.username_entry.get()) and len(self.password_entry.get())) == 0:
            print("Please enter username and password")
        elif self.skip_login():
            self.master.destroy()
            self.create_window()
        elif mongo_con.check_user(self.username_entry.get().strip(), self.password_entry.get().strip()) is not None:
            self.access = True

            print("Logging in under", self.username_entry.get(), "with password:", self.password_entry.get())

            self.master.destroy()
            self.create_window()
            return
        else:
            self.user_message.config(text="Username or password was incorrect.", fg='black')
            self.username_entry.focus_set()
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def skip_login(self):
        self.skip = True

