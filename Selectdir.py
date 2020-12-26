import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
# from Main import *
import tkinter.font as tkFont
import os
# from search import *
from query import query_picture

class Selectdir(object):
    def __init__(self, master=None):
        self.root = master

        # make the canvas expandable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.root.geometry("1280x720")

        # use these two folderpath to save the path of dataset and queryset (default under this line)
        self.root.queryfolder = r"D:/python/Graduation-design-master/queries"
        self.root.datafolder = r"D:/python/Graduation-design-master/dataset"
        # path to save index.csv
        self.root.indexcsvpath = self.root.queryfolder + "\\"
        # "C:/Users/DYL18/Desktop/Graduation_design/vacation-image-search-engine/queries/"

        self.createpage()

    def createpage(self):

        inp1 = tk.Entry(self.root, command=lambda: entry())
        inp1.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.1)

        databutton = tk.Button(self.root, text="本地上传", width=30, height=8, command=lambda: choosedatadir())
        databutton.place(relx=0.8, rely=0.3, relwidth=0.1, relheight=0.1)


        enterbutton = tk.Button(self.root, text="开始检索", width=60, height=5, command=lambda: enter())
        enterbutton.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.1)

        def entry():
            self.root.picture = inp1.get()


        def choosedatadir():
            self.root.picture = filedialog.askopenfilename(parent=self.root, initialdir=os.getcwd(), title="本地上传")
            print(self.root.datafolder)


        def enter():
            im_ls = query_picture(self.root.picture)

