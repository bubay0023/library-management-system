import time
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

root = Tk()

root.title("Library Management System")

##root.geometry("900X400")
root.resizable(0,0)
#bg = PhotoImage(file="pront_page.png")
#label1 = Label(root, image=bg)
#label1.pack()

class main:

    def __init__(self):

        bg = PhotoImage(file="pront_page.png")
        label1 = Label(root, image=bg)
        label1.pack()
        self.fm1 = Frame(root, height=300, width=300, bg='white',relief='sunken')
        self.fm1.place(x=100, y=180)
        self.top = Label(self.fm1,bg='#33B8FF', width=50,height=2)
        self.top.place(x=0,y=0)
        #user id
        self.b1 = Label(self.fm1, text='User ID :', font=('Arial', 10, 'bold'), fg='black',bg='white')
        self.b1.place(x=20, y=42)
        self.e1 = Entry(self.fm1, width=35, font=('arial', 10, 'bold'), bd=4, relief='groove')
        self.e1.place(x=22, y=65)
        #possword
        self.b2= Label(self.fm1, text="Possword :", font=('Arial', 10, 'bold'), fg='black',bg='white')
        self.b2.place(x=20, y=90 )
        self.e2= Entry(self.fm1, show="*", width=35,font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.e2.place(x=22, y=113)
        #login button

        self.btn1= Button(self.fm1,text="Log In", fg="black",bg='#33B8FF', width=30, font=("Arial",10,'bold'),
                          activebackground="#3399FF",activeforeground="black",bd=3,relief='raised',cursor='hand2',command=self.login)
        self.btn1.place(x=22,y=150)

        self.forgot = Label(self.fm1, text='Forgot Password?', fg='black', activeforeground='black',
                            font=('cursive', 11, 'bold'),cursor='hand2',bg='white')
        self.forgot.place(x=90, y=220)
        self.forgot.bind("<Button>",self.mouseclick)

        root.mainloop()

    def login(self):
        self.var1 = self.e1.get()
        self.var2 = self.e2.get()
        self.mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

        self.curA = self.mydb.cursor(buffered=True)
        query = ("SELECT * FROM users WHERE username=%s and password=%s")
        self.curA.execute(query, (self.var1, self.var2))
        self.mydb.commit()
        self.ab = self.curA.fetchone()
        self.mydb.close()

        if self.ab != None:
            self.under_fm = Frame(root, height=630, width=1205, bg='#fff')
            self.under_fm.place(x=0, y=0)
            self.fm2 = Frame(root,bg='#042546', height=40, width=1205)
            self.fm2.place(x=0, y=0)
            img = Image.open("book-41635.png")
            resize = img.resize((40, 30))
            icon1 = ImageTk.PhotoImage(resize)
            self.ll1 = Label(self.fm2,image=icon1,bg='#042546')
            self.ll1.image=icon1
            self.ll1.place(x=5,y=2)
            self.name2 = Label(self.fm2, text="Well Come "+self.ab[1], fg="white", bg='#042546', font=("Lumanosimo", 10, 'bold'))
            self.name2.place(x=55,y=10)
            logOut_ion = Image.open("log-out.png")
            logOut_ion_resize = logOut_ion.resize((20, 20))
            logOut_ion1 = ImageTk.PhotoImage(logOut_ion_resize)
            self.l_out = Label(self.fm2, image=logOut_ion1, bg='#042546',cursor='hand2')
            self.l_out.Image = logOut_ion1
            self.l_out.place(x=1100, y=5)
            self.l_out.bind("<Button>", self.logOut)
            self.l_out_b = Label(self.fm2, text="Log Out", fg="white", bg='#042546', font=("Arial", 10, 'bold'),
                              cursor='hand2')
            self.l_out_b.place(x=1120, y=5)
            self.l_out_b.bind("<Button>", self.logOut)

            self.side_bar()
            self.Dashboard(1)


        else:
            messagebox.showerror('Library System', 'Your ID or Password is invalid!')
    def side_bar(self):
        self.fm3 = Frame(root, bg='#0C457E', height=600, width=150)
        self.fm3.place(x=0, y=40)
        ion1 = Image.open("dashboard_icon.png")
        resize = ion1.resize((20,20))
        Ion1=ImageTk.PhotoImage(resize)
        self.ll2= Label(self.fm3,image=Ion1,bg='#0C457E')
        self.ll2.Image=Ion1
        self.ll2.place(x=10,y=10)
        self.btn2 = Label(self.fm3,text="Dashboard",fg="black",bg='#0C457E',font=("Arial",10,'bold'),cursor='hand2')
        self.btn2.place(x=35,y=12)
        self.btn2.bind("<Button>", self.Dashboard)
        ion2 = Image.open("books.png")
        resize1 = ion2.resize((20, 20))
        Ion2 = ImageTk.PhotoImage(resize1)
        self.ll3 = Label(self.fm3, image=Ion2, bg='#0C457E')
        self.ll3.Image = Ion2
        self.ll3.place(x=10, y=40)
        self.btn3 = Label(self.fm3, text="Add Books", fg="black", bg='#0C457E', font=("Arial", 10, 'bold'),
                          cursor='hand2')
        self.btn3.place(x=35, y=42)
        self.btn3.bind("<Button>", self.addbooks)
        ion3 = Image.open("student-20.png")
        Ion3 = ImageTk.PhotoImage(ion3)
        self.ll4 = Label(self.fm3, image=Ion3, bg='#0C457E')
        self.ll4.Image = Ion3
        self.ll4.place(x=10, y=70)
        self.btn4 = Label(self.fm3, text="Add Students", fg="black", bg='#0C457E', font=("Arial", 10, 'bold'),
                          cursor='hand2')
        self.btn4.place(x=35, y=72)
        self.btn4.bind("<Button>", self.add_students)

        self.book_arrow = Image.open("books-20.png")
        self.arrow_icon = ImageTk.PhotoImage(self.book_arrow)
        self.icon_arrow = Label(self.fm3, image=self.arrow_icon, bg='#0C457E')
        self.icon_arrow.image = self.arrow_icon
        self.icon_arrow.place(x=10, y=100)
        self.btn5 = Label(self.fm3, text="Books", fg="black", bg='#0C457E', font=("Arial", 10, 'bold'),
                          cursor='hand2')
        self.btn5.place(x=35, y=102)
        self.btn5.bind("<Button>", self.showbooks)
        self.student_arrow = Image.open("students-20.png")
        self.student_icon = ImageTk.PhotoImage(self.student_arrow )
        self.icon_student = Label(self.fm3, image=self.student_icon, bg='#0C457E')
        self.icon_student.image = self.student_icon
        self.icon_student.place(x=10, y=130)
        self.btn6 = Label(self.fm3, text="Students", fg="black", bg='#0C457E', font=("Arial", 10, 'bold'),
                          cursor='hand2')
        self.btn6.place(x=35, y=132)
        self.btn6.bind("<Button>", self.showstudents)

        self.student_pyment = Image.open("payment-20.png")
        self.payment_icon = ImageTk.PhotoImage(self.student_pyment)
        self.icon_payment = Label(self.fm3, image=self.payment_icon, bg='#0C457E')
        self.icon_payment.image = self.payment_icon
        self.icon_payment.place(x=10, y=160)
        self.btn7 = Label(self.fm3, text="Payment", fg="black", bg='#0C457E', font=("Arial", 10, 'bold'),
                          cursor='hand2')
        self.btn7.place(x=35, y=162)
        self.btn7.bind("<Button>", self.payment)

    def payment(self,event):
        self.payment_fm = Frame(root, height=590, width=1355, bg='#fff')
        self.payment_fm.place(x=150, y=40)
        self.payment_fm_date = Label(self.payment_fm, text="Date :", bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.payment_fm_date.place(x=900, y=0)
        self.payment_fm_date1 = Label(self.payment_fm, text=self.today, bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.payment_fm_date1.place(x=950, y=0)
        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h)>12 and int(m)>0:
                self.payment_fm_lb4.config(text="PM")

            self.payment_fm_lb1.config(text=h)
            self.payment_fm_lb2.config(text=m)
            self.payment_fm_lb3.config(text=s)
            self.payment_fm_lb1.after(200,clock)
            
        self.payment_fm_lb1 = Label(self.payment_fm, text='12', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.payment_fm_lb1.place(x=10, y=5)
        self.payment_fm_lb4 = Label(self.payment_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.payment_fm_lb4.place(x=30, y=3)
        self.payment_fm_lb2 = Label(self.payment_fm, text='05', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.payment_fm_lb2.place(x=40, y=5)
        self.payment_fm_lb5 = Label(self.payment_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.payment_fm_lb5.place(x=60, y=3)
        self.payment_fm_lb3 = Label(self.payment_fm, text='37', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.payment_fm_lb3.place(x=70, y=5)
        self.payment_fm_lb4 = Label(self.payment_fm, text='AM', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.payment_fm_lb4.place(x=100, y=5)
        clock()

        self.payment_fm1=Frame(self.payment_fm,bg='#fff',height=500,width=1355)
        self.payment_fm1.place(x=0,y=60)
        self.collegeidllb= Label(self.payment_fm1,text='College Id :',bg='#fff',font=('Arial',15,'bold'),fg='black')
        self.collegeidllb.place(x=20,y=10)
        self.collegeidllben=Entry(self.payment_fm1,width=15,bg='#fff',font=('Arial',15,'bold'))
        self.collegeidllben.place(x=142,y=10)
        self.findstudentdata = Button(self.payment_fm1, text="SEARCH", fg="white", bg='#0C15AA', width=15,
                                font=("Fira Sans", 10, 'bold'),
                                activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                cursor='hand2',command=self.feedetails)
        self.findstudentdata.place(x= 320,y=10)
    def feedetails(self):
        self.id = self.collegeidllben.get()
        if self.id != '':
            self.mydb2 = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

            self.curb2 = self.mydb2.cursor(buffered=True)
            query = ("SELECT * FROM students WHERE CollegeId=%s")
            self.curb2.execute(query, (self.id,))
            self.mydb2.commit()
            self.a2 = self.curb2.fetchone()
            if self.a2 != None:
                student = Frame(self.payment_fm1, height=400, width=500, bg='#fff', relief='groove', bd=2)
                student.place(x=100, y=50)
                studentop = Frame(student, height=30, width=495, bg="#0C15AA", relief='groove', bd=1)
                studentop.place(x=0, y=0)
                studentop_icon = Label(studentop, image=self.penciliconl1, bg="#0C15AA")
                studentop_icon.Image = self.penciliconl1
                studentop_icon.place(x=5, y=2)
                studentsdetails = Label(studentop, text="STUDENT DETAILS ", bg="#0C15AA", fg="white",
                          font=("Fira Sans", 10, "bold"))
                studentsdetails.place(x=30, y=3)
                studentName = Label(student, text="Name : " + self.a2[1].title(), bg="#fff", fg="#39393C",
                                         font=("Fira Sans", 10, "bold"))
                studentName.place(x=10, y=40)
                studentreg = Label(student, text="Registration Number : " + self.a2[0], fg="#39393C",
                                        bg="#fff",
                                        font=("Fira Sans", 10, 'bold'))
                studentreg.place(x=10, y=60)
                studentcourse = Label(student, text="Course : " + self.a2[2], fg="#39393C", bg="#fff",
                                           font=("Fira Sans", 10, 'bold'))
                studentcourse.place(x=10, y=80)
                studentseason = Label(student, text="Batch : " + self.a2[6], fg="#39393C",
                                           bg="#fff",
                                           font=("Fira Sans", 10, 'bold'))
                studentseason.place(x=10, y=100)
                studentNamber = Label(student, text="Contact No : " + self.a2[5], fg="#39393C",
                                           bg="#fff",
                                           font=("Fira Sans", 10, 'bold'))
                studentNamber.place(x=10, y=120)
                studentEmail = Label(student, text="Email : " + self.a2[4], fg="#39393C",
                                          bg="#fff",
                                          font=("Fira Sans", 10, 'bold'))
                studentEmail.place(x=10, y=140)
                studentfee = Label(student, text="Late Fee : \u20B9" + str(self.a2[10]), fg="black",
                                        bg="#fff",
                                        font=("Fira Sans", 10, 'bold'))
                studentfee.place(x=10, y=160)
                if self.a2[10]>0:
                    self.pay = Button(student, text="pay", fg="white", bg='#0C15AA', width=10,height=2,
                                font=("Fira Sans", 10, 'bold'),
                                activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                cursor='hand2',command=self.show_yes_no_popup)
                    self.pay.place(x=350,y=300)
                else:
                    self.pay = Button(student, text="pay", fg="white", bg='#B2ACAA', width=10, height=2,
                                      font=("Fira Sans", 10, 'bold'),
                                       bd=2, relief='raised',
                                      cursor='hand2')
                    self.pay.place(x=350, y=300)
            else:
                ion = Image.open("notfound.png")
                resize = ion.resize((400, 400))
                Ion1 = ImageTk.PhotoImage(resize)
                notfound = Label(self.payment_fm1, image=Ion1, bg='#fff')
                notfound.Image = Ion1
                notfound.place(x=0, y=50)
            self.mydb2.close()
        else:
            pass

    def show_yes_no_popup(self):
        self.result = messagebox.askyesno("Confirmation", "Do you want to proceed?")

        if self.result:
            self.feepay()
    def feepay(self):
        t_date=self.today
        #t_time=datetime.now().time()

        self.mydb3 = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')
        self.paycur= self.mydb3.cursor(buffered=True)
        query=("INSERT INTO payment (studentid, student_name, date, time, fee) VALUES (%s, %s, %s, NOW(), %s)")
        self.paycur.execute(query, (self.a2[0], self.a2[1], t_date, self.a2[10]))
        self.studentcur = self.mydb3.cursor(buffered=True)
        self.mydb3.commit()
        query1=('UPDATE students SET Charge=%s WHERE CollegeId =%s')
        self.studentcur.execute(query1, (0,self.a2[0]))
        self.mydb3.commit()
        self.mydb3.close()
        self.feedetails()


    def logOut(self,event):
        self.logoutfram= Frame(root,bg='#fff',height=600,width=1300)
        self.logoutfram.place(x=0,y=0)
        #self.under_fm.destroy()
        main()
        #self.code()

    def Dashboard(self,event):
        self.dashboard_fm = Frame(root, height=590, width=1355, bg='#fff')
        self.dashboard_fm.place(x=150,y=40)

        self.today = date.today()
        self.date = Label(self.dashboard_fm, text="Date :", bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date.place(x=900, y=0)
        self.date1 = Label(self.dashboard_fm, text=self.today, bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date1.place(x=950, y=0)

        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h)>12 and int(m)>0:
                self.lb4.config(text="PM")

            self.lb1.config(text=h)
            self.lb2.config(text=m)
            self.lb3.config(text=s)
            self.lb1.after(200,clock)

        self.lb1 = Label(self.dashboard_fm, text='12', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.lb1.place(x=10, y=5)
        self.lb4 = Label(self.dashboard_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.lb4.place(x=30, y=3)
        self.lb2 = Label(self.dashboard_fm, text='05', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.lb2.place(x=40, y=5)
        self.lb5 = Label(self.dashboard_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.lb5.place(x=60, y=3)
        self.lb3 = Label(self.dashboard_fm, text='37', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.lb3.place(x=70, y=5)
        self.lb4 = Label(self.dashboard_fm, text='AM', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.lb4.place(x=100, y=5)
        clock()

        self.dashboard_fm1 = Frame(self.dashboard_fm, height=70, width=250, bg="#E9812A")
        self.dashboard_fm1.place(x=30,y=50)
        def Bookcount():
            mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

            curA = mydb.cursor(buffered=True)
            query = ("select count(*) as BookId from books")
            curA.execute(query)
            mydb.commit()
            ab = curA.fetchone()
            mydb.close()
            self.booksCount.config(text=str(ab)[1])
        bookicon = Image.open("icons8-book-50.png")
        bookicon1=ImageTk.PhotoImage(bookicon)
        self.boil = Label(self.dashboard_fm1,image=bookicon1,bg="#E9812A")
        self.boil.Image = bookicon1
        self.boil.place(x=190,y=7)
        self.booksCount = Label(self.dashboard_fm1,text="0",bg="#E9812A",fg="white",font=("Arial",25,"bold"))
        self.booksCount.place(x=15,y=5)
        self.booksllb = Label(self.dashboard_fm1, text="Total Books", bg="#E9812A", fg="white", font=("Arial", 10, "bold"))
        self.booksllb.place(x=10, y=45)
        Bookcount()
        self.dashboard_fm2 = Frame(self.dashboard_fm, height=70, width=250, bg="#3550D8")
        self.dashboard_fm2.place(x=330, y=50)
        def studentcount():
            mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

            curA = mydb.cursor(buffered=True)
            query = ("select count(*) as CollegeId from students")
            curA.execute(query)
            mydb.commit()
            ab = curA.fetchone()
            mydb.close()
            self.studentCount.config(text=str(ab)[1])


        studenticon = Image.open("icons8-students-64.png")
        studenticon1 = ImageTk.PhotoImage(studenticon)
        self.stil = Label(self.dashboard_fm2, image=studenticon1, bg="#3550D8")
        self.stil.Image = studenticon1
        self.stil.place(x=180, y=3)

        self.studentCount = Label(self.dashboard_fm2, text="0", bg="#3550D8", fg="white", font=("Arial", 25, "bold"))
        self.studentCount.place(x=15, y=5)
        self.studentsllb = Label(self.dashboard_fm2, text="Students", bg="#3550D8", fg="white",
                              font=("Arial", 10, "bold"))
        self.studentsllb.place(x=10, y=45)
        studentcount()
        self.dashboard_fm3 = Frame(self.dashboard_fm, height=70, width=250, bg="#EEC32F")
        self.dashboard_fm3.place(x=630, y=50)

        usericon = Image.open("icons8-users-64.png")
        usericon1 = ImageTk.PhotoImage(usericon)
        self.uril = Label(self.dashboard_fm3, image=usericon1, bg="#EEC32F")
        self.uril.Image = usericon1
        self.uril.place(x=180, y=1)
        def usercount():
            mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

            curA = mydb.cursor(buffered=True)
            query = ("select count(*) as username from users")
            curA.execute(query)
            mydb.commit()
            ab = curA.fetchone()
            mydb.close()
            self.userCount.config(text=str(ab)[1])
        self.userCount = Label(self.dashboard_fm3, text="0", bg="#EEC32F", fg="white", font=("Arial", 25, "bold"))
        self.userCount.place(x=15, y=5)
        usercount()
        self.usersllb = Label(self.dashboard_fm3, text="Total Users", bg="#EEC32F", fg="white",
                                 font=("Arial", 10, "bold"))
        self.usersllb.place(x=10, y=45)


        self.studentsearch = Frame(self.dashboard_fm, height=250, width=300, bg='#fff',relief='groove',bd=2)
        self.studentsearch.place(x=100,y=200)
        self.studentsearchTop = Frame(self.studentsearch, height=30, width=296,bg="#0C15AA",relief='groove',bd=1)
        self.studentsearchTop.place(x=0,y=0)
        self.pencilicon = Image.open("icons8-pencil-64.png")
        self.pencilicoN = self.pencilicon.resize((20,20))
        self.penciliconl1 = ImageTk.PhotoImage(self.pencilicoN)
        self.pencilicon_l = Label(self.studentsearchTop, image=self.penciliconl1,bg="#0C15AA")
        self.pencilicon_l.Image = self.penciliconl1
        self.pencilicon_l.place(x=5,y=2)
        self.studentsearchTopll1 = Label(self.studentsearchTop, text="SEARCH STUDENT", bg="#0C15AA", fg="white",
                              font=("Fira Sans", 10, "bold"))
        self.studentsearchTopll1.place(x=30,y=3)
        self.studentregNo = Label(self.studentsearch,text="Registration Number", fg="#39393C",bg="#fff",
                              font=("Fira Sans", 10,'bold'))
        self.studentregNo.place(x=10,y=45)
        self.studentregNoen = Entry(self.studentsearch, width=37, font=('arial', 10, 'bold'), bd=3, relief='groove')
        self.studentregNoen.place(x=13,y=70)
        self.studentregName = Label(self.studentsearch, text="Student Name", fg="#39393C", bg="#fff",
                                  font=("Fira Sans", 10, 'bold'))
        self.studentregName.place(x=10,y=95)
        self.studentregNameen = Entry(self.studentsearch, width=37, font=('arial', 10, 'bold'), bd=3, relief='groove')
        self.studentregNameen.place(x=13, y=120)
        self.studentsearchbtn = Button(self.studentsearch, text="SUBMIT", fg="white", bg='#0C15AA', width=32, font=("Fira Sans", 10, 'bold'),
                           activebackground="#0C457E", activeforeground="black", bd=2, relief='raised', cursor='hand2',command=self.studentdata)
        self.studentsearchbtn.place(x=12,y=170)
    def studentdata(self):

        self.var3 = self.studentregNoen.get()
        self.var4 = self.studentregNameen.get()
        self.mydb1 = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

        self.curb = self.mydb1.cursor(buffered=True)
        query = ("SELECT * FROM students WHERE CollegeId=%s and Name=%s")
        self.curb.execute(query, (self.var3, self.var4.lower()))
        self.mydb1.commit()
        self.a = self.curb.fetchone()
        if self.a != None:
            if self.a[7] != None:
                date_difference = self.today - self.a[7]
                date_difference_in_days = date_difference.days
            #print(date_difference_in_days)
                if date_difference_in_days > 15 :
                    fine_days= self.today-self.a[8]
                    fine_days_in_days= fine_days.days
                    fine = fine_days_in_days*10

                    self.curfine = self.mydb1.cursor(buffered=True)
                    queryfine = ("UPDATE students SET Charge=%s WHERE CollegeID=%s")
                    self.curfine.execute(queryfine, (fine,self.var3))
                    self.mydb1.commit()

            bookcur1 = self.mydb1.cursor(buffered=True)
            query1 = ("SELECT COUNT(*) AS count_of_book FROM books WHERE CollageId=%s")
            bookcur1.execute(query1, (self.var3,))

            bookcount = bookcur1.fetchone()
            bookcur2 = self.mydb1.cursor(buffered=True)
            query3 = ("UPDATE students SET NoBook=%s WHERE CollegeID=%s")
            bookcur2.execute(query3, (int(bookcount[0]), self.var3))

            self.curbx = self.mydb1.cursor(buffered=True)
            query_data= ("SELECT * FROM students WHERE CollegeId=%s and Name=%s")
            self.curbx.execute(query_data, (self.var3, self.var4.lower()))
            self.mydb1.commit()
            self.ab1 = self.curbx.fetchone()


            self.student = Frame(self.dashboard_fm, height=400, width=500, bg='#fff',relief='groove',bd=2)
            self.student.place(x=500 , y=150)
            self.studentop = Frame(self.student,height=30,width=495,bg="#0C15AA",relief='groove',bd=1)
            self.studentop.place(x=0,y=0)
            self.studentop_icon = Label(self.studentop,image=self.penciliconl1,bg="#0C15AA")
            self.studentop_icon.Image = self.penciliconl1
            self.studentop_icon.place(x=5,y=2)
            self.studentsdetails = Label(self.studentop, text="STUDENT DETAILS ", bg="#0C15AA", fg="white",
                                         font=("Fira Sans", 10, "bold"))
            self.studentsdetails.place(x=30, y=3)
            self.studentName = Label(self.student, text="Name : "+self.ab1[1].title(), bg="#fff", fg="#39393C",
                                     font=("Fira Sans", 10, "bold"))
            self.studentName.place(x=10,y=40)
            self.studentreg = Label(self.student, text="Registration Number : "+self.ab1[0], fg="#39393C", bg="#fff",
                                  font=("Fira Sans", 10, 'bold'))
            self.studentreg.place(x=10,y=60)
            self.studentcourse = Label(self.student, text="Course : "+self.ab1[2], fg="#39393C", bg="#fff",
                                font=("Fira Sans", 10, 'bold'))
            self.studentcourse.place(x=10, y=80)
            self.studentseason = Label(self.student, text="Batch : "+self.ab1[6], fg="#39393C",
                                   bg="#fff",
                                   font=("Fira Sans", 10, 'bold'))
            self.studentseason.place(x=10, y=100)
            self.studentNamber = Label(self.student, text="Contact No : "+self.ab1[5], fg="#39393C",
                                   bg="#fff",
                                   font=("Fira Sans", 10, 'bold'))
            self.studentNamber.place(x=10, y=120)
            self.studentEmail = Label(self.student, text="Email : "+self.ab1[4], fg="#39393C",
                                   bg="#fff",
                                   font=("Fira Sans", 10, 'bold'))
            self.studentEmail.place(x=10, y=140)
            self.studentfee = Label(self.student, text="Late Fee : \u20B9"+str(self.ab1[10]), fg="black",
                                  bg="#fff",
                                  font=("Fira Sans", 10, 'bold'))
            self.studentfee.place(x=10, y=160)
            self.studentbook = Label(self.student, text="Books Issue : "+str(self.ab1[11]), fg="black",
                                    bg="#fff",
                                    font=("Fira Sans", 10, 'bold'))
            self.studentbook.place(x=10, y=180)


            if self.ab1[11] != 0:
                def toggle_visibility(widget):
                    if widget.cget("foreground") == "red":
                        widget.config(foreground="black")
                    else:
                        widget.config(foreground="red")
                    widget.after(500, lambda: toggle_visibility(widget))

                def apply_blinking_to_text_widgets(parent_widget):
                    for widget in parent_widget.winfo_children():
                        if isinstance(widget,Label):
                            toggle_visibility(widget)
                        elif isinstance(widget, Frame):
                            apply_blinking_to_text_widgets(widget)
                self.bookslist = Frame(self.student, height=90,width=430,bg="#fff")
                self.bookslist.place(x=50,y=200)
                self.curbook = self.mydb1.cursor(buffered=True)
                query_book_list = ("SELECT * FROM books WHERE CollageId=%s")
                self.curbook.execute(query_book_list, (self.var3,))
                self.mydb1.commit()
                self.issuebooklist = self.curbook.fetchall()
                n = 5
                for book in self.issuebooklist:
                    studentbook = Label(self.bookslist, text="* {} ({})   Renewal date :{}".format(book[1],book[0],self.ab1[8]), fg="red",
                                        bg="#fff",
                                        font=("Fira Sans", 10, 'bold'))
                    studentbook.place(x=10,y=n)
                    n += 20
                apply_blinking_to_text_widgets(self.bookslist)


            self.issuebooks = Button(self.student, text="ISSUE BOOKS", fg="white", bg='#0C15AA', width=15,
                                           font=("Fira Sans", 15, 'bold'),
                                           activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                           cursor='hand2',command=self.issuebook)
            self.issuebooks.place(x=25,y=320)

            self.returnbooks = Button(self.student, text="RETURN BOOKS", fg="white", bg='#0C15AA', width=15,
                                     font=("Fira Sans", 15, 'bold'),
                                     activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                     cursor='hand2',command=self.returnbook)
            self.returnbooks.place(x=280, y=320)

        else:
            messagebox.showerror('STUDENT','STUDENT NOT FOUND!')

        self.mydb1.close()

    def issuebook(self):
        if self.ab1[11] < 3:

            self.issbook_w = Tk()
            self.issbook_w.title(" Issue Book ")
            self.issbook_w.geometry("400x400+300+210")
            self.issbook_w.resizable(0,0)
            self.issbook_fm = Frame(self.issbook_w,height=400,width=400,bg="#fff")
            self.issbook_fm.place(x=0,y=0)
            self.booksearch = Label(self.issbook_fm, text="Books Id : ", fg="#39393C",
                                 bg="#fff",font=("Fira Sans", 11, 'bold'))
            self.booksearch.place(x=15,y=20)
            self.booken= Entry(self.issbook_fm, width=20, font=('arial', 10, 'bold'), bd=2, relief='groove')
            self.booken.place(x= 100,y=22)
            self.booksfind = Button(self.issbook_fm, text="SEARCH", fg="white", bg='#0C15AA', width=10,
                                  font=("Fira Sans", 8, 'bold'),
                                  activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                  cursor='hand2',command=self.bookfind)
            self.booksfind.place(x=270,y=20)
            self.issbook_w.mainloop()
        else:
            messagebox.showerror('STUDENT', 'STUDENT ALREADY REACHED MAXIMUM LIMIT !')
    def bookfind(self):
        self.var5 = self.booken.get()
        self.mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

        self.curc = self.mydb.cursor(buffered=True)
        query = ("SELECT * FROM books WHERE BookId = %s")
        self.curc.execute(query,(self.var5,))
        self.mydb.commit()
        self.ab3 = self.curc.fetchone()
        self.mydb.close()
        self.bookDetails = Frame(self.issbook_fm, height=340, width=400, bg="#fff")
        self.bookDetails.place(x=0, y=60)

        if self.ab3 != None:
            statue = "Not Issue"
            if self.ab3[5] != None:
                statue = "Issue"
            self.bookName = Label(self.bookDetails, text=" Book Name : " + self.ab3[1], bg="#fff", fg="#39393C",
                                     font=("Fira Sans", 10, "bold"))
            self.bookName.place(x=20, y=20)
            self.bookautherName = Label(self.bookDetails, text=" Auther : " + self.ab3[2], bg="#fff", fg="#39393C",
                                  font=("Fira Sans", 10, "bold"))
            self.bookautherName.place(x=20, y=40)
            self.bookedition = Label(self.bookDetails, text=" Edition: " + self.ab3[3], bg="#fff", fg="#39393C",
                                  font=("Fira Sans", 10, "bold"))
            self.bookedition.place(x=20, y=60)
            self.bookprice = Label(self.bookDetails, text=" Price : " + str(self.ab3[4]), bg="#fff", fg="#39393C",
                                  font=("Fira Sans", 10, "bold"))
            self.bookprice.place(x=20, y=80)
            self.bookprice = Label(self.bookDetails, text=" Status : " +statue, bg="#fff", fg="#39393C",
                                   font=("Fira Sans", 10, "bold"))
            self.bookprice.place(x=20, y=100)


            self.Issue = Button(self.bookDetails, text="ISSUE", fg="white", bg='#0C15AA', width=15,
                                    font=("Fira Sans", 10, 'bold'),
                                    activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                    cursor='hand2', command=self.issuconfirm)
            self.Issue.place(x=137 , y=280)


        else:
            self.bookAlete = Label(self.bookDetails, text=" OppS BooK not Found!  " , bg="#fff", fg="#39393C",
                                  font=("Fira Sans", 15, "bold"))
            self.bookAlete.place(x=80, y=100)

    def issuconfirm(self):

        self.mybook = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')
        self.bookcur = self.mybook.cursor(buffered=True)
        query=("UPDATE books SET Issue='Issued', CollageId=%s WHERE BookID=%s")
        self.bookcur.execute(query, (self.ab1[0],self.var5))
        self.mybook.commit()


        toDate = self.today + timedelta(days=15)
        self.formatted_date = toDate.strftime('%Y-%m-%d')
        print(self.today,toDate,self.formatted_date)
        self.bookcur3 = self.mybook.cursor(buffered=True)
        query4 = ("UPDATE students SET FromDate=%s,ToDate=%s WHERE CollegeID=%s")
        self.bookcur3.execute(query4, (self.today,self.formatted_date, self.ab1[0]))

        self.mybook.commit()
        self.mybook.close()
        messagebox.showerror('BOOK', 'BOOK SUCCESSFULLY ISSUE !!')
        self.studentdata()
        self.issbook_w.destroy()


    def returnbook(self):
        self.rebook_w = Tk()
        self.rebook_w.title(" Return Book ")
        self.rebook_w.geometry("600x200+300+210")
        self.rebook_w.resizable(0, 0)
        self.Return_fm = Frame(self.rebook_w, height=200, width=600, bg="#fff")
        self.Return_fm.place(x=0, y=0)
        self.book_search = Label(self.Return_fm, text="Books Id : ", fg="#39393C",
                                bg="#fff", font=("Fira Sans", 11, 'bold'))
        self.book_search.place(x=15, y=20)
        self.book_en = Entry(self.Return_fm, width=20, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.book_en.place(x=100, y=22)
        self.books_find = Button(self.Return_fm, text="SEARCH", fg="white", bg='#0C15AA', width=10,
                                font=("Fira Sans", 8, 'bold'),
                                activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                cursor='hand2',command=self.Removed_books)
        self.books_find.place(x=270, y=20)
        self.rebook_w.mainloop()

    def Removed_books(self):
        self.Return_fm1 = Frame(self.Return_fm, height=150, width=600, bg="#fff")
        self.Return_fm1.place(x=0,y=50)
        self.book = self.book_en.get()
        mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')
        curc = mydb.cursor(buffered=True)
        query = ("SELECT * FROM books WHERE BookId = %s AND CollageId=%s")
        curc.execute(query,(self.book,self.ab1[0]))
        mydb.commit()
        ab3 = curc.fetchone()
        mydb.close()
        if ab3 != None:
            bll1 = Label(self.Return_fm1,text="Book Id : ",fg="black",bg='#fff',font=("Arial",10,'bold'))
            bll1.place(x=30,y=10)
            bll2 = Label(self.Return_fm1, text=ab3[0],bg="#fff", fg="#39393C",
                                   font=("Fira Sans", 10, "bold"))
            bll2.place(x=100, y=10)
            bll3 = Label(self.Return_fm1, text="Name : ", fg="black", bg='#fff', font=("Arial", 10, 'bold'))
            bll3.place(x=30, y=30)
            bll4 = Label(self.Return_fm1, text=ab3[1], bg="#fff", fg="#39393C",
                         font=("Fira Sans", 10, "bold"))
            bll4.place(x=100, y=30)
            bll5 = Label(self.Return_fm1, text="Auther : ", fg="black", bg='#fff', font=("Arial", 10, 'bold'))
            bll5.place(x=30, y=50)
            bll6 = Label(self.Return_fm1, text=ab3[2], bg="#fff", fg="#39393C",
                         font=("Fira Sans", 10, "bold"))
            bll6.place(x=100, y=50)
            bll7 = Label(self.Return_fm1, text="Edition : ", fg="black", bg='#fff', font=("Arial", 10, 'bold'))
            bll7.place(x=30, y=70)
            bll8 = Label(self.Return_fm1, text=ab3[3], bg="#fff", fg="#39393C",
                         font=("Fira Sans", 10, "bold"))
            bll8.place(x=100, y=70)

            self.remove = Button(self.Return_fm1, text="REMOVE", fg="white", bg='#0C15AA', width=15,
                                font=("Fira Sans", 10, 'bold'),
                                activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                cursor='hand2',command=self.Removed_books_confirmed)
            self.remove.place(x=400, y=90)
        else:
            self.not_found = PhotoImage(file="not-verified.png")
            label1 = Label(self.Return_fm, image=self.not_found)
            label1.Image = label1
            label1.place(x=20, y=10)

    def Removed_books_confirmed(self):
        mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')
        curc = mydb.cursor(buffered=True)
        query = ("UPDATE books SET CollageId = NULL,Issue=NULL WHERE BookId = %s")
        curc.execute(query, (self.book,))


        mydb.commit()
        mydb.close()
        messagebox.showerror('BOOK', 'BOOK SUCCESSFULLY REMOVED !!')
        self.studentdata()
        self.rebook_w.destroy()
    def addbooks(self,event):
        self.addbook_fm = Frame(root, height=590, width=1355, bg='#fff')
        self.addbook_fm.place(x=150, y=40)
        self.date0 = Label(self.addbook_fm, text="Date :", bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date0.place(x=900, y=0)
        self.date2 = Label(self.addbook_fm, text = self.today, bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date2.place(x=950, y=0)

        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h)>12 and int(m)>0:
                self.alb4.config(text="PM")

            self.alb1.config(text=h)
            self.alb2.config(text=m)
            self.alb3.config(text=s)
            self.alb1.after(200,clock)

        self.alb1 = Label(self.addbook_fm, text='12', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb1.place(x=10, y=5)
        self.alb4 = Label(self.addbook_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.alb4.place(x=30, y=3)
        self.alb2 = Label(self.addbook_fm, text='05', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb2.place(x=40, y=5)
        self.alb5 = Label(self.addbook_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.alb5.place(x=60, y=3)
        self.alb3 = Label(self.addbook_fm, text='37', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb3.place(x=70, y=5)
        self.alb4 = Label(self.addbook_fm, text='AM', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb4.place(x=100, y=5)
        clock()

        def Bookcount():
            mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

            curA = mydb.cursor(buffered=True)
            query = ("select count(*) as BookId from books")
            curA.execute(query)
            mydb.commit()
            ab = curA.fetchone()
            mydb.close()
            self.booksCount1.config(text=str(ab)[1])

        self.addbook_fm1 = Frame(self.addbook_fm, height=70, width=250, bg="#E9812A")
        self.addbook_fm1.place(x=30, y=50)
        bookicon = Image.open("icons8-book-50.png")
        bookicon1 = ImageTk.PhotoImage(bookicon)
        self.boil1 = Label(self.addbook_fm1, image=bookicon1, bg="#E9812A")
        self.boil1.Image = bookicon1
        self.boil1.place(x=190, y=7)
        self.booksCount1 = Label(self.addbook_fm1, text="0", bg="#E9812A", fg="white", font=("Arial", 25, "bold"))
        self.booksCount1.place(x=15, y=5)
        self.booksllb1 = Label(self.addbook_fm1, text="Total Books", bg="#E9812A", fg="white",
                              font=("Arial", 10, "bold"))
        self.booksllb1.place(x=10, y=45)
        Bookcount()



        self.addbook1 = Frame(self.addbook_fm, height=390, width=700, bg='#fff', relief='groove', bd=2)
        self.addbook1.place(x=80, y=150)
        self.addbook1Top = Frame(self.addbook1, height=30, width=895, bg="#0C15AA", relief='groove', bd=1)
        self.addbook1Top.place(x=0, y=0)
        self.pencilicon_l1 = Label(self.addbook1Top, image=self.penciliconl1, bg="#0C15AA")
        self.pencilicon_l1.Image = self.penciliconl1
        self.pencilicon_l1.place(x=5, y=2)
        self.addbook1Topll1 = Label(self.addbook1Top, text="ADD BOOKS", bg="#0C15AA", fg="white",
                                         font=("Fira Sans", 10, "bold"))
        self.addbook1Topll1.place(x=30, y=3)

        self.BookId = Label(self.addbook1, text="Book Id : ", fg="#39393C", bg="#fff",
                                  font=("Fira Sans", 10, 'bold'))
        self.BookId.place(x=10, y=45)
        self.BookIden = Entry(self.addbook1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.BookIden.place(x=80, y=46)

        self.BookName = Label(self.addbook1, text="Book Name : ", fg="#39393C", bg="#fff",
                            font=("Fira Sans", 10, 'bold'))
        self.BookName.place(x=10, y=75)
        self.BookNameen = Entry(self.addbook1, width=50, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.BookNameen.place(x=105, y=76)

        self.BookAuthor = Label(self.addbook1, text="Book Author : ", fg="#39393C", bg="#fff",
                            font=("Fira Sans", 10, 'bold'))
        self.BookAuthor.place(x=10, y=105)
        self.BookAuthoren = Entry(self.addbook1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.BookAuthoren.place(x=110, y=106)

        self.BookEdition = Label(self.addbook1, text="Book Edition : ", fg="#39393C", bg="#fff",
                                font=("Fira Sans", 10, 'bold'))
        self.BookEdition.place(x=10, y=135)
        self.BookEditionen = Entry(self.addbook1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.BookEditionen.place(x=112, y=136)

        self.BookPrice = Label(self.addbook1, text="Book Price : ", fg="#39393C", bg="#fff",
                                 font=("Fira Sans", 10, 'bold'))
        self.BookPrice.place(x=10, y=165)
        self.BookPriceen = Entry(self.addbook1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.BookPriceen.place(x=100, y=166)

        self.Addbookbtn = Button(self.addbook1, text="ADD NOW", fg="white", bg='#0C15AA', width=32,
                                       font=("Fira Sans", 10, 'bold'),
                                       activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                       cursor='hand2',command=self.addBookNow)
        self.Addbookbtn.place(x=30, y=290)



    def addBookNow(self):
        self.Id = self.BookIden.get()
        self.Title = self.BookNameen.get()
        self.Author = self.BookAuthoren.get()
        self.Edition = self.BookEditionen.get()
        self.Price = self.BookPriceen.get()
        self.books = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')
        self.curser = self.books.cursor(buffered=True)
        query = ("SELECT * FROM books WHERE BookId=%s")
        self.curser.execute(query, (self.Id,))
        self.books.commit()
        self.tem1 = self.curser.fetchone()
        if self.tem1 == None:
            self.cur = self.books.cursor(buffered=True)
            query = ("SELECT * FROM books WHERE BookId=%s AND Title=%s AND Auther=%s AND Edition=%s")
            self.cur.execute(query, (self.Id, self.Title,self.Author,self.Edition))
            self.books.commit()
            self.tem = self.cur.fetchone()

            if self.tem == None:
                self.cur1 = self.books.cursor(buffered=True)
                query1 = ("INSERT INTO books (BookId, Title, Auther, Edition, Price) VALUES (%s, %s, %s, %s, %s )")
                self.cur1.execute(query1,(self.Id,self.Title,self.Author,self.Edition,int(self.Price)))
                self.books.commit()
                messagebox.showerror('BOOKS', 'THIS BOOK SUCCESFULLY ADD')
                self.addbooks(1)

            else:
                messagebox.showerror('BOOKS', 'THIS BOOK IS ALLREADY IN LIBRARY !!')
        else:
            messagebox.showerror('BOOKS', 'BOOK ID ALLREADY PRESEND !!')
        self.books.close()

    def add_students(self,event):
        self.addstudent_fm = Frame(root, height=590, width=1355, bg='#fff')
        self.addstudent_fm.place(x=150, y=40)
        self.date1 = Label(self.addstudent_fm, text="Date :", bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date1.place(x=900, y=0)
        self.date21 = Label(self.addstudent_fm, text=self.today, bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date21.place(x=950, y=0)
        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h)>12 and int(m)>0:
                self.alst4.config(text="PM")

            self.alst1.config(text=h)
            self.alst2.config(text=m)
            self.alst3.config(text=s)
            self.alst1.after(200,clock)
        self.alst1 = Label(self.addstudent_fm, text='12', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alst1.place(x=10, y=5)
        self.alst4 = Label(self.addstudent_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.alst4.place(x=30, y=3)
        self.alst2 = Label(self.addstudent_fm, text='05', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alst2.place(x=40, y=5)
        self.alst5 = Label(self.addstudent_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.alst5.place(x=60, y=3)
        self.alst3 = Label(self.addstudent_fm, text='37', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alst3.place(x=70, y=5)
        self.alst4 = Label(self.addstudent_fm, text='AM', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alst4.place(x=100, y=5)
        clock()

        def studentcount():
            mydb = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

            curA = mydb.cursor(buffered=True)
            query = ("select count(*) as CollegeId from students")
            curA.execute(query)
            mydb.commit()
            ab = curA.fetchone()
            mydb.close()
            self.studentCount1.config(text=str(ab)[1])

        self.addstudent_fm1 = Frame(self.addstudent_fm, height=70, width=250, bg="#3550D8")
        self.addstudent_fm1.place(x=30, y=50)
        studenticon = Image.open("icons8-students-64.png")
        studenticon1 = ImageTk.PhotoImage(studenticon)
        self.stoil1 = Label(self.addstudent_fm1, image=studenticon1, bg="#3550D8")
        self.stoil1.Image = studenticon1
        self.stoil1.place(x=180, y=5)
        self.studentCount1 = Label(self.addstudent_fm1, text="0", bg="#3550D8", fg="white", font=("Arial", 25, "bold"))
        self.studentCount1.place(x=15, y=5)
        self.studentsllb1 = Label(self.addstudent_fm1, text="Total Students", bg="#3550D8", fg="white",
                               font=("Arial", 10, "bold"))
        self.studentsllb1.place(x=10, y=45)
        studentcount()

        self.add_student1 = Frame(self.addstudent_fm, height=390, width=700, bg='#fff', relief='groove', bd=2)
        self.add_student1.place(x=180, y=150)
        self.add_student1Top = Frame(self.add_student1, height=30, width=696, bg="#0C15AA", relief='groove', bd=1)
        self.add_student1Top.place(x=0, y=0)
        self.pencilicon_l12 = Label(self.add_student1Top, image=self.penciliconl1, bg="#0C15AA")
        self.pencilicon_l12.Image = self.penciliconl1
        self.pencilicon_l12.place(x=5, y=2)
        self.add_student1Topll1 = Label(self.add_student1Top, text="ADD STUDENT", bg="#0C15AA", fg="white",
                                    font=("Fira Sans", 10, "bold"))
        self.add_student1Topll1.place(x=30, y=3)

        self.studentId = Label(self.add_student1, text="College Id : ", fg="#39393C", bg="#fff",
                            font=("Fira Sans", 10, 'bold'))
        self.studentId.place(x=10, y=45)
        self.studentIden = Entry(self.add_student1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.studentIden.place(x=100, y=46)

        self.studentName1 = Label(self.add_student1, text="Student Name : ", fg="#39393C", bg="#fff",
                               font=("Fira Sans", 10, 'bold'))
        self.studentName1.place(x=10, y=75)
        self.studentNameen = Entry(self.add_student1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.studentNameen.place(x=125, y=76)

        self.studentcourse = Label(self.add_student1, text="Course : ", fg="#39393C", bg="#fff",
                               font=("Fira Sans", 10, 'bold'))
        self.studentcourse.place(x=10, y=105)
        self.studentcourseen = Entry(self.add_student1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.studentcourseen.place(x=80, y=106)

        self.studentyear = Label(self.add_student1, text="Year : ", fg="#39393C", bg="#fff",
                               font=("Fira Sans", 10, 'bold'))
        self.studentyear.place(x=10, y=135)
        self.studentyearen = Entry(self.add_student1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.studentyearen.place(x=80, y=136)

        self.studentemail = Label(self.add_student1, text="Email : ", fg="#39393C", bg="#fff",
                               font=("Fira Sans", 10, 'bold'))
        self.studentemail.place(x=10, y=165)
        self.studentemailen = Entry(self.add_student1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.studentemailen.place(x=80, y=166)

        self.studentcontact = Label(self.add_student1, text="Contact No : ", fg="#39393C", bg="#fff",
                               font=("Fira Sans", 10, 'bold'))
        self.studentcontact.place(x=10, y=195)
        self.studentcontacten = Entry(self.add_student1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.studentcontacten.place(x=100, y=196)

        self.studentbatch = Label(self.add_student1, text="Batch : ", fg="#39393C", bg="#fff",
                                    font=("Fira Sans", 10, 'bold'))
        self.studentbatch.place(x=10, y=225)
        self.studentbatchen = Entry(self.add_student1, width=37, font=('arial', 10, 'bold'), bd=2, relief='groove')
        self.studentbatchen.place(x=80, y=226)

        self.Addstudentbtn = Button(self.add_student1, text="ADD NOW", fg="white", bg='#0C15AA', width=32,
                                 font=("Fira Sans", 10, 'bold'),
                                 activebackground="#0C457E", activeforeground="black", bd=2, relief='raised',
                                 cursor='hand2',command=self.addstudentnow)
        self.Addstudentbtn.place(x=350, y=320)

    def addstudentnow(self):
        self.collId = self.studentIden.get()
        self.student_Name = self.studentNameen.get()
        self.student_course = self.studentcourseen.get()
        self.student_year = self.studentyearen.get()
        self.student_email = self.studentemailen.get()
        self.student_contact = self.studentcontacten.get()
        self.batch = self.studentbatchen.get()

        if(self.student_course != "" and self.collId != "" and self.student_Name != "" and self.student_year != "" and self.student_email != "" and self.student_contact != "" ):
            self.studens = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')
            self.curser1 = self.studens.cursor(buffered=True)
            query = ("SELECT * FROM students WHERE CollegeId=%s")
            self.curser1.execute(query, (self.collId,))
            self.studens.commit()
            self.tem2 = self.curser1.fetchone()
            if self.tem2 == None:
                self.curstudent = self.studens.cursor(buffered=True)
                queryX = ("INSERT INTO students (CollegeId, Name, Course, year, Email, ContactNo, batch) VALUES (%s, %s, %s, %s, %s, %s, %s )")
                self.curstudent.execute(queryX, (self.collId, self.student_Name.lower(), self.student_course, int(self.student_year), self.student_email, self.student_contact, self.batch))
                self.studens.commit()
                messagebox.showerror('BOOKS', ('{} SUCCESFULLY ADD'.format(self.student_Name.split()[0])))
                self.add_students(1)
            else:
                messagebox.showerror('STUDEN', 'COLLEGE ID ALLREADY PRESENT !!')
            self.studens.close()

        else:
            messagebox.showerror('STUDEN', 'PLEASE FILL ALL THE BOXS !!')

    def mouseclick(self,event):
        self.forg_w=Tk()
        self.forg_w.title("Change Password")
        self.forg_w.geometry("300x300+300+210")
        self.forg_w.resizable(0,0)
        self.h1=Label(self.forg_w, text='User ID :', font=('Arial', 10, 'bold'), fg='black')
        self.h1.place(x=20,y=20)

        self.forg_w.mainloop()

    def showbooks(self,event):
        self.showbook_fm = Frame(root, height=590, width=1355, bg='#fff')
        self.showbook_fm.place(x=150, y=40)
        self.date_sh_fm = Label(self.showbook_fm, text="Date :", bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date_sh_fm.place(x=900, y=0)
        self.date2_sh_fm = Label(self.showbook_fm, text=self.today, bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date2_sh_fm.place(x=950, y=0)

        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h)>12 and int(m)>0:
                self.alb4_sh_fm.config(text="PM")

            self.alb1_sh_fm.config(text=h)
            self.alb2_sh_fm.config(text=m)
            self.alb3_sh_fm.config(text=s)
            self.alb1_sh_fm.after(200,clock)

        self.alb1_sh_fm = Label(self.showbook_fm, text='12', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb1_sh_fm.place(x=10, y=5)
        self.alb4_sh_fm = Label(self.showbook_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.alb4_sh_fm.place(x=30, y=3)
        self.alb2_sh_fm = Label(self.showbook_fm, text='05', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb2_sh_fm.place(x=40, y=5)
        self.alb5_sh_fm = Label(self.showbook_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.alb5_sh_fm.place(x=60, y=3)
        self.alb3_sh_fm = Label(self.showbook_fm, text='37', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb3_sh_fm.place(x=70, y=5)
        self.alb4_sh_fm = Label(self.showbook_fm, text='AM', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb4_sh_fm.place(x=100, y=5)
        clock()
        self.table_frame = Frame(self.showbook_fm, bd=1, relief='flat',height=553, width=1355, bg='#fff')
        self.table_frame.place(x=0,y=70)
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.book_table = ttk.Treeview(self.table_frame, columns=("Book ID", "Title", "Author", "Edition",
                                                                  "Price"),height=20,
                                       xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.book_table.xview)
        self.scroll_y.config(command=self.book_table.yview)
        self.book_table.heading("Book ID", text="Book ID")
        self.book_table.heading("Title", text="Title")
        self.book_table.heading("Author", text="Author")
        self.book_table.heading("Edition", text="Edition")
        self.book_table.heading("Price", text="Price")
        self.book_table['show'] = 'headings'
        self.book_table.column("Book ID", width=200)
        self.book_table.column("Title", width=350)
        self.book_table.column("Author", width=250)
        self.book_table.column("Edition", width=120)
        self.book_table.column("Price", width=110)

        self.book_table.pack(fill=BOTH, expand=1)

        self.book_list = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

        self.cur_book_list = self.book_list.cursor(buffered=True)
        query = ("select * from books")
        self.cur_book_list.execute(query)
        self.book_list.commit()
        self.sh_book = self.cur_book_list.fetchall()
        self.book_list.close()
        if len(self.sh_book) !=0 :
            for books in self.sh_book:
                self.book_table.insert('',END,values=books)
    def showstudents(self,event):
        self.showstudent_fm = Frame(root, height=590, width=1355, bg='#fff')
        self.showstudent_fm.place(x=150, y=40)
        self.date_sh_st_fm = Label(self.showstudent_fm, text="Date :", bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date_sh_st_fm.place(x=900, y=0)
        self.date2_sh_st_fm = Label(self.showstudent_fm, text=self.today, bg='#fff', fg='black', font=("calibri", 12, 'bold'))
        self.date2_sh_st_fm.place(x=950, y=0)

        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            if int(h) > 12 and int(m) > 0:
                self.alb4_sh_fm.config(text="PM")

            self.alb1_sh_st_fm.config(text=h)
            self.alb2_sh_st_fm.config(text=m)
            self.alb3_sh_st_fm.config(text=s)
            self.alb1_sh_st_fm.after(200, clock)

        self.alb1_sh_st_fm = Label(self.showstudent_fm, text='12', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb1_sh_st_fm.place(x=10, y=5)
        self.alb4_sh_st_fm = Label(self.showstudent_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.alb4_sh_st_fm.place(x=30, y=3)
        self.alb2_sh_st_fm = Label(self.showstudent_fm, text='05', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb2_sh_st_fm.place(x=40, y=5)
        self.alb5_sh_st_fm = Label(self.showstudent_fm, text=':', font=("Arial", 11, "bold"), bg='#fff', fg="black")
        self.alb5_sh_st_fm.place(x=60, y=3)
        self.alb3_sh_st_fm = Label(self.showstudent_fm, text='37', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb3_sh_st_fm.place(x=70, y=5)
        self.alb4_sh_st_fm = Label(self.showstudent_fm, text='AM', font=("Arial", 10, "bold"), bg='#fff', fg="black")
        self.alb4_sh_st_fm.place(x=100, y=5)
        clock()
        self.table_frame1 = Frame(self.showstudent_fm,height=550,width=100,bg='#fff')
        self.table_frame1.place(x=0,y=70)
        self.scroll_X = Scrollbar(self.table_frame1,orient=HORIZONTAL)
        self.scroll_Y = Scrollbar(self.table_frame1,orient=VERTICAL)
        self.student_table = ttk.Treeview(self.table_frame1,columns=("CollegeId",'Name','Course','Email',
                                                                     'ContactNo','batch','ToDate','Charge','NoBook')
                                          , height=20, xscrollcommand=self.scroll_X.set, yscrollcommand=self.scroll_Y.set)
        self.scroll_X.pack(side=BOTTOM,fill=X)
        self.scroll_Y.pack(side=RIGHT,fill=Y)
        self.scroll_X.config(command=self.student_table.xview)
        self.scroll_Y.config(command=self.student_table.yview)
        self.student_table.heading('CollegeId',text='College Id')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Course', text='Course')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('ContactNo', text='Contact No')
        self.student_table.heading('batch', text='Batch')
        self.student_table.heading('ToDate', text='Renewal')
        self.student_table.heading('Charge', text='Charge')
        self.student_table.heading('NoBook', text='NoBook')
        self.student_table['show'] = 'headings'
        self.student_table.column("CollegeId", width=80)
        self.student_table.column('Name', width=120)
        self.student_table.column('Course', width=240)
        self.student_table.column('Email', width=200)
        self.student_table.column('ContactNo', width=100)
        self.student_table.column('batch', width=70)
        self.student_table.column('ToDate', width=80)
        self.student_table.column('Charge', width=50)
        self.student_table.column('NoBook', width=50)

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_list = mysql.connector.connect(host="localhost", user='root', password='Sourav2002@', database='mydb')

        self.cur_student_list = self.student_list.cursor(buffered=True)
        query = ("select * from students")
        self.cur_student_list.execute(query)
        self.student_list.commit()
        self.sh_student = self.cur_student_list.fetchall()
        self.student_list.close()

        if len(self.sh_student) !=0 :
            for students in self.sh_student:
                self.student_table.insert('',END,values=(students[0],students[1].title(),students[2],students[4],students[5],students[6],students[8],students[10],students[11]))

if __name__=='__main__':
    login = main()
    #login.code()