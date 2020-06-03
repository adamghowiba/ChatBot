import tkinter as tk
import randomeat

# TODO Create enter submit
# fix UI Deisgn
# TODO Add users tab


class Window(object):

    def __init__(self, width=700, height=700, title="GUI"):
        self.window = tk.Tk()
        self.width = width
        self.height = height
        self.title = title
        self.location = 0
        self.tvv = 0

        self.window.title(title)
        self.center_window()

        self.frame = tk.Frame(self.window, bg="#3B444B")
        self.chat_conversations = tk.Frame(self.frame, bg="white", width=200)
        self.chat_section = tk.Text(self.frame, bg='yellow')

        self.text_box = tk.Text(self.frame, width=self.width, height=3, bg='white')

        self.button = tk.Button(self.frame, text='Button', width=5, height=3, command=self.send_message)

        self.label = None

        self.text_box.bind("<Return>", self.send_message)
        self.text_box.focus_set()

    def init_widgets(self):
        self.frame.place(relheight=1.0, relwidth=1.0)
        self.create_text_box()
        self.create_submit()
        self.create_chats_section()

        self.window.mainloop()

    def create_chats_section(self):
        self.chat_conversations.pack(fill=tk.BOTH, side="left")
        self.chat_section.place(x=self.chat_conversations.winfo_reqwidth(), relwidth=1.0, relheight=0.926)

    def create_text_box(self):
        self.text_box.place(y=(self.height - self.text_box.winfo_reqheight()))

    def create_submit(self):
        self.button.place(y=self.height - self.button.winfo_reqheight(), x=self.width - self.button.winfo_reqwidth())

    def get_textbox(self):
        return self.text_box

    def center_window(self):
        w = self.width
        h = self.height
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Commands ----- #

    def send_message(self, event=None):
        self.tvv += 1
        # self.label = tk.Text(self.chat_section,
        #                      width=self.frame.winfo_width() - self.user_chats.winfo_width(), height=3,
        #                      fg='blue', bg="green")
        self.chat_section.insert(0.0, self.text_box.get(0.0, tk.END))
        randomeat.pick_random_place()
        # self.location += self.label.winfo_reqheight()
        # self.label.grid(column=0, row=self.tvv)
        # self.window.update()
        # self.label.place(
        #     y=self.frame.winfo_height() - self.label.winfo_height() - self.text_box.winfo_height() - self.location)

        self.text_box.delete(0.0, tk.END)
        # self.text_box.place()
