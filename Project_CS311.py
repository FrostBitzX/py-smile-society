import sqlite3
from tkinter import *
from tkinter import messagebox

def mainwindow() :
    global menubar
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.resizable(FALSE, FALSE)
    root.iconbitmap("icon.ico")
    root.title("𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗦𝗺𝗶𝗹𝗲 𝗦𝗼𝗰𝗶𝗲𝘁𝘆 𝗖𝗮𝗿𝗱")
    root.option_add('*font',"'Barlow', 16")
    root.rowconfigure((0,1,2,3,4,5),weight=1)
    root.columnconfigure((0,1),weight=1)
    menubar = Menu(root)
    menubar.add_command(label="My Profile", command=profileclick)
    menubar.add_command(label="Reward", command=menu1)
    menubar.add_command(label="Donate", command=menu2)
    menubar.add_command(label="Exit", command=root.quit)
    root.config(bg="#B983FF", menu=menubar) 
    return root

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

def loginlayout() :
    global userentry, pwdentry, loginframe
    
    loginframe = Frame(root,bg='white')
    loginframe.rowconfigure((0,1,2,3,4,5),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    loginframe.grid(row=0,column=0,columnspan=2,rowspan=6,sticky='news')
    emptyMenu = Menu(root)
    root.config(bg='#28527a',menu=emptyMenu)
    root.title("𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗦𝗺𝗶𝗹𝗲 𝗦𝗼𝗰𝗶𝗲𝘁𝘆 𝗖𝗮𝗿𝗱")

    Label(loginframe,image=img01,bg='white',border=0).grid(column=0,rowspan=6,sticky="news")

    Label(loginframe,text="SMILE SOCIETY CARD REWARD",font="Dosis 26 bold",bg='white',fg='#2B2B2B').grid(row=0,column=1,padx=30,sticky='news')
    Label(loginframe,text="Member ID",font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=1,column=1,padx=30,sticky='w')
    userentry = Entry(loginframe,bg='#EEEEEE',font="Dosis 20 bold",fg='#2B2B2B', relief="flat",width=36,textvariable=userinfo)
    userentry.grid(row=2,column=1,padx=30,ipady=10,sticky='w')

    Label(loginframe,text="Password",font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=3,column=1,sticky='w',padx=30)
    pwdentry = Entry(loginframe,bg='#EEEEEE',font="Dosis 20 bold",fg='#2B2B2B', relief="flat",width=36,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=4,column=1,padx=30,ipady=10,sticky='w')

    Button(loginframe,relief="flat",bg='white',image=signinbtn,compound="center",command=loginclick).grid(row=5,column=1)
    userentry.focus_force()


def loginclick() :
    global username,point,result,n_id
    if userinfo.get() == "":
        messagebox.showwarning("ADMIN:","Please enter ID Card")
        userentry.focus_force()
    else:
        sql = "select * from user where n_card=?" 
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            if pwdinfo.get() ==  "":
                messagebox.showwarning("ADMIN","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "select * from user where n_card=? AND pass=?"
                cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
                result = cursor.fetchone()
                if result:
                    messagebox.showinfo("ADMIN","Login successfully")
                    username = result[2]
                    point = result[4]
                    n_id = result[0]
                    userentry.delete(0,END)
                    pwdentry.delete(0,END)
                    menu1()
                    
                else:
                    messagebox.showwarning("ADMIN","Incorrect Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showwarning("ADMIN","Member ID not found")       

def profileclick() :
    
    root.title("Welcome "+result[2])
    welcomeframe = Frame(root, bg='white')
    welcomeframe.rowconfigure((0,1,2,3,4), weight=1)
    welcomeframe.rowconfigure(5, weight=5)
    welcomeframe.columnconfigure((0,1),weight=1)
    welcomeframe.place(x=0, y=0, width=w, height=h)

    Label(welcomeframe, image=prof, bg="white").grid(row=0 ,columnspan=2,pady=30)

    Label(welcomeframe, text="Card NO : ", font="Dosis 30 bold",bg="white",fg='#242424').grid(row=1, column=0, sticky="e")
    Label(welcomeframe, text=result[0], font="Dosis 30 bold",bg="white",fg='#4E4E4E').grid(row=1,column=1 ,sticky=W,padx=10)

    Label(welcomeframe, text="Fullname : ", font="Dosis 30 bold",bg="white",fg='#242424').grid(row=2, column=0, sticky="e")
    Label(welcomeframe, text=result[2], font="Dosis 30 bold",bg="white",fg='#4E4E4E').grid(row=2,column=1 ,sticky=W,padx=10)

    Label(welcomeframe, text="Level : ", font="Dosis 30 bold",bg="white",fg='#242424').grid(row=3, column=0, sticky="e")
    Label(welcomeframe, text=result[3], font="Dosis 30 bold",bg="white",fg='#4E4E4E').grid(row=3,column=1 ,sticky=W,padx=10)

    Label(welcomeframe, text="Point : ", font="Dosis 30 bold",bg="white",fg='#242424').grid(row=4, column=0, sticky="e")
    Label(welcomeframe, text=point, font="Dosis 30 bold",bg="white",fg='#4E4E4E').grid(row=4,column=1 ,sticky=W,padx=10)

    Button(welcomeframe,image=signoutbtn,bg="white",relief='flat',command=loginlayout).grid(row=5,columnspan=2)

def menu1():
    global pd1,pd2,pd3,pd4,pd5,pd6,pd7,pd8
    root.config(menu=menubar)
    frame1 = Frame(root,bg='white')
    frame1.place(x=0,y=0,width=w,height=h)
    frame1.columnconfigure(0,weight=2)
    frame1.columnconfigure((1,2,3,4),weight=1)
    frame1.rowconfigure((1,2,3,4,5,6),weight=1)
    frame1.rowconfigure((7),weight=2)

    #left
    left = Frame(frame1,bg='#91E0FF')
    left.grid(rowspan=8,column=0,sticky='news')
    left.columnconfigure(0,weight=1)

    Label(left, image=prof,bg="#91E0FF").grid(row=0,column=0,pady=20)
    Label(left, text=username, bg='#91E0FF',fg='white',font="Dosis 16 bold").grid(row=1,column=0)
    Label(left,text='Point: '+ str(point), image=bgp, bg='#91E0FF',fg='white',font="Dosis 15 bold",compound=CENTER).grid(row=2,column=0,pady=15)
    Button(left,image=signoutbtn,bg="#91E0FF",relief='flat',command=loginlayout).grid(row=3,column=0,pady=30)

    #right
    Label(frame1,text='REWARD',font="Dosis 50 bold",bg='white',fg='#2B2B2B').grid(row=0,columnspan=5,column=1)

    Label(frame1,image=img_pd2,bg='white').grid(row=1,column=1,padx=10)
    pd1 = Button(frame1,image=redeembtn,compound=CENTER,relief='flat',bg='white',command=payment1)
    pd1.grid(row=2,column=1)
    Label(frame1,image=img_pd3,bg='white').grid(row=1,column=2,padx=10)
    pd2 = Button(frame1,image=redeembtn,compound=CENTER,relief='flat',bg='white',command=payment2)
    pd2.grid(row=2,column=2)
    Label(frame1,image=img_pd4,bg='white').grid(row=1,column=3,padx=10)
    pd3 = Button(frame1,image=redeembtn,compound=CENTER,relief='flat',bg='white',command=payment3)
    pd3.grid(row=2,column=3)
    Label(frame1,image=img_pd5,bg='white').grid(row=1,column=4,padx=10)
    pd4 = Button(frame1,image=redeembtn,compound=CENTER,relief='flat',bg='white',command=payment4)
    pd4.grid(row=2,column=4)

    Label(frame1,image=img_pd6,bg='white').grid(row=4,column=1,padx=10)
    pd5 = Button(frame1,image=redeembtn,compound=CENTER,relief='flat',bg='white',command=payment5)
    pd5.grid(row=5,column=1)
    Label(frame1,image=img_pd7,bg='white').grid(row=4,column=2,padx=10)
    pd6 = Button(frame1,image=redeembtn,compound=CENTER,relief='flat',bg='white',command=payment6)
    pd6.grid(row=5,column=2)
    Label(frame1,image=img_pd8,bg='white').grid(row=4,column=3,padx=10)
    pd7 = Button(frame1,image=redeembtn,compound=CENTER,relief='flat',bg='white',command=payment7)
    pd7.grid(row=5,column=3)
    Label(frame1,image=img_pd9,bg='white').grid(row=4,column=4,padx=10)
    pd8 = Button(frame1,image=redeembtn,compound=CENTER,relief='flat',bg='white',command=payment8)
    pd8.grid(row=5,column=4)

    Button(frame1,text='REWARD',relief='flat',bg="#272727",font="Dosis 20 bold",fg='#e8e8e8',command=menu1).grid(row=7,columnspan=2,column=1,sticky='news')
    Button(frame1,text='DONATE',relief='flat',bg="#494949",font="Dosis 20 bold",fg='#e8e8e8',command=menu2).grid(row=7,columnspan=2,column=3,sticky='news')

def payment1():
    global btnclick, pd, p_pd
    btnclick = 1
    pd = 'exercise bike'
    p_pd = 500
    paymentreward()
def payment2():
    global btnclick, pd, p_pd
    btnclick = 2
    pd = 'iphone 13 pro max'
    p_pd = 1000
    paymentreward()
def payment3():
    global btnclick, pd, p_pd
    btnclick = 3
    pd = 'xiaomi bot'
    p_pd = 750
    paymentreward()
def payment4():
    global btnclick, pd, p_pd
    btnclick = 4
    pd = 'nike T-shirt'
    p_pd = 550
    paymentreward()
def payment5():
    global btnclick, pd, p_pd
    btnclick = 5
    pd = 'dior pf'
    p_pd = 675
    paymentreward()
def payment6():
    global btnclick, pd, p_pd
    btnclick = 6
    pd = 'xiaomi purifier'
    p_pd = 850
    paymentreward()
def payment7():
    global btnclick, pd, p_pd
    btnclick = 7
    pd = 'sneaker'
    p_pd = 980
    paymentreward()
def payment8():
    global btnclick, pd, p_pd
    btnclick = 8
    pd = 'marshall'
    p_pd = 120
    paymentreward()

def paymentdn1():
    global btnclickdn, dn
    btnclickdn = 1
    dn = 'มูลนิธิกระจกเงา'
    paymentdonate()
def paymentdn2():
    global btnclickdn, dn
    btnclickdn = 2
    dn = 'มูลนิธิช่วยคนตาบอด แห่งประเทศไทย ในพระบรมราชินูปถัมภ์'
    paymentdonate()
def paymentdn3():
    global btnclickdn, dn
    btnclickdn = 3
    dn = 'มูลนิธิบ้านนกขมิ้น'
    paymentdonate()
def paymentdn4():
    global btnclickdn, dn
    btnclickdn = 4
    dn = 'มูลนิธิหัวใจแห่งประเทศไทย ในพระบรมราชินูปถัมภ์'
    paymentdonate()
def paymentdn5():
    global btnclickdn, dn
    btnclickdn = 5
    dn = 'มูลนิธิเดอะวอยซ์ (เสียงจากเรา)'
    paymentdonate()
def paymentdn6():
    global btnclickdn, dn
    btnclickdn = 6
    dn = 'บ้านพักสี่ขา เพื่อหมาจร'
    paymentdonate()
def paymentdn7():
    global btnclickdn, dn
    btnclickdn = 7
    dn = 'มูลนิธิเด็กอ่อนในสลัมฯ'
    paymentdonate()
def paymentdn8():
    global btnclickdn, dn
    btnclickdn = 8
    dn = 'มูลนิธิรามาธิบดี'
    paymentdonate()

def menu2():
    global dn1,dn2,dn3,dn4,dn5,dn6,dn7,dn8
    root.config(menu=menubar)
    frame1 = Frame(root,bg='white')
    frame1.place(x=0,y=0,width=w,height=h)
    frame1.columnconfigure(0,weight=2)
    frame1.columnconfigure((1,2,3,4),weight=1)
    frame1.rowconfigure((1,2,3,4,5,6),weight=1)
    frame1.rowconfigure((7),weight=2)

    #left
    left = Frame(frame1,bg='#91E0FF')
    left.grid(rowspan=8,column=0,sticky='news')
    left.columnconfigure(0,weight=1)

    Label(left, image=prof,bg="#91E0FF").grid(row=0,column=0,pady=20)
    Label(left, text=username, bg='#91E0FF',fg='white',font="Dosis 16 bold").grid(row=1,column=0)
    Label(left,text='Point: '+ str(point), image=bgp, bg='#91E0FF',fg='white',font="Dosis 15 bold",compound=CENTER).grid(row=2,column=0,pady=15)
    Button(left,image=signoutbtn,bg="#91E0FF",relief='flat',command=loginlayout).grid(row=3,column=0,pady=30)

    #right
    Label(frame1,text='DONATE',font="Dosis 50 bold",bg='white',fg='#2B2B2B').grid(row=0,columnspan=5,column=1)

    Label(frame1,image=img_dn1,bg='white').grid(row=1,column=1,padx=10)
    dn1 = Button(frame1,image=donatebtn,compound=CENTER,relief='flat',bg='white',command=paymentdn1)
    dn1.grid(row=2,column=1)
    Label(frame1,image=img_dn2,bg='white').grid(row=1,column=2,padx=10)
    dn2 = Button(frame1,image=donatebtn,compound=CENTER,relief='flat',bg='white',command=paymentdn2)
    dn2.grid(row=2,column=2)
    Label(frame1,image=img_dn3,bg='white').grid(row=1,column=3,padx=10)
    dn3 = Button(frame1,image=donatebtn,compound=CENTER,relief='flat',bg='white',command=paymentdn3)
    dn3.grid(row=2,column=3)
    Label(frame1,image=img_dn4,bg='white').grid(row=1,column=4,padx=10)
    dn4 = Button(frame1,image=donatebtn,compound=CENTER,relief='flat',bg='white',command=paymentdn4)
    dn4.grid(row=2,column=4)

    Label(frame1,image=img_dn5,bg='white').grid(row=4,column=1,padx=10)
    dn5 = Button(frame1,image=donatebtn,compound=CENTER,relief='flat',bg='white',command=paymentdn5)
    dn5.grid(row=5,column=1)
    Label(frame1,image=img_dn6,bg='white').grid(row=4,column=2,padx=10)
    dn6 = Button(frame1,image=donatebtn,compound=CENTER,relief='flat',bg='white',command=paymentdn6)
    dn6.grid(row=5,column=2)
    Label(frame1,image=img_dn7,bg='white').grid(row=4,column=3,padx=10)
    dn7 = Button(frame1,image=donatebtn,compound=CENTER,relief='flat',bg='white',command=paymentdn7)
    dn7.grid(row=5,column=3)
    Label(frame1,image=img_dn8,bg='white').grid(row=4,column=4,padx=10)
    dn8 = Button(frame1,image=donatebtn,compound=CENTER,relief='flat',bg='white',command=paymentdn8)
    dn8.grid(row=5,column=4)

    Button(frame1,text='REWARD',relief='flat',bg="#494949",font="Dosis 20 bold",fg='#e8e8e8',command=menu1).grid(row=7,columnspan=2,column=1,sticky='news')
    Button(frame1,text='DONATE',relief='flat',bg="#272727",font="Dosis 20 bold",fg='#e8e8e8',command=menu2).grid(row=7,columnspan=2,column=3,sticky='news')

def paymentreward():
    global address1,address2,city,postal,phone
    root.config(menu=menubar)
    frame1 = Frame(root,bg='white')
    frame1.place(x=0,y=0,width=w,height=h)
    frame1.columnconfigure(0,weight=2)
    frame1.columnconfigure((1,2,3,4),weight=1)
    frame1.rowconfigure((1,2,3,4,5,6),weight=1)
    frame1.rowconfigure((7),weight=1)

    #left
    left = Frame(frame1,bg='#91E0FF')
    left.grid(rowspan=8,column=0,sticky='news')
    left.columnconfigure(0,weight=1)

    Label(left, image=prof,bg="#91E0FF").grid(row=0,column=0,pady=20)
    Label(left, text=username, bg='#91E0FF',fg='white',font="Dosis 10 bold").grid(row=1,column=0)
    Label(left,text='Point: '+ str(point), image=bgp, bg='#91E0FF',fg='white',font="Dosis 15 bold",compound=CENTER).grid(row=2,column=0,pady=15)
    Button(left,image=signoutbtn,bg="#91E0FF",relief='flat',command=loginlayout).grid(row=3,column=0,pady=30)

    #right
    if btnclick == 1:
        Label(frame1,image=img_pd2,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclick == 2:
        Label(frame1,image=img_pd3,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclick == 3:
        Label(frame1,image=img_pd4,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclick == 4:
        Label(frame1,image=img_pd5,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclick == 5:
        Label(frame1,image=img_pd6,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclick == 6:
        Label(frame1,image=img_pd7,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclick == 7:
        Label(frame1,image=img_pd8,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclick == 8:
        Label(frame1,image=img_pd9,bg='white').grid(row=0,columnspan=5,column=1)

    Label(frame1,text='Address 1 :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=1,column=1,sticky="e",padx=80)
    address1 = Entry(frame1,width=22,bg='#EEEEEE',relief="flat",textvariable=address1info)
    address1.grid(row=1,column=2,sticky="w",ipady=10)

    Label(frame1,text='Address 2 :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=2,column=1,sticky="e",padx=80)
    address2 = Entry(frame1,width=22,bg='#EEEEEE',relief="flat",textvariable=address2info)
    address2.grid(row=2,column=2,sticky="w",ipady=10)

    Label(frame1,text='City :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=3,column=1,sticky="e",padx=80)
    city = Entry(frame1,width=22,bg='#EEEEEE',relief="flat",textvariable=cityinfo)
    city.grid(row=3,column=2,sticky="w",ipady=10)

    Label(frame1,text='Postal Code :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=4,column=1,sticky="e",padx=80)
    postal = Entry(frame1,width=22,bg='#EEEEEE',relief="flat",textvariable=postalinfo)
    postal.grid(row=4,column=2,sticky="w",ipady=10)

    Label(frame1,text='Phone :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=5,column=1,sticky="e",padx=80)
    phone = Entry(frame1,width=22,bg='#EEEEEE',relief="flat",textvariable=phoneinfo)
    phone.grid(row=5,column=2,sticky="w",ipady=10)

    Label(frame1,text='  Point:',image=scoin,fg='#2B2B2B',font="Dosis 20 bold",bg='white',compound=LEFT).grid(row=7,column=1,padx=30,sticky='e')
    Label(frame1,text=p_pd,fg='#2B2B2B',font="Dosis 20 bold",bg='white',compound=CENTER).grid(row=7,column=2,padx=30,sticky='w')    

    Button(frame1,text='Redeem',bg="#B0DCF8",fg='#2B2B2B',font="Dosis 20 bold",width=10,relief="flat",command=rewardclick).grid(row=7,column=3)
    Button(frame1,text='Back',bg="#B0DCF8",fg='#2B2B2B',font="Dosis 20 bold",width=10,relief="flat",command=menu1).grid(row=7,column=4)

def paymentdonate():
    global f_name, l_name, p_num, email, count
    root.config(menu=menubar)
    frame1 = Frame(root,bg='white')
    frame1.place(x=0,y=0,width=w,height=h)
    frame1.columnconfigure(0,weight=2)
    frame1.columnconfigure((1,2,3,4),weight=1)
    frame1.rowconfigure((1,2,3,4,5,6),weight=1)
    frame1.rowconfigure((7),weight=1)

    #left
    left = Frame(frame1,bg='#91E0FF')
    left.grid(rowspan=8,column=0,sticky='news')
    left.columnconfigure(0,weight=1)

    Label(left, image=prof,bg="#91E0FF").grid(row=0,column=0,pady=20)
    Label(left, text=username, bg='#91E0FF',fg='white',font="Dosis 10 bold").grid(row=1,column=0)
    Label(left,text='Point: '+ str(point), image=bgp, bg='#91E0FF',fg='white',font="Dosis 15 bold",compound=CENTER).grid(row=2,column=0,pady=15)
    Button(left,image=signoutbtn,bg="#91E0FF",relief='flat',command=loginlayout).grid(row=3,column=0,pady=30)

    #right
    if btnclickdn == 1:
        Label(frame1,image=img_dn1,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclickdn == 2:
        Label(frame1,image=img_dn2,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclickdn == 3:
        Label(frame1,image=img_dn3,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclickdn == 4:
        Label(frame1,image=img_dn4,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclickdn == 5:
        Label(frame1,image=img_dn5,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclickdn == 6:
        Label(frame1,image=img_dn6,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclickdn == 7:
        Label(frame1,image=img_dn7,bg='white').grid(row=0,columnspan=5,column=1)
    elif btnclickdn == 8:
        Label(frame1,image=img_dn8,bg='white').grid(row=0,columnspan=5,column=1)

    Label(frame1,text='First Name :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=1,column=1,sticky="e",padx=80)
    f_name = Entry(frame1,width=22,fg='#2B2B2B',bg='#EEEEEE',relief="flat",textvariable=f_nameinfo)
    f_name.grid(row=1,column=2,sticky="w",ipady=10)

    Label(frame1,text='Last Name :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=2,column=1,sticky="e",padx=80)
    l_name = Entry(frame1,width=22,fg='#2B2B2B',bg='#EEEEEE',relief="flat",textvariable=l_nameinfo)
    l_name.grid(row=2,column=2,sticky="w",ipady=10)

    Label(frame1,text='Phone :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=3,column=1,sticky="e",padx=80)
    p_num = Entry(frame1,width=22,fg='#2B2B2B',bg='#EEEEEE',relief="flat",textvariable=p_numinfo)
    p_num.grid(row=3,column=2,sticky="w",ipady=10)

    Label(frame1,text='Email :',font="Dosis 20 bold",bg='white',fg='#2B2B2B').grid(row=4,column=1,sticky="e",padx=80)
    email = Entry(frame1,width=22,fg='#2B2B2B',bg='#EEEEEE',relief="flat",textvariable=emailinfo)
    email.grid(row=4,column=2,sticky="w",ipady=10)

    Label(frame1,text='  Point:',image=scoin,fg='#2B2B2B',font="Dosis 20 bold",bg='white',compound=LEFT).grid(row=7,column=1,padx=30,sticky='e')
    count = Spinbox(frame1, from_=1, to=point,width=10,fg='#2B2B2B',bg='#EEEEEE',relief="flat",textvariable=pointinfo)
    count.grid(row=7,column=2,padx=30,ipady=10,sticky='w')    

    Button(frame1,text='Donate',bg="#B0DCF8",fg='#2B2B2B',font="Dosis 20 bold",width=10,relief="flat",command=donateclick).grid(row=7,column=3)
    Button(frame1,text='Back',bg="#B0DCF8",fg='#2B2B2B',font="Dosis 20 bold",width=10,relief="flat",command=menu2).grid(row=7,column=4)

def rewardclick():
    global point
    if address1info.get() == '':
        messagebox.showwarning("Admin" , "Enter Address1 First")
        address1.focus_force()
    elif address2info.get() == '':
        messagebox.showwarning("Admin" , "Enter Address2 First")
        address2.focus_force()
    elif cityinfo.get() == '':
        messagebox.showwarning("Admin" , "Enter city First")
        city.focus_force()
    elif postalinfo.get() == '':
        messagebox.showwarning("Admin" , "Enter Postal code First")
        postal.focus_force()
    elif phoneinfo.get() == '':
        messagebox.showwarning("Admin" , "Enter Phone number First")
        phone.focus_force()
    else:
        if point >= p_pd :
            point = point - p_pd
            Alladdress = address1info.get() +' '+ address2info.get() +' '+ cityinfo.get() +' '+ postalinfo.get()
            sql = '''insert into product ("user_id" , "p_name" , "u_address" , "u_phone", "product") values (?,?,?,?,?)'''
            cursor.execute(sql, [n_id,username,Alladdress,phoneinfo.get(),pd])
            conn.commit()

            sql = '''
                update user
                set point=?
                where n_card=?
            '''
            cursor.execute(sql, [point,n_id])
            conn.commit()
            messagebox.showinfo("Admin :" , "Redeem Successfully")
            address1.delete(0,END)
            address2.delete(0,END)
            city.delete(0,END)
            postal.delete(0,END)
            phone.delete(0,END)
            menu1()
        else :
            messagebox.showerror("Admin :" , "Redeem unsuccessful\nPlease check your point.")

def donateclick():
    global point
    if f_nameinfo.get() == '':
        messagebox.showwarning("Admin" , "Enter First name First")
        f_name.focus_force()
    elif l_nameinfo.get() == '':
        messagebox.showwarning("Admin" , "Enter Last name First")
        l_name.focus_force()
    elif p_numinfo.get() == '':
        messagebox.showwarning("Admin" , "Enter Phone number First")
        p_num.focus_force()
    elif emailinfo.get() == '':
        messagebox.showwarning("Admin" , "Enter E-mail First")
        email.focus_force()
    else:
        point = point - int(pointinfo.get())
        Allname = f_nameinfo.get() +' '+ l_nameinfo.get()
        sql = '''insert into donate ("user_id" , "d_name" , "d_phone" , "email", "donate", "count") values (?,?,?,?,?,?)'''
        cursor.execute(sql, [n_id,Allname,p_numinfo.get(),emailinfo.get(),dn,pointinfo.get()])
        conn.commit()
        sql = '''
            update user
            set point=?
            where n_card=?
        '''
        cursor.execute(sql, [point,n_id])
        conn.commit()
        messagebox.showinfo("Admin :" , "Donate Successfully")
        f_name.delete(0,END)
        l_name.delete(0,END)
        p_num.delete(0,END)
        email.delete(0,END)
        count.delete(0,END)
        menu2()


w = 1100 #width of application
h = 650 #height of application

createconnection()
root = mainwindow()

#product exchange
img_pd2 = PhotoImage(file='img_project/exercise bike.png').subsample(4,4)
img_pd3 = PhotoImage(file='img_project/ip13.png').subsample(7,7)
img_pd4 = PhotoImage(file='img_project/mi bot.png').subsample(3,3)
img_pd5 = PhotoImage(file='img_project/nike T-shirt.png').subsample(4,4)
img_pd6 = PhotoImage(file='img_project/diorpf.png').subsample(5,5)
img_pd7 = PhotoImage(file='img_project/xiaoperifeir.png').subsample(4,4)
img_pd8 = PhotoImage(file='img_project/sneaker.png').subsample(4,4)
img_pd9 = PhotoImage(file='img_project/marshall.png').subsample(3,3)
img01 = PhotoImage(file="login-pic.png")

#Donate
img_dn1 = PhotoImage(file='Donate/dn1.png').subsample(7,7)
img_dn2 = PhotoImage(file='Donate/dn2.png').subsample(6,6)
img_dn3 = PhotoImage(file='Donate/dn3.png').subsample(5,5)
img_dn4 = PhotoImage(file='Donate/dn4.png').subsample(5,5)
img_dn5 = PhotoImage(file='Donate/dn5.png').subsample(5,5)
img_dn6 = PhotoImage(file='Donate/dn6.png').subsample(7,7)
img_dn7 = PhotoImage(file='Donate/dn7.png').subsample(6,6)
img_dn8 = PhotoImage(file='Donate/dn8.png').subsample(6,6)

signinbtn = PhotoImage(file="sign-in-btn.png")
signoutbtn = PhotoImage(file="sign-out-btn.png").subsample(2,2)
redeembtn = PhotoImage(file="redeem-btn.png").subsample(2,2)
donatebtn = PhotoImage(file="donate-btn.png").subsample(2,2)
scoin = PhotoImage(file="scoin.png").subsample(8,8)

prof = PhotoImage(file="avataaars.png").subsample(4,4)
bgp = PhotoImage(file="point.png").subsample(2,2)

userinfo = StringVar()
pwdinfo = StringVar()

address1info = StringVar()
address2info = StringVar()
cityinfo = StringVar()
postalinfo = StringVar()
phoneinfo = StringVar()

f_nameinfo = StringVar()
l_nameinfo = StringVar()
p_numinfo = StringVar()
emailinfo = StringVar()
pointinfo = StringVar()


loginlayout()

root.mainloop()
cursor.close() #close cursor
conn.close() #close database connection