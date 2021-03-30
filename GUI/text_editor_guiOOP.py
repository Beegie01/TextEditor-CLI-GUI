from tkinter import Tk, messagebox, Frame, Menu, scrolledtext, filedialog, Label
import os

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.text_frame = Frame(master=master)
        self.text_frame.rowconfigure(0, weight=1)
        self.text_frame.columnconfigure(0, weight=1)
        self.text_frame.grid(rowspan=5, columnspan=4, sticky='nsew')
        self.status_frame = Frame(master=master, bg='blue')
        self.status_frame.rowconfigure(0, weight=1)
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.grid(row=5, columnspan=4, sticky='ew')
        self.filename = None
        self.menu_bar = Menu(master, tearoff=0)
        self.master.config(menu=self.menu_bar,)
        self.text_field = scrolledtext.ScrolledText(master=self.text_frame, bg='black', fg='white',
                                                    font=['Times New Roman', 12])
        self.file_loc_stat = None
        self.file_status = Label(master=self.status_frame, fg='white', bg='blue')
        self.file_status.grid(row=0, column=0, sticky='we')

    def read_file(self):
        self.filename = filedialog.askopenfilename(defaultextension='*.txt', initialdir=os.getcwd(),
                               filetypes=[("TXT FILES", '*.txt'), ('CSV Files', '*.csv'), ('ALL FIILES', '*.*')])
        with open(self.filename, 'r+', encoding='utf8') as hand:
            tx = hand.readlines()
        txt = ''.join(tx)
        self.text_field.delete(index1='1.0', index2='end')
        self.text_field.insert(index='end', chars=txt)
        self.text_field.grid(sticky='nsew')
        self.update_fileloc()
        self.update_filestatus()

    def update_fileloc(self):
        self.file_loc_stat = Label(master=self.status_frame, text=f"File Name: {self.filename}", fg='white', bg='blue')
        self.file_loc_stat.grid(row=0, column=5, sticky='ew')

    def update_filestatus(self):
        # textfield is empty
        if ([True for ele in [None, '', ' '] if self.filename == ele]) and (len(self.text_field.get(index1='1.0', index2='end')) < 2):
            self.file_status = Label(master=self.status_frame, text=f"Unsaved File!!!", bg='RED', fg='WHITE')
            self.file_status.grid(row=0, column=0, sticky='we')

        else:
            self.file_status = Label(master=self.status_frame, text=f"Existing File", bg='green', fg='WHITE')
            self.file_status.grid(row=0, column=0, sticky='we')

    def setup_menu(self):
        menu = Menu(self.menu_bar, tearoff=0)
        menu.add_command(label='New Window', command=self.new_window)
        menu.add_command(label='Create New', command=self.create)
        menu.add_command(label='Open File', command=self.read_file)
        menu.add_command(label='Save', command=self.save_text)
        menu.add_command(label='Save As', command=self.save_as)
        self.menu_bar.add_cascade(menu=menu, label='File')
        self.menu_bar.add_command(label='Exit', command=self.master.destroy)

    def new_window(self):
        pass

    def create(self):
        if messagebox.askquestion(message='Do You Want To Create A New Text File?') == 'yes':
            self.filename = None
            self.text_field.delete(index1='1.0', index2='end')
            self.text_field.grid(sticky='nsew')
            self.update_filestatus()
            self.update_fileloc()


    def save_as(self):
        self.filename = filedialog.asksaveasfilename(defaultextension='*.txt', initialdir=os.getcwd(),
                                                     filetypes=[('TXT FILE', '*.txt'), ('CSV FILE', '*.csv'), ('PYTHON FILE', '*.py')])
        with open(self.filename, 'w+', encoding='utf8') as hand:
            hand.writelines(self.text_field.get(index1='1.0', index2='end'))
        self.update_filestatus()
        self.update_fileloc()

    def save_text(self):
        if self.filename is None:
            messagebox.showerror(message='No File Has Been Selected!!')
            if not (messagebox.askyesnocancel(title='SaveorNot', message='Create an Empty file?')):
                return None
            self.filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                                         defaultextension='.txt', filetypes=[('txt files', '*.txt'), ('All Files', '*.*')])

        with open(self.filename, 'w+', encoding='utf8') as hand:
            hand.writelines(self.text_field.get(index1='1.0', index2='end'))
        self.update_fileloc()
        self.update_filestatus()


win1 = Tk()
win1.title("Text Editor")
tx = TextEditor(win1)
tx.setup_menu()

sw, sh = win1.winfo_screenwidth(), win1.winfo_screenheight()
win1.rowconfigure(index=0, weight=1)
win1.columnconfigure(index=0, weight=1)

aw, ah = int(sw*.4), int(sh*.6)
win1.geometry(f"{aw}x{ah}")
win1.mainloop()
