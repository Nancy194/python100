# 题目：画图，学用circle画圆形。

from tkinter import *

canvas = Canvas(width=400, height=500, bg='yellow')
canvas.pack(expand=YES, fill=BOTH)

k = 1
j = 1
for i in range(0,26):
    canvas.create_oval(210 - k,210 - k,210 + k,210 + k, width=0.5)
    k += j
    j += 0.5
mainloop()

'''

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
'''