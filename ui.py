import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from image import create_image


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.width = 400
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Open file button
        self.open_files_btn = tk.Button(self,
                                        text='Select Files',
                                        command=self.open_files)
        self.open_files_btn.pack(side="top")

        # Quit Button
        self.quit = tk.Button(self,
                              text="QUIT",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def open_files(self):
        self.files = filedialog.askopenfilenames()
        if (len(self.files) > 0):
            self.show_pdf_save_location_picker()

    def show_pdf_save_location_picker(self):
        self.pdf_save_location_btn = tk.Button(self,
                                               text="Where to save PDF?",
                                               command=self.pdf_save_location)
        self.pdf_save_location_btn.pack(side="top")

    def pdf_save_location(self):
        self.pdf_save_location = filedialog.askdirectory()
        self.show_pdf_entry()

    def show_pdf_entry(self):
        # PDF Label
        pdf_name_label_text = tk.StringVar()
        pdf_name_label_text.set('PDF Name')
        self.pdf_name_label = tk.Label(
            self, textvariable=pdf_name_label_text, height=4)
        self.pdf_name_label.pack(side='left')

        # PDF input
        self.pdf_name_value = tk.StringVar()
        self.pdf_name = tk.Entry(self, textvariable=self.pdf_name_value)
        self.pdf_name.pack(side="left")

        # Save file button
        self.save_btn = tk.Button(self,
                                  text='Save',
                                  command=self.save_file)
        self.save_btn.pack(side='bottom')

    def save_file(self):
        pdf_path = self.pdf_save_location + f'/{self.pdf_name_value.get()}'
        create_image(list(self.files), pdf_path)
        messagebox.showinfo('Success', 'PDF was created')
