"""
主界面
"""
from Selectdir import *

#  创建主界面
root = tk.Tk()
root.title('CBIR')
photo = tk.PhotoImage(file="a.gif")  # 背景图片

#  添加背景和标题
lb0 = tk.Label(root, image=photo, compound=tk.CENTER)
lb0.place(relx=0, rely=0, relwidth=1, relheight=1)
lb1 = tk.Label(root, text='请输入需要检索的图片', font=("宋体", 25), image=photo, compound=tk.CENTER)
lb1.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)

Selectdir(root)
root.mainloop()
