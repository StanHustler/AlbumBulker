import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askdirectory
import os
import os.path
import shutil


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
tk.Label(MainWindow, text="Path:").grid(row=0, column=0)
tk.Entry(MainWindow, textvariable=vPath).grid(row=0, column=1)
tk.Button(MainWindow, text="Select", command=select_path).grid(row=0, column=2)

tk.Button(MainWindow, text='Clear', font=('Arial', 12), width=10, height=1, command=lambda: del_file(vPath.get())).grid(
    row=1, column=1)
MainWindow.mainloop()
