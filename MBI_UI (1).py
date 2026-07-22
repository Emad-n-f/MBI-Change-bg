from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry('350x200+550+280')
win.resizable(0,0)
win.title('Emad noudeh farahani') 
print('??????????????????????')

def mbi():
    if (len(ent_h.get()) >= 1 and len(ent_w.get())) >= 1:
        height = float(ent_h.get())
        weight = float(ent_w.get())
        mbi = weight/(height**2)
        if mbi < 18.5:
            messagebox.showinfo('MBI',f'your mbi is{mbi} \nYou have underweight.')
        elif 18.5 <= mbi <25:
            messagebox.showinfo('MBI',f'your mbi is{mbi} \nYou are normal.')
        elif 25 <= mbi <30:
            messagebox.showinfo('MBI',f'your mbi is{mbi} \nYou have overweight.')
        elif mbi >= 30:
            messagebox.showinfo('MBI',f'your mbi is{mbi} \nYou are very fat.')
    else:
        messagebox.showerror('Erorr!','feilds are empty!')
    ent_h.delete(0,END)
    ent_w.delete(0,END)


ent_h = Entry(win,width=30)
ent_h.place(x=110,y=50)
ent_w = Entry(win,width=30)
ent_w.place(x=110,y=100)


lbl_wellcome = Label(win,text='Wellcome to MBI calculate',font='Arial 15')
lbl_wellcome.pack()
lbl_h = Label(win,text='Height',font='Arial 13')
lbl_h.place(x=20,y=50)
lbl_h = Label(win,text='Weight',font='Arial 12')
lbl_h.place(x=20,y=100)


btn_MBI = Button(win,text='Show MBI',width=20,height=2,bg='green',fg='#FFFFFF',command=mbi)
btn_MBI.place(x=110,y=145)


win.mainloop()