import random
from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('400x250+500+300')
win.title('Emad Noudeh Farahani')
win.resizable(0,0)

def ch():
    rand_col = ''
    lst = ["0","1",'2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(6):
        rand_col = rand_col + random.choice(lst)     
    A = '#' + rand_col
    win.configure(bg=A)
    lbl_color = Label(win,text=f'Code of color {A}',width=20)
    lbl_color.place(x=125,y=200)
    
    
win.configure(ch())


btn_ch =Button(win,text='Change color',command=ch,width=20,height=2)
btn_ch.pack(pady=50)








win.mainloop()








