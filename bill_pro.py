from tkinter import * 
from tkinter import ttk
from tkinter import messagebox as tkmsg
import random
import os


root = Tk()
number  = random.randint(1000,50000)

def qt():
    x = tkmsg.askyesno('Exit Billing Software','Do you realy want to Exit Software')

    if x>0:
        root.destroy()

    else:
        return


def genrate():
    if name_var.get()=='' or phn_var.get()=='':
        tkmsg.showerror('Details Unfilled','Please Enter your Name or Phone Number')
        return


    txt_box.delete('1.0',END)


    welcomescr()
    if brd_var1.get()>0:
        txt_box.insert(END,(f'\n\tBeardo Dark Side\t\t\t{brd_var1.get()}\t\t{fn_p1}'))
    if cob_var.get()>0:
        txt_box.insert(END,(f'\n\tCobra Ltd Ed.\t\t\t{cob_var.get()}\t\t{fn_p2}'))
    if jag_var.get()>0:
        txt_box.insert(END,(f'\n\tJaguar Classic\t\t\t{jag_var.get()}\t\t{fn_p3}'))
    if ca_var.get()>0:
        txt_box.insert(END,(f'\n\tCreed Aventus\t\t\t{ca_var.get()}\t\t{fn_p4}'))
    if rk_var.get()>0:
        txt_box.insert(END,(f'\n\tRobert Kavali\t\t\t{rk_var.get()}\t\t{fn_p5}'))


    if bw_var.get()>0:
        txt_box.insert(END,(f'\n\tBeardo Wax\t\t\t{bw_var.get()}\t\t{fn_h1}'))
    if sw_var.get()>0:
        txt_box.insert(END,(f'\n\tSet Wet\t\t\t{sw_var.get()}\t\t{fn_h2}'))
    if lp_var.get()>0:
        txt_box.insert(END,(f'\n\tLoReal Proffessial\t\t\t{lp_var.get()}\t\t{fn_h3}'))
    if mds_var.get()>0:
        txt_box.insert(END,(f'\n\tMade HAir Spray\t\t\t{mds_var.get()}\t\t{fn_h4}'))
    if vega_var.get()>0:
        txt_box.insert(END,(f'\n\tVega hair Brush\t\t\t{vega_var.get()}\t\t{fn_h5}'))


    if pht_var.get()>0:
        txt_box.insert(END,(f'\n\tPhillips Trimmer\t\t\t{pht_var.get()}\t\t{fn_g1}'))
    if brn_var.get()>0:
        txt_box.insert(END,(f'\n\tBrawn Trimmer\t\t\t{brn_var.get()}\t\t{fn_g2}'))
    if brf_var.get()>0:
        txt_box.insert(END,(f'\n\tBeardo Face Wash\t\t\t{brf_var.get()}\t\t{fn_g3}'))
    if mcc_var.get()>0:
        txt_box.insert(END,(f'\n\tMcCaffiene\t\t\t{mcc_var.get()}\t\t{fn_g4}'))
    txt_box.insert(END,'\n----------------------------------------------------------------------------------------------------------')
    txt_box.insert(END,f'\t\tTOtal Bill : \t\t\t{tot_var.get()}')
    txt_box.insert(END,f'\n\tTax : \t\t\t{str(tx_var.get())}')
    txt_box.insert(END,'\n----------------------------------------------------------------------------------------------------------')
    txt_box.insert(END,'\t\t\t\tThank You For Shopping')


def col(rgb):
    return "#%02x%02x%02x"%rgb

def abt_us():
    tkmsg.showinfo('About Us','Made by - Ayush Mahawar , Abhinav Bhardwaj , Harsh Chauhan')


def tot_bill():
    if name_var.get()=='' or phn_var.get()=='':
        tkmsg.showerror('Details Unfilled','Please Enter your Name or Phone Number')
        return
    # ================ PERFUMES ========================
                # ======= fn qty perfumes ===============
    p1 = brd_var1.get()
    p2 = cob_var.get()
    p3 = jag_var.get()
    p4 = ca_var.get()
    p5 = rk_var.get()

                #======================== prices of perfumes =================================

    p_brd_per = 1500
    cobra_p = 200
    jag_p = 1999
    ca_p = 1149
    rk_p= 5850

                # ========= final price of perfumes ==================
    
    global fn_p1
    fn_p1 = p_brd_per * p1

    global fn_p2
    fn_p2 = cobra_p * p2
    
    global fn_p3 
    fn_p3 = jag_p * p3

    global fn_p4
    fn_p4 =  ca_p* p4

    global fn_p5
    fn_p5 =  rk_p * p5

    fn_P1 = fn_p1+fn_p2+fn_p3+fn_p4+fn_p5

    # =====================================================


    # =========================== HAIR STYLLING =====================

    h1 = bw_var.get()
    h2 = sw_var.get()
    h3 = lp_var.get()
    h4 = mds_var.get()
    h5 = vega_var.get()

    
        #============================ hair style price ===============

    brd_wx = 275
    stwt = 150
    lp_p = 1299
    mhs = 385
    vhb = 325

        # ==============================================================================


        # ====================== FINAL PRICE OF HAIR PRODUCTS ====================
    global fn_h1
    fn_h1 = h1 * brd_wx

    global fn_h2
    fn_h2 = h2 * stwt

    global fn_h3
    fn_h3 = h3 * lp_p

    global fn_h4
    fn_h4 = h4 * mhs

    global fn_h5
    fn_h5 = h5 * vhb


    fn_hair = fn_h1+fn_h2+fn_h3+fn_h4+fn_h5

        # ========================================================================


    # ================== GROOMING ============================

    # ========================== OTY ===========================
    g1= pht_var.get()
    g2 = brn_var.get()
    g3 = brf_var.get()
    g4 = mcc_var.get()


    # =========================grooming price =======================================

    phil_tri = 450
    brn_trim = 400
    brd_fw = 250
    mccaf = 1488

    # =============================================================================

    global fn_g1
    fn_g1 = g1*phil_tri

    global fn_g2
    fn_g2 = g2*brn_trim

    global fn_g3
    fn_g3 = g3*brd_fw

    global fn_g4
    fn_g4 = g4*mccaf

    fn_g = fn_g1+fn_g2+fn_g3+fn_g4
    # ===============================================================

    Total_p = fn_g + fn_P1 + fn_hair
    tot_var.set(f'Rs. {Total_p}')

    tx = round(float(Total_p*0.02),2)
    tx_var.set(f'Rs. {tx}')

    if Total_p==0:
        tkmsg.showerror('Not Bought Anything','Please Select atleast One product ')

def sv_bill():
    if tot_var.get()=='0.0':
        tkmsg.showerror('Not Bought Anything','Please Bought something, to save your bill')
    else:
        ans = tkmsg.askyesno('Save Bill','Your want to save your bill')
        if ans==0:
            return
        else:
            bill_data = txt_box.get('1.0',END)
            f = open(f'Bills\\{number}.txt','a')
            content = f.write(bill_data)
            f.close()
            tkmsg.showinfo('Saved',f'Your Bill {number} number is saved succesfully')

def get_bill():
    for  i in os.listdir('Bills'):
        if i == f'{billnum_var.get()}.txt':
            txt_box.delete('1.0',END)
            f1= open(f'Bills\\{i}','r')
            for j in f1:
                txt_box.insert(END,j)
            f1.close()


bg_col = col((128, 20, 69))
fg_col = col((209, 121, 161))
sec_col = col((237, 154, 173))
root.geometry('1500x786+10+10')
root.maxsize(1500,786)
root.minsize(1500,786)


root.iconbitmap(r'bill_ZeH_icon.ico')
root.title('Billing Software')
root.config(bg='black')


def gr_p():


    grom_p =  Tk()
    grom_p.title('Price Of Hair product')
    grom_p.geometry('300x300+13+62')
    grom_p.maxsize(300,300)
    grom_p.minsize(300,300)

    def col(rgb):
        return "#%02x%02x%02x"%rgb


    color1 =  col((33, 110, 110))

    header = Label(grom_p,text='Original GroomingProduct Price',font=('Times of Roman',12,'bold'),bd=10,relief=GROOVE,bg = color1,fg='white')
    header.pack(fill=X,ipady=8)


    fr1 = LabelFrame(grom_p,text='Grooming Product',font=('Times of Roman',10,'bold'),bg=color1,fg='gold',bd=10,relief=GROOVE)
    fr1.place(x=0,y=60)


    ph_tp = Label(fr1,text='Phillips trimmer',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    ph_tp.grid(row=0,column=0,pady = 15)


    brn_tp = Label(fr1,text='Brawn trimmer',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    brn_tp.grid(row=1,column=0,pady=15)


    brd_fw_p = Label(fr1,text='Beardo Face Wash',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    brd_fw_p.grid(row=2,column=0,pady=15,padx=10)


    mcc_op = Label(fr1,text='McCaffeine',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    mcc_op.grid(row=3,column=0,pady=15)


        # phil_tri = 450
        # brn_trim = 400
        # brd_fw = 250
        # mccaf = 1488


    fr2 = LabelFrame(grom_p,text='Price',font=('Times of Roman',10,'bold'),bg=color1,fg='gold',bd=10,relief=GROOVE)
    fr2.place(x=173,y=60,width=120)

    pht_op = Label(fr2,text='Rs. 450',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    pht_op.grid(row=0,column=0,pady = 15,padx=20)


    brntr_p = Label(fr2,text='Rs. 400',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    brntr_p.grid(row=1,column=0,pady=15)


    brdfw_p = Label(fr2,text='Rs. 250',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    brdfw_p.grid(row=2,column=0,pady=15)


    mccaf_pr = Label(fr2,text='Rs. 1488',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    mccaf_pr.grid(row=3,column=0,pady=15)


    grom_p.mainloop()

def hs_p():

    hsp_win =  Tk()
    hsp_win.title('Price Of Hair product')
    hsp_win.geometry('300x380+13+62')
    hsp_win.maxsize(300,380)
    hsp_win.minsize(300,380)

    def col(rgb):
        return "#%02x%02x%02x"%rgb


    color1 =  col((33, 110, 110))

    header = Label(hsp_win,text='Original HairProduct Price',font=('Times of Roman',12,'bold'),bd=10,relief=GROOVE,bg = color1,fg='white')
    header.pack(fill=X,ipady=8)


    fr1 = LabelFrame(hsp_win,text='Hair Product',font=('Times of Roman',10,'bold'),bg=color1,fg='gold',bd=10,relief=GROOVE)
    fr1.place(x=0,y=60)


    brd_wx = Label(fr1,text='Beardo wax',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    brd_wx.grid(row=0,column=0,pady = 15)


    set_w = Label(fr1,text='Set Wet',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    set_w.grid(row=1,column=0,pady=15)


    lrp = Label(fr1,text='LoReal Professinnel',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    lrp.grid(row=2,column=0,pady=15,padx=10)


    mhs_p = Label(fr1,text='Made Hair Spray',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    mhs_p.grid(row=3,column=0,pady=15)


    ve_hb = Label(fr1,text='vega Hair Brush',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    ve_hb.grid(row=4,column=0,pady=30)


        # brd_wx = 275
        # stwt = 150
        # lp_p = 1299
        # mhs = 385
        # vhb = 325


    fr2 = LabelFrame(hsp_win,text='Price',font=('Times of Roman',10,'bold'),bg=color1,fg='gold',bd=10,relief=GROOVE)
    fr2.place(x=176,y=60,width=120)

    brwp = Label(fr2,text='Rs. 275',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    brwp.grid(row=0,column=0,pady = 15,padx=20)


    sw_p = Label(fr2,text='Rs. 150',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    sw_p.grid(row=1,column=0,pady=15)


    lrp_p = Label(fr2,text='Rs. 1299',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    lrp_p.grid(row=2,column=0,pady=15)


    mhs_pr = Label(fr2,text='Rs. 385',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    mhs_pr.grid(row=3,column=0,pady=15)


    veg_p = Label(fr2,text='Rs. 325',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    veg_p.grid(row=4,column=0,pady=30)


    hsp_win.mainloop()

def per_p():

    perfume =  Tk()
    perfume.title('Price Of Perfumes')
    perfume.geometry('300x380+13+62')
    perfume.maxsize(300,380)
    perfume.minsize(300,380)

    def col(rgb):
        return "#%02x%02x%02x"%rgb


    color1 =  col((33, 110, 110))

    header = Label(perfume,text='Original Perfumes Price',font=('Times of Roman',12,'bold'),bd=10,relief=GROOVE,bg = color1,fg='white')
    header.pack(fill=X,ipady=8)


    fr1 = LabelFrame(perfume,text='Perfumes',font=('Times of Roman',10,'bold'),bg=color1,fg='gold',bd=10,relief=GROOVE)
    fr1.place(x=0,y=60)


    brd_drk = Label(fr1,text='Beardo Dark Side',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    brd_drk.grid(row=0,column=0,pady = 15,padx=10)


    cobra_lt = Label(fr1,text='Cobra Ltd Ed.',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    cobra_lt.grid(row=1,column=0,pady=15)


    jag_c = Label(fr1,text='jaguar Classic',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    jag_c.grid(row=2,column=0,pady=15)


    ca_op = Label(fr1,text='Beardo Dark Side',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    ca_op.grid(row=3,column=0,pady=15)


    rk_op = Label(fr1,text='Beardo Dark Side',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    rk_op.grid(row=4,column=0,pady=30)


    '''  p_brd_per = 1500
        cobra_p = 200
        jag_p = 1999
        ca_p = 1149
        rk_p= 5850'''


    fr2 = LabelFrame(perfume,text='Price',font=('Times of Roman',10,'bold'),bg=color1,fg='gold',bd=10,relief=GROOVE)
    fr2.place(x=162,y=60,width=137)

    brd_drkp = Label(fr2,text='Rs. 1500',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    brd_drkp.grid(row=0,column=0,pady = 15,padx=20)


    cobra_ltp = Label(fr2,text='Rs. 200',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    cobra_ltp.grid(row=1,column=0,pady=15)


    jag_cp = Label(fr2,text='Rs. 1999',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    jag_cp.grid(row=2,column=0,pady=15)


    ca_opp = Label(fr2,text='Rs. 1149',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    ca_opp.grid(row=3,column=0,pady=15)


    rk_opp = Label(fr2,text='Rs. 5850',font = ('Times of Roman',10,'bold'),bg=color1,fg='white')
    rk_opp.grid(row=4,column=0,pady=30)

    perfume.mainloop()

# ====================== menu bar ===================================

mymenu = Menu(root)
m1 =Menu(mymenu,tearoff=0)
m1.add_command(label  = 'Perfumes',command= per_p)
m1.add_command(label= 'HairStyling Products',command=hs_p)
m1.add_command(label='Grooming products',command=gr_p)



m3= Menu(mymenu,tearoff=0)
m3.add_command(label = 'About Us',command = abt_us)

root.config(menu=mymenu)
 
mymenu.add_cascade(label = 'Original Price',menu=m1)
mymenu.add_cascade(label='More',menu=m3)


# ====================================================================

lab1 = Label(root,text='BILLING SOFTWARE',font=('Times of Roman',38,'bold'),bd=16,relief=GROOVE,bg=bg_col,fg='white')
lab1.pack(fill=X)

# =======================Information Box ==========================================


f1 = LabelFrame(root,text ="Infomation Box",font=('Times of Roman',12,'bold'),fg='gold',bg=bg_col,bd=10,relief=GROOVE)
f1.place(x=0,y=99,relwidth=1)

name_var  =StringVar()
cus_name = Label(f1,text='''Customer's Name : ''',font = ('Tiems of Roman',18,'bold'),bg=bg_col,fg='white')
cus_name.grid(row=0,column=0,padx=25)
ent_name = Entry(f1,width=15,bd=5,relief=SUNKEN,font=('Times of Roman',15,'bold'),bg=sec_col,textvariable=name_var)
ent_name.grid(row=0,column=1,pady=10)


phn_var = StringVar()
cus_phn = Label(f1,text='''Phone Number :''',font = ('Tiems of Roman',18,'bold'),bg=bg_col,fg='white')
cus_phn.grid(row=0,column=3,padx=25)
ent_phn = Entry(f1,width=15,bd=5,relief=SUNKEN,font=('Times of Roman',15,'bold'),bg=sec_col,textvariable = phn_var)
ent_phn.grid(row=0,column=4,pady=10)


billnum_var = StringVar()
cus_billnum = Label(f1,text='''Bill Number :''',font = ('Tiems of Roman',18,'bold'),bg=bg_col,fg='white')
cus_billnum.grid(row=0,column=5,padx=25)
ent_billnum = Entry(f1,width=15,bd=5,relief=SUNKEN,font=('Times of Roman',15,'bold'),bg=sec_col,textvariable=billnum_var)
ent_billnum.grid(row=0,column=6,pady=12)

serch_btn = Button(f1,text='Search My Bill',font=('Times of Roman',15,'bold'),bd=5,bg=sec_col,command=get_bill)
serch_btn.grid(row=0,column=7,ipadx=10,padx=35)


# =================================================================================


# ======================== perfumes  ====================================

f2 = LabelFrame(root,text ="Perfumes",font=('Times of Roman',12,'bold'),fg='gold',bg=bg_col,bd=10,relief=GROOVE)
f2.place(x=0,y=195)

# ============================================================================

brd_var1 = IntVar()
brdper =Label(f2,text='Beardo Dark Side ',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
brdper.grid(row=0,column=0,padx=15)
brdper_comb = ttk.Combobox(f2,width=20,state='readonly',font=('Times of Roman',11,'bold'),textvariable = brd_var1)
brdper_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
brdper_comb.grid(row=0,column=1,pady=15,padx=10)

cob_var = IntVar()
cobra =Label(f2,text='Cobra Ltd Ed.',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
cobra.grid(row=1,column=0,padx=15,sticky=W)
cob_comb = ttk.Combobox(f2,width=20,textvariable=cob_var,state='readonly',font=('Times of Roman',11,'bold'))
cob_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
cob_comb.grid(row=1,column=1,pady=15,padx=10)

jag_var=IntVar()
jag =Label(f2,text='Jaguar Classic',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
jag.grid(row=2,column=0,padx=15,sticky=W)
jag_comb = ttk.Combobox(f2,width=20,textvariable=jag_var,state='readonly',font=('Times of Roman',11,'bold'))
jag_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
jag_comb.grid(row=2,column=1,pady=15,padx=10)


ca_var = IntVar()
ca =Label(f2,text='Creed Aventus',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
ca.grid(row=3,column=0,padx=15,sticky=W)
ca_comb = ttk.Combobox(f2,width=20,textvariable=ca_var,state='readonly',font=('Times of Roman',11,'bold'))
ca_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
ca_comb.grid(row=3,column=1,pady=15,padx=10)

rk_var = IntVar()
rk =Label(f2,text='Robert Kaveli',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
rk.grid(row=4,column=0,padx=15,sticky=W)
rk_comb = ttk.Combobox(f2,width=20,state='readonly',font=('Times of Roman',11,'bold'),textvariable=rk_var)
rk_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
rk_comb.grid(row=4,column=1,pady=15,padx=10)

# =======================================================================

# ================================ Hair Styling ===========================

f3 = LabelFrame(root,text ="Hair Styling",font=('Times of Roman',12,'bold'),fg='gold',bg=bg_col,bd=10,relief=GROOVE)
f3.place(x=449,y=195)



bw_var = IntVar()
bw =Label(f3,text='Beardo Wax',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
bw.grid(row=0,column=0,padx=15,sticky=W)
bw_comb = ttk.Combobox(f3,width=20,textvariable=bw_var,state='readonly',font=('Times of Roman',11,'bold'))
bw_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
bw_comb.grid(row=0,column=1,pady=15,padx=20)


sw_var = IntVar()
sw =Label(f3,text='Set Wet',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
sw.grid(row=1,column=0,padx=15,sticky=W)
sw_comb = ttk.Combobox(f3,width=20,textvariable=sw_var,state='readonly',font=('Times of Roman',11,'bold'))
sw_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
sw_comb.grid(row=1,column=1,pady=15,padx=20)


lp_var = IntVar()
lp =Label(f3,text='LOreal Professionnel',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
lp.grid(row=2,column=0,padx=15,sticky=W)
lp_comb = ttk.Combobox(f3,width=20,textvariable=lp_var,state='readonly',font=('Times of Roman',11,'bold'))
lp_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
lp_comb.grid(row=2,column=1,pady=15)


mds_var = IntVar()
mds =Label(f3,text='Mades Hair Spray',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
mds.grid(row=3,column=0,padx=15,sticky=W)
mds_comb = ttk.Combobox(f3,width=20,textvariable=mds_var,state='readonly',font=('Times of Roman',11,'bold'))
mds_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
mds_comb.grid(row=3,column=1,pady=15)


vega_var = IntVar()
vega =Label(f3,text='Vega Hair Brush',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
vega.grid(row=4,column=0,padx=15,sticky=W)
vega_comb = ttk.Combobox(f3,width=20,textvariable=vega_var,state='readonly',font=('Times of Roman',11,'bold'))
vega_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
vega_comb.grid(row=4,column=1,pady=15)

# =========================================================================

# ============================== Grooming =====================================

f3 = LabelFrame(root,text ="Grooming",font=('Times of Roman',12,'bold'),fg='gold',bg=bg_col,bd=10,relief=GROOVE)
f3.place(x=0,y=503,height=258)


pht_var = IntVar()
pht =Label(f3,text='Phillips (Trimmer)',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
pht.grid(row=0,column=0,padx=15,sticky=W)
pht_comb = ttk.Combobox(f3,width=20,textvariable=pht_var,state='readonly',font=('Times of Roman',11,'bold'))
pht_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
pht_comb.grid(row=0,column=1,pady=15)


brn_var = IntVar()
brn =Label(f3,text='Brawn (Trimmer)',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
brn.grid(row=1,column=0,padx=15,sticky=W)
brn_comb = ttk.Combobox(f3,width=20,textvariable=brn_var,state='readonly',font=('Times of Roman',11,'bold'))
brn_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
brn_comb.grid(row=1,column=1,pady=15)


brf_var = IntVar()
brf =Label(f3,text='Beardo(face Wash)',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
brf.grid(row=2,column=0,padx=15,sticky=W)
brf_comb = ttk.Combobox(f3,width=20,textvariable=brf_var,state='readonly',font=('Times of Roman',11,'bold'))
brf_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
brf_comb.grid(row=2,column=1,pady=15)


mcc_var = IntVar()
mcc =Label(f3,text='McCaffeine',font=('Times of Roman',16,'bold'),bg=bg_col,fg='white')
mcc.grid(row=3,column=0,padx=15,sticky=W)
mcc_comb = ttk.Combobox(f3,width=20,textvariable=mcc_var,state='readonly',font=('Times of Roman',11,'bold'))
mcc_comb['values'] = (1,2,3,4,5,6,7,8,9,10)
mcc_comb.grid(row=3,column=1,pady=15,padx=3)

# ============================================================================

# =============================== Btn frame ===========================
f_height = 136
f4 = Frame(root,bd=10,relief=GROOVE,bg=bg_col)
f4.place(x=449,y=500,width=490,height=136)

tot_btn = Button(f4,text = 'Total Bill',font=('Times of Roman',10,'bold'),bd=5,bg=sec_col,command=tot_bill)
tot_btn.grid(row=0,column=0,padx=60,pady=10,ipadx=29,ipady=5)

gen_btn = Button(f4,text = 'Generate Bill',font=('Times of Roman',10,'bold'),bd=5,bg=sec_col,command=genrate)
gen_btn.grid(row =0,column=1,padx=40,pady=10,ipadx=10,ipady=5)

sv_btn = Button(f4,text = 'Save Bill',font=('Times of Roman',10,'bold'),border=5,bg=sec_col,command=sv_bill)
sv_btn.grid(row =1,column=0,ipady=5,ipadx=30)

ext_btn = Button(f4,text = 'Exit',font=('Times of Roman',10,'bold'),bd=5,command=qt,bg=sec_col)
ext_btn.grid(row=1,column=1,ipadx = 40,ipady=5)

# ======================================================================

#============================= bill show ================================

f5 = Frame(root,bd=10,relief=GROOVE,bg=bg_col)
f5.place(x=449,y=640,width=490,height=120)


bill_lb = Label(f5,text='Total bill : ',font =('Times of Roman',20,'bold'),bg=bg_col,fg='white')
bill_lb.grid(row=0,column=0,padx = 15,pady=10)


tot_var = StringVar()
ent_totb = Entry(f5,width =20,bd=5,relief=SUNKEN,font=('Times of Roman',15,'bold'),textvariable=tot_var)
ent_totb.grid(row=0,column=1)
tot_var.set(0.00)


tx_var = StringVar()
tx_lab = Label(f5,text = 'Tax : ',font =('Times of Roman',20,'bold'),bg=bg_col,fg='white')
tx_lab.grid(row=1,column=0,padx=15,sticky=W)
tx_ent = Entry(f5,width =20,bd=5,relief=SUNKEN,font=('Times of Roman',15,'bold'),textvariable=tx_var)
tx_ent.grid(row=1,column=1)
tx_var.set(0.00)

# =======================================================================

#=============================== bill txt ===============================

f6 = Frame(root,bd=10,relief=GROOVE,bg=bg_col)
f6.place(x=950,y=195,width=543)

bilin = Label(f6,text='Bill Information',font = ('Times of Roman',20,'bold'),bg=bg_col,fg='white')
bilin.pack()
# ==========================================================================

# ============================= txt box ======================================

bill_info  =StringVar()
txt_box =Text(root,bd=5,relief=SUNKEN,font=('Times of Roman',11,'bold'))
txt_box.place(x=950,y=260,width=543,height = 501)


def welcomescr():
    
    txt_box.insert(END,f'''===========================================================
    \t\t\tShopping Bill
===========================================================
    Customer's Name : {name_var.get()}
    Customer's Phone Number : {phn_var.get()}
    Bill Number : {number}

===========================================================
    \tProduct\t\t\tQty\t\tPrice
    ''')


welcomescr()

root.mainloop()