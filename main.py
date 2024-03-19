from tkinter import *
from tkinter import messagebox, filedialog

class TaskListApp:
    def __init__(self, root, width, height, x, y, title):
        self.root = root
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.title(title)
        self.root.resizable(False, False)
        self.root.config(bg="#F5F5F5")

        self.label_color = "#8D4AEA"
        self.button_color = "#5E35B1"
        self.entry_color = "#FFFFFF"
        self.listbox_color = "#FFFFFF"
        self.select_bg_color = "#EDE7F6"

    def draw_widgets(self):
        self.create_labels()
        self.create_listbox()
        self.create_entry()
        self.create_button_frame()
        self.create_buttons()

    def create_labels(self):
        Label(self.root, text='ToDo List', font=('Arial', 18, 'bold'), bg=self.label_color, fg='white').place(x=250, y=0)
        Label(self.root, text='Tasks:', font=('Arial', 14, 'bold'), bg=self.root.cget("bg")).place(x=10, y=30)
        Label(self.root, text='New Task:', font=('Arial', 14, 'bold'), bg=self.root.cget("bg")).place(x=10, y=340)

    def create_listbox(self):
        self.listbox = Listbox(self.root, width=55, height=14, font=('Arial', 13), bg=self.listbox_color,
                               selectbackground=self.select_bg_color, selectforeground='orange', bd=0, relief='flat')
        self.listbox.place(x=10, y=60)

    def create_entry(self):
        self.entry = Entry(self.root, width=55, font=('Arial', 12), bd=1, bg=self.entry_color, relief='flat')
        self.entry.place(x=10, y=370)
        self.entry.bind('<Return>', self.add_task)

    def create_button_frame(self):
        self.button_frame = Frame(self.root, bg=self.root.cget("bg"), bd=1, relief='solid')
        self.button_frame.place(x=10, y=420, width=580, height=70)

    def create_buttons(self):
        buttons = [
            ("Delete", self.delete_task),
            ("Clear", self.clear_tasks),
            ("Save", self.save_tasks),
            ("Open", self.open_tasks),
            ("Add", self.add_task)
        ]

        for idx, (text, command) in enumerate(buttons):
            Button(self.button_frame, text=text, command=command, bg=self.button_color, fg='white', bd=0,
                   font=('Arial', 12, 'bold'), width=10, relief='flat').grid(row=0, column=idx, padx=10, pady=10)

    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)

    def clear_tasks(self):
        self.listbox.delete(0, END)

    def save_tasks(self):
        tasks = self.listbox.get(0, END)
        with open('saved.txt', 'w') as f:
            for task in tasks:
                f.write(str(task) + '\n')
        messagebox.showinfo('Info', 'Tasks saved successfully.')

    def open_tasks(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                              filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            self.listbox.delete(0, END)
            with open(filename, 'r') as f:
                for line in f:
                    self.listbox.insert(END, line.strip())

if __name__ == '__main__':
    root = Tk()
    app = TaskListApp(root, 600, 500, 390, 100, 'ToDo List')  # Adjusted height and position
    app.draw_widgets()
    root.mainloop()
