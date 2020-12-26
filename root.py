import tkinter as tk
from Selectdir import *
import tkinter.font as tkFont

root = tk.Tk()
root.title('CBIR')
photo = tk.PhotoImage(file="a.gif")  # file：t图片路径

lb0 = tk.Label(root, image=photo, compound=tk.CENTER)
lb0.place(relx=0, rely=0, relwidth=1, relheight=1)
lb1 = tk.Label(root, text='请输入需要检索的图片', font=("宋体", 25), image=photo, compound=tk.CENTER)
lb1.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)
# Selectdir(root)
Selectdir(root)
root.mainloop()