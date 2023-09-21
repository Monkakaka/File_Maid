from tkinter import *
from searchFile import module1

## 윈도우 기본 설정
window = Tk()
window.title("Flie Maid")
window.geometry("300x350")
window.resizable(False, False)



button1 = Button(text="파일 탐색", command=lambda: switch_module(module1), width=30, height=3)
##button2 = Button(text="x", command=lambda: switch_module(module1), width=30, height=3)
##button3 = Button(text="x", command=lambda: switch_module(module1), width=30, height=3)


button1.pack(side=TOP, pady=10)
##button2.pack(side=TOP, pady=10)
##button3.pack(side=TOP, pady=10)



window.mainloop()