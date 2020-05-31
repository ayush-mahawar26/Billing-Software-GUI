from tkinter import *

qty = Tk()

qty.geometry('793x250')
qty.maxsize(793,250)
qty.minsize(793,250)

qty.title('Stock Available')


lab1 = Label(qty,text='Available Quantity',font=('times of Roman',20,'bold'),bd = 10,relief=GROOVE)
lab1.pack(fill=X)

# ============================== perfuems =========================================

frame1 = LabelFrame(qty,text='Perfumes',font=('Times of Roman',10,'bold'),bd=6,relief=SUNKEN)
frame1.place(x=2,y=56)

lab_p1 = Label(frame1,text='Beardo Dark Side',font=('Times of Roman',13,'bold'))
lab_p1.grid(row=0,column=0,pady=5)

lab_p2 =  Label(frame1,text='Cobra Ltd Ed.',font=('Times of Roman',13,'bold'))
lab_p2.grid(row=1,column=0,pady=5)

lab_p3 =  Label(frame1,text='Jaguar Classic',font=('Times of Roman',13,'bold'))
lab_p3.grid(row=2,column=0,pady=5)

lab_p4 =  Label(frame1,text='Creed Aventus',font=('Times of Roman',13,'bold'))
lab_p4.grid(row=3,column=0,pady=5)

lab_p5 =  Label(frame1,text='Robert Kavali',font=('Times of Roman',13,'bold'))
lab_p5.grid(row=4,column=0)

global per1
per1 =  20

global per2
per2 =  20

global per3
per3 =  20

global per4
per4 =  20

global per5
per5 =  20

# Quantity
frame2 = LabelFrame(qty,text='Quantity',font=('Times of Roman',10,'bold'),bd=6,relief=SUNKEN)
frame2.place(x=165,y=56)

qtlab1 = Label(frame2,text=per1,font=('Times of Roman',13,'bold'))
qtlab1.grid(row=0,column=0,pady=5,ipadx=3)

qtlab2 = Label(frame2,text=per2,font=('Times of Roman',13,'bold'))
qtlab2.grid(row=2,column=0,pady=5,ipadx=3)

qtlab3 = Label(frame2,text=per3,font=('Times of Roman',13,'bold'))
qtlab3.grid(row=3,column=0,pady=5,ipadx=3)

qtlab4 = Label(frame2,text=per4,font=('Times of Roman',13,'bold'))
qtlab4.grid(row=4,column=0,pady=5,ipadx=3)

qtlab5 = Label(frame2,text=per5,font=('Times of Roman',13,'bold'))
qtlab5.grid(row=5,column=0,ipadx=3)


# =================================================================================

frame3 = LabelFrame(qty,text='Hair product',font=('Times of Roman',10,'bold'),bd=6,relief=SUNKEN)
frame3.place(x=255,y=56)

lab_h1 = Label(frame3,text='Beardo Wax',font=('Times of Roman',13,'bold'))
lab_h1.grid(row=0,column=0,pady=5)

lab_h2 =  Label(frame3,text='Set Wet',font=('Times of Roman',13,'bold'))
lab_h2.grid(row=1,column=0,pady=5)

lab_h3 =  Label(frame3,text='LoReal Proffesennal',font=('Times of Roman',13,'bold'))
lab_h3.grid(row=2,column=0,pady=5)

lab_h4 =  Label(frame3,text='Made hair Spray',font=('Times of Roman',13,'bold'))
lab_h4.grid(row=3,column=0,pady=5)

lab_h5 =  Label(frame3,text='Vega Hair brush',font=('Times of Roman',13,'bold'))
lab_h5.grid(row=4,column=0)

global har1
har1 =  20

global har2
har2 =  20

global har3
har3 =  20

global har4
har4 =  20

global har5
har5 =  20

# Quantity
frame4 = LabelFrame(qty,text='Quantity',font=('Times of Roman',10,'bold'),bd=6,relief=SUNKEN)
frame4.place(x=440,y=56)

qt_h1 = Label(frame4,text=har1,font=('Times of Roman',13,'bold'))
qt_h1.grid(row=0,column=0,pady=5,ipadx=3)

qt_h2 = Label(frame4,text=har2,font=('Times of Roman',13,'bold'))
qt_h2.grid(row=2,column=0,pady=5,ipadx=3)

qt_h3 = Label(frame4,text=har3,font=('Times of Roman',13,'bold'))
qt_h3.grid(row=3,column=0,pady=5,ipadx=3)

qt_h4 = Label(frame4,text=har4,font=('Times of Roman',13,'bold'))
qt_h4.grid(row=4,column=0,pady=5,ipadx=3)

qt_h5 = Label(frame4,text=har5,font=('Times of Roman',13,'bold'))
qt_h5.grid(row=5,column=0,ipadx=3)


# ======================== gromming qty =========================

frame5 = LabelFrame(qty,text='Hair product',font=('Times of Roman',10,'bold'),bd=6,relief=SUNKEN)
frame5.place(x=530,y=56)

lab_g1 = Label(frame5,text='Beardo Wax',font=('Times of Roman',13,'bold'))
lab_g1.grid(row=0,column=0,pady=5)

lab_g2 =  Label(frame5,text='Set Wet',font=('Times of Roman',13,'bold'))
lab_g2.grid(row=1,column=0,pady=5)

lab_g3 =  Label(frame5,text='LoReal Proffesennal',font=('Times of Roman',13,'bold'))
lab_g3.grid(row=2,column=0,pady=5)

lab_g4 =  Label(frame5,text='Made hair Spray',font=('Times of Roman',13,'bold'))
lab_g4.grid(row=3,column=0,pady=5)


global gr1
gr1 =  20

global gr2
gr2 =  20

global gr3
gr3 =  20

global gr4
gr4 =  20

# Quantity
frame6 = LabelFrame(qty,text='Quantity',font=('Times of Roman',10,'bold'),bd=6,relief=SUNKEN)
frame6.place(x=710,y=56)

qt_g1 = Label(frame6,text=gr1,font=('Times of Roman',13,'bold'))
qt_g1.grid(row=0,column=0,pady=5,ipadx=3)

qt_g2 = Label(frame6,text=gr2,font=('Times of Roman',13,'bold'))
qt_g2.grid(row=2,column=0,pady=5,ipadx=3)

qt_g3 = Label(frame6,text=gr3,font=('Times of Roman',13,'bold'))
qt_g3.grid(row=3,column=0,pady=5,ipadx=3)

qt_g4 = Label(frame6,text=gr4,font=('Times of Roman',13,'bold'))
qt_g4.grid(row=4,column=0,pady=5,ipadx=3)


qty.mainloop()