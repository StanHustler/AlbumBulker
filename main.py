import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askdirectory
import os
import os.path
import shutil

import get


def select_path():
    _path_ = askdirectory()
    vPath.set(_path_)


def del_file(path_data):
    for i in os.listdir(path_data):  # 返回一个含有目录下所有东西的列表
        file_data = path_data + "\\" + i  # 绝对路径
        if os.path.isfile(file_data):  # 判断path所对应的是否是已存在的文件
            os.remove(file_data)  # 删除文件
        else:
            shutil.rmtree(file_data)  # 递归删除一个目录以及目录内的所有内容
    tk.messagebox.showinfo(title="OK", message="OK")


MainWindow = tk.Tk()
MainWindow.title("AB")
# MainWindow.geometry('220x250')

vPath = tk.StringVar()
vNum = tk.IntVar()
# 1st row
tk.Label(MainWindow, text="Path:").grid(row=0, column=0)
tk.Entry(MainWindow, textvariable=vPath).grid(row=0, column=1)
tk.Button(MainWindow, text="Select", command=select_path).grid(row=0, column=2)

# 2nd row
tk.Button(MainWindow, text='Clear', font=('Arial', 12), width=10, height=1, command=lambda: del_file(vPath.get())).grid(
    row=1, column=1)

# 3rd row
tk.Label(MainWindow, text="Num:").grid(row=2, column=0)
tk.Entry(MainWindow, textvariable=vNum).grid(row=2, column=1)
tk.Button(MainWindow, text="Download", command=lambda: get.down_song(vNum.get(), vPath.get())).grid(row=2, column=2)

MainWindow.mainloop()
