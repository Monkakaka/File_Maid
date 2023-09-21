import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from datetime import datetime

## 윈도우 기본 설정
window = Tk()
window.title("Search Maid")
window.geometry("700x700")
window.resizable(False, False)

source_folder = ""
destination_folder = ""
cutoff_time = None  # 초기값은 None으로 설정

photo = PhotoImage(file="C:/Users/ChoiJaeDong/source/repos/File Maid/000.png")

## 폴더 버튼 기능
def select_source():
    global source_folder
    source_folder = filedialog.askdirectory()
    txt1.configure(text=source_folder)

def select_destination():
    global destination_folder
    destination_folder = filedialog.askdirectory()
    txt3.configure(text=destination_folder)
     
def open_destination():
    if destination_folder:
        os.startfile(destination_folder)

def set_cutoff_time():
    global cutoff_time
    date_str = simpledialog.askstring("날짜 입력", "날짜를 입력하세요 (YYYY-MM-DD):")
    try:
        cutoff_time = datetime.strptime(date_str, "%Y-%m-%d")
        txt2.configure(text=cutoff_time)
    except ValueError:
        pass

def copy_new_files():
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    if cutoff_time is None:
        return
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if file_creation_time > cutoff_time:
                shutil.copy(file_path, os.path.join(destination_folder, file))

## 위젯 배치
label1 = Label(window, text='1. 어떤 폴더에서 찾으실건가요?')
label1.pack(side=TOP, pady=20)

txt1 = Label(window, text=" ")
txt1.pack(side=TOP)

button1 = Button(window, text="폴더 찾기", command=select_source)
button1.pack(side=TOP, pady=20)

label2 = Label(window, text='2. 어떤 조건으로 찾으실건가요?')
label2.pack(side=TOP, pady=20)

txt2 = Label(window, text=" ")
txt2.pack(side=TOP)

set_date_button = Button(window, text="날짜 설정", command=set_cutoff_time)
set_date_button.pack(side=TOP, pady=20)

label3 = Label(window, text='1. 어떤 폴더에 놔두실건가요?')
label3.pack(side=TOP, pady=20)

txt3 = Label(window, text=" ")
txt3.pack(side=TOP)

button2 = Button(window, text="폴더 찾기", command=select_destination)
button2.pack(side=TOP, pady=20)

button3 = Button(window, text="작업 시키기", command=copy_new_files, image=photo)
button3.pack(side=TOP, pady=20)

button4 = Button(window, text="작업 확인하기", command=open_destination, width=15, height=2)
button4.pack(side=TOP, pady=20)

window.mainloop()
