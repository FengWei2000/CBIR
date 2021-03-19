"""
创建界面，选择文件，创建检索结果界面
"""

from PIL import ImageTk
import tkinter as tk
from tkinter import filedialog
import os
from query import query_picture
from resize import *
import time
from settings import find_num


class Selectdir(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry("1280x720")
        self.Createpage()

    #  创建界面
    def Createpage(self):
        inp1 = tk.Entry(self.root, font=("宋体", 18))
        inp1.pack()
        inp1.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.1)

        #  添加一些小图标
        imgs = Image.open('sousuo.png')
        imgs_resized = Resize(0.05 * 1280, 0.1 * 720, imgs)
        self.imgs = ImageTk.PhotoImage(imgs_resized)
        lbs = tk.Label(self.root, imag=self.imgs, compound=tk.CENTER, bg='white')
        lbs.place(relx=0.15, rely=0.3, relwidth=0.05, relheight=0.1)

        imgt = Image.open('tupian.png')
        imgt_resized = Resize(0.05 * 1280, 0.1 * 720, imgt)
        self.imgt = ImageTk.PhotoImage(imgt_resized)
        lbt = tk.Label(self.root, imag=self.imgt, compound=tk.CENTER, bg='lightskyblue')
        lbt.place(relx=0.05, rely=0.05, relwidth=0.05, relheight=0.1)

        imgc = Image.open('chengyuan.png')
        imgc_resized = Resize(0.05 * 1280, 0.1 * 720, imgc)
        self.imgc = ImageTk.PhotoImage(imgc_resized)
        lbc = tk.Label(self.root, imag=self.imgc, compound=tk.CENTER, bg='white')
        lbc.place(relx=0.7, rely=0.9, relwidth=0.05, relheight=0.1)

        #  标注作者姓名
        lbname = tk.Label(self.root, text="李佳乐 冯威", font=("宋体", 20), bg='white')
        lbname.place(relx=0.75, rely=0.9, relwidth=0.15, relheight=0.1)
        #  本地上传图标
        databutton = tk.Button(self.root, text="本地上传",font=("宋体", 20), command=lambda: Choosedatadir(inp1))
        databutton.place(relx=0.8, rely=0.3, relwidth=0.1, relheight=0.1)
        #  开始检索图标
        enterbutton = tk.Button(self.root, text="开始检索",font=("宋体", 20), command=lambda: Enter())
        enterbutton.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.1)

        #  选择图片
        def Choosedatadir(inp1):
            self.root.picture = filedialog.askopenfilename(parent=self.root, initialdir=os.getcwd(), title="本地上传")
            inp1.insert(0, self.root.picture)

        #  输入框地址为图片地址
        def Enter():
            var = inp1.get()

            start = time.perf_counter()
            im_ls = query_picture(var, find_num)
            end = time.perf_counter()
            run_time = end - start
            print('run_time:', run_time)

            #  关闭主页面，创建结果界面
            self.root.destroy()
            result = tk.Tk()
            result.geometry("1280x720")
            result.title('查询结果')
            photo = tk.PhotoImage(file="a.gif")  # 背景图片

            background = tk.Label(result, image=photo, compound=tk.CENTER)
            background.place(relx=0, rely=0, relwidth=1, relheight=1)

            backbutton = tk.Button(result, text="返回", font=("宋体", 25), command=lambda: Back(result))
            backbutton.place(relx=0.8, rely=0.1, relwidth=0.08, relheight=0.08)

            word1 = tk.Label(result, text='将要检索的图片如下', font=("宋体", 25), image=photo, compound=tk.CENTER)
            word1.place(relx=0.1, rely=0, relwidth=0.3, relheight=0.07)

            word2 = tk.Label(result, text='检索结果如下', font=("宋体", 25), image=photo, compound=tk.CENTER)
            word2.place(relx=0.15, rely=0.4, relwidth=0.2, relheight=0.07)

            #  上传的图片
            img0 = Image.open(var)
            img0_resized = Resize(0.3 * 1280, 0.3 * 720, img0)
            img0 = ImageTk.PhotoImage(img0_resized)
            lb0 = tk.Label(result, imag=img0, compound=tk.CENTER)
            lb0.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.3)
            #  十张检索结果图
            img1 = Image.open(im_ls[0])
            img1_resized = Resize(0.19 * 1280, 0.2 * 720, img1)
            img1 = ImageTk.PhotoImage(img1_resized)
            lb1 = tk.Label(result, imag=img1, compound=tk.CENTER)
            lb1.place(relx=0, rely=0.5, relwidth=0.19, relheight=0.2)

            img2 = Image.open(im_ls[1])
            img2_resized = Resize(0.19 * 1280, 0.2 * 720, img2)
            img2 = ImageTk.PhotoImage(img2_resized)
            lb2 = tk.Label(result, imag=img2, compound=tk.CENTER)
            lb2.place(relx=0.2, rely=0.5, relwidth=0.19, relheight=0.2)

            img3 = Image.open(im_ls[2])
            img3_resized = Resize(0.19 * 1280, 0.2 * 720, img3)
            img3 = ImageTk.PhotoImage(img3_resized)
            lb3 = tk.Label(result, imag=img3, compound=tk.CENTER)
            lb3.place(relx=0.4, rely=0.5, relwidth=0.19, relheight=0.2)

            img4 = Image.open(im_ls[3])
            img4_resized = Resize(0.19 * 1280, 0.2 * 720, img4)
            img4 = ImageTk.PhotoImage(img4_resized)
            lb4 = tk.Label(result, imag=img4, compound=tk.CENTER)
            lb4.place(relx=0.6, rely=0.5, relwidth=0.19, relheight=0.2)

            img5 = Image.open(im_ls[4])
            img5_resized = Resize(0.19 * 1280, 0.2 * 720, img5)
            img5 = ImageTk.PhotoImage(img5_resized)
            lb5 = tk.Label(result, imag=img5, compound=tk.CENTER)
            lb5.place(relx=0.8, rely=0.5, relwidth=0.19, relheight=0.2)

            img6 = Image.open(im_ls[5])
            img6_resized = Resize(0.19 * 1280, 0.2 * 720, img6)
            img6 = ImageTk.PhotoImage(img6_resized)
            lb6 = tk.Label(result, imag=img6, compound=tk.CENTER)
            lb6.place(relx=0, rely=0.75, relwidth=0.19, relheight=0.2)

            img7 = Image.open(im_ls[6])
            img7_resized = Resize(0.19 * 1280, 0.2 * 720, img7)
            img7 = ImageTk.PhotoImage(img7_resized)
            lb7 = tk.Label(result, imag=img7, compound=tk.CENTER)
            lb7.place(relx=0.2, rely=0.75, relwidth=0.19, relheight=0.2)

            img8 = Image.open(im_ls[7])
            img8_resized = Resize(0.19 * 1280, 0.2 * 720, img8)
            img8 = ImageTk.PhotoImage(img8_resized)
            lb8 = tk.Label(result, imag=img8, compound=tk.CENTER)
            lb8.place(relx=0.4, rely=0.75, relwidth=0.19, relheight=0.2)

            img9 = Image.open(im_ls[8])
            img9_resized = Resize(0.19 * 1280, 0.2 * 720, img9)
            img9 = ImageTk.PhotoImage(img9_resized)
            lb9 = tk.Label(result, imag=img9, compound=tk.CENTER)
            lb9.place(relx=0.6, rely=0.75, relwidth=0.19, relheight=0.2)

            img10 = Image.open(im_ls[9])
            img10_resized = Resize(0.19 * 1280, 0.2 * 720, img10)
            img10 = ImageTk.PhotoImage(img10_resized)
            lb10 = tk.Label(result, imag=img10, compound=tk.CENTER)
            lb10.place(relx=0.8, rely=0.75, relwidth=0.19, relheight=0.2)

            result.mainloop()

        #  返回按键
        def Back(result):
            result.destroy()

            root = tk.Tk()
            root.title('CBIR')
            photo = tk.PhotoImage(file="a.gif")  # 背景图片

            lb0 = tk.Label(root, image=photo, compound=tk.CENTER)
            lb0.place(relx=0, rely=0, relwidth=1, relheight=1)
            lb1 = tk.Label(root, text='请输入需要检索的图片', font=("宋体", 25), image=photo, compound=tk.CENTER)
            lb1.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)

            Selectdir(root)
            root.mainloop()
