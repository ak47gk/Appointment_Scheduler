import datetime
import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import pymysql
from PIL import Image, ImageTk

#giving a screen size
root = Tk()
root.geometry("650x700+0+0")
root.title("Patient/Doctor Scheduler")

def booknow():
    class Patient:
        def __init__(self, patient):
            self.root = patient
            self.root.title("Book an Appointment")
            self.root.geometry("500x600+0+0")

            # --------------------------------PatientData----------------------------------------
            first_name = Label(patient, text="First Name :", font='Verdana 10 bold')
            first_name.place(x=65, y=130)

            last_name = Label(patient, text="Last Name :", font='Verdana 10 bold')
            last_name.place(x=65, y=160)

            age = Label(patient, text="Age :", font='Verdana 10 bold')
            age.place(x=65, y=190)

            gender = Label(patient, text="Gender :", font='Verdana 10 bold')
            gender.place(x=65, y=220)

            city = Label(patient, text="City :", font='Verdana 10 bold')
            city.place(x=65, y=250)

            mail = Label(patient, text="E-mail :", font='Verdana 10 bold')
            mail.place(x=65, y=280)

            phone = Label(patient, text="Phone Number :", font='Verdana 10 bold')
            phone.place(x=65, y=310)

            address = Label(patient, text="Address :", font='Verdana 10 bold')
            address.place(x=65, y=340)

            reason = Label(patient, text="Reason for visit :", font='Verdana 10 bold')
            reason.place(x=65, y=370)
            # --------------------------------------EntryBox---------------------------------------------

            first_name = StringVar()
            last_name = StringVar()
            age = StringVar()
            city = StringVar()
            mail = StringVar()
            phone = StringVar()
            address = StringVar()
            reason = StringVar()

            first_name = Entry(patient, width=40, textvariable=first_name)
            first_name.place(x=200, y=133)

            last_name = Entry(patient, width=40, textvariable=last_name)
            last_name.place(x=200, y=163)

            age = Entry(patient, width=40, textvariable=age)
            age.place(x=200, y=193)

            gender = ttk.Combobox(patient, textvariable=gender, width=37, state='readonly')
            gender['values'] = ("", "male", "female")
            gender.place(x=200, y="223")

            city = Entry(patient, width=40, textvariable=city)
            city.place(x=200, y=253)

            mail = Entry(patient, width=40, textvariable=mail)
            mail.place(x=200, y=283)

            phone = Entry(patient, width=40, textvariable=phone)
            phone.place(x=200, y=313)

            address = Entry(patient, width=40, textvariable=address)
            address.place(x=200, y=343)

            reason = Entry(patient, width=40, textvariable=reason)
            reason.place(x=200, y=373)

            # -----------------------------------commands----------------------------------------------
            def action():
                if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or mail.get() == "" or phone.get() == "" or address.get() == "" or reason.get() == "":
                    messagebox.showerror("Error", "All Fields Are Required", parent=patient)
                else:
                    try:
                        con = pymysql.connect(host="localhost", user="root", password="", database="scheduler")
                        cur = con.cursor()
                        cur.execute("select * from patient_info where mail=%s", mail.get())
                        row = cur.fetchone()
                        if row is not None:
                            messagebox.showerror("Error", "You've already submitted a requested", parent=patient)
                        else:
                            cur.execute(
                                "insert into patient_info(first_name,last_name,age,gender,city,mail,phone,address,reason) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    first_name.get(),
                                    last_name.get(),
                                    age.get(),
                                    gender.get(),
                                    city.get(),
                                    mail.get(),
                                    phone.get(),
                                    address.get(),
                                    reason.get()
                                ))
                            con.commit()
                            clear()
                            con.close()

                            messagebox.showinfo("Success",
                                                "You'll receive an email where you'll get an appointment time and date. ",
                                                parent=patient)
                    except Exception as es:
                        messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=patient)

            # clear data function
            def clear():
                first_name.delete(0, END)
                last_name.delete(0, END)
                age.delete(0, END)
                gender.delete(0)
                city.delete(0, END)
                mail.delete(0, END)
                phone.delete(0, END)
                address.delete(0, END)
                reason.delete(0, END)

            # --------------------------------------buttons---------------------------------------------
            btn_confirm = Button(patient, text="Confirm", font='Verdana 10 bold', command=action)
            btn_confirm.place(x=200, y=413)

            btn_clear = Button(patient, text="Clear", font='Verdana 10 bold', command=clear)
            btn_clear.place(x=280, y=413)

    root = Tk()
    ob = Patient(root)
    root.mainloop()


image1=Image.open(r"C:\Users\UseR\Desktop\Appointment Scheduler\XYZloc.png")
map=ImageTk.PhotoImage(image1)
image2=Image.open(r"C:\Users\UseR\Desktop\Appointment Scheduler\XYZ.png").resize((150, 150), Image.ANTIALIAS)
logo=ImageTk.PhotoImage(image2)
image3=Image.open(r"C:\Users\UseR\Desktop\Appointment Scheduler\facebook.png").resize((30, 30), Image.ANTIALIAS)
facebook=ImageTk.PhotoImage(image3)
image4=Image.open(r"C:\Users\UseR\Desktop\Appointment Scheduler\twitter.png").resize((30, 30), Image.ANTIALIAS)
twitter=ImageTk.PhotoImage(image4)
def jumptobooknow():
    tabControl.select(3)
def jumptofacebook():
    webbrowser.open("http://facebook.com", new=1)
def jumptotwitter():
    webbrowser.open("http://twitter.com", new=1)

#creating tabs on main window
tabControl=ttk.Notebook(root)
tab1=ttk.Frame(tabControl)
tab2=ttk.Frame(tabControl)
tab3=ttk.Frame(tabControl)
tab4=ttk.Frame(tabControl)
tabControl.add(tab1, text="Home")
tabControl.add(tab2, text="Services")
tabControl.add(tab3, text="Contact US")
tabControl.add(tab4, text="BOOK NOW")
tabControl.pack(expand=1,fill='both')
ttk.Label(tab1,text="Welcome to the scheduler app of XYZ clinic\n"
               "You can easily book an appointment with Dr. XYZ using our scheduler app\n"
               "To know about the services we provide go to SERVICES option\n"
               "For location and other information got to CONTACT US option\n"
               "To book an appointment go to' \u2193").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab1,image=logo).grid(column=1,row=0)
buttonControl= Button(tab1, text="BOOK NOW", command=booknow).grid(column=0, row=1)
ttk.Label(tab2, text="1)Primary Doctor Care\n"
                     "We are primary care office that your first contact with an undiagonosed health concern\n"
                     "as well as continuing care of varied medical condition\n"
                     "\n"
                     "2)Physical Exam\n"
                     "We do all sorts of Physical Examination\n"
                     "\n"
                     "3)xyz\n"
                     "xyz").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab3,text="Find us at:\n").grid(column=0,row=0, sticky=W)
ttk.Label(tab3,image=map).grid(column=0,row=1)
ttk.Label(tab3,text="Call us at +88012345678910\n").grid(column=0,row=2, sticky=N)
ttk.Label(tab3,text="Follow Us on >>").grid(column=1,row=1, sticky=NE)
ttk.Label(tab3,text="E-mail: ").place(x=50,y=400)
ttk.Label(tab3,text="Name: ").place(x=50,y=450)
ttk.Entry(tab3,width=50).place(x=100,y=400)
ttk.Entry(tab3,width=50).place(x=100,y=450)
ttk.Entry(tab3).place(x=50,y=500,width=360,height=80)
buttonControl00= Button(tab3, text="Send").place(x=370,y=600)


buttonControl0= Button(tab3, image=facebook, command=jumptofacebook).grid(column=1, row=1)
buttonControl1= Button(tab3, image=twitter, command=jumptotwitter).grid(column=2, row=1)
buttonControl2= Button(tab4, text="Jump to Booking window", command=booknow).place(x=240,y=250)

def doctor():
    class Doctor:
        def __init__(self, doctor):
            self.root = doctor
            self.root.title("Management")
            self.root.geometry("1000x600+0+0")

            # --------------------AllVariables-------------------------------
            def fetch_data():
                con = pymysql.connect(host="localhost", user="root", password="", database="scheduler")
                cur = con.cursor()
                cur.execute("select first_name,age,city,phone,reason from patient_info")
                rows = cur.fetchall()
                if len(rows) != 0:
                    dategiving_table.delete(*dategiving_table.get_children())
                    for row in rows:
                        dategiving_table.insert("", END, values=row)
                        con.commit()
                    con.close()

            # ------------------------table1---------------------------------
            TABLE1 = Frame(self.root)
            TABLE1.place(x=0, y=0, width=600, height=600)

            table1_frame = Frame(TABLE1)
            table1_frame.place(x=0, y=0, width=600, height=500)

            scroll_x = Scrollbar(table1_frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(table1_frame, orient=VERTICAL)
            dategiving_table = ttk.Treeview(table1_frame, columns=("first_name", "age", "city", "phone", "reason"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=dategiving_table.yview)
            scroll_y.config(command=dategiving_table.xview)
            dategiving_table.heading("first_name", text="Name")
            dategiving_table.heading("age", text="Age")
            dategiving_table.heading("city", text="City")
            dategiving_table.heading("phone", text="Contact No")
            dategiving_table.heading("reason", text="Reason")
            dategiving_table.column("first_name", width=100)
            dategiving_table.column("age", width=30)
            dategiving_table.column("city", width=80)
            dategiving_table.column("phone", width=120)
            dategiving_table.column("reason", width=160)
            dategiving_table['show'] = 'headings'
            dategiving_table.pack(fill=BOTH, expand=1)
            fetch_data()

            # -------------------buttonActions------------------------------------
            btn_frame = Frame(TABLE1)
            btn_frame.place(x=150, y=500, width=400, height=100)

            confirmbtn = Button(btn_frame, text="Manage", command=self.manage, width=10).grid(row=0, column=0, padx=10,
                                                                                              pady=40)
            clearbtn = Button(btn_frame, text="Clear", width=10).grid(row=0, column=1, padx=10, pady=40)
            updatebtn = Button(btn_frame, text="Update", command=lambda:[fetch_data(),fetch()], width=10).grid(row=0, column=2, padx=10,
                                                                                            pady=40)

            # -----------------table2---------------------------------------
            TABLE2 = Frame(self.root)
            TABLE2.place(x=600, y=0, width=400, height=250)

            text = Label(TABLE2, text="Welcome Back Dr. XYZ,", font=("times new roman", 15, "bold"))
            text.grid(row=0, column=0, columnspan=3)
            today = Label(TABLE2, text="Today is:     ", font=("times new roman", 15, "bold"))
            today.grid(row=1, column=0)
            date = Label(TABLE2, text=datetime.date.today(), font=("times new roman", 15, "bold"))
            date.grid(row=1, column=1)

            # -----------------table3---------------------------------------

            def fetch():
                con = pymysql.connect(host="localhost", user="root", password="", database="scheduler")
                cur = con.cursor()
                cur.execute("select first_name,phone,start_time from patient_info")
                rows = cur.fetchall()
                if len(rows) != 0:
                    appointment_table.delete(*appointment_table.get_children())
                    for row in rows:
                        appointment_table.insert("", END, values=row)
                        con.commit()
                    con.close()

            TABLE3 = Frame(self.root)
            TABLE3.place(x=600, y=100, width=400, height=500)

            table3_frame = Frame(TABLE3, relief=RIDGE)
            table3_frame.place(x=00, y=0, width=400, height=500)

            scroll_x = Scrollbar(table3_frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(table3_frame, orient=VERTICAL)
            appointment_table = ttk.Treeview(table3_frame, columns=("first_name", "phone", "start_time"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=appointment_table.xview)
            scroll_y.config(command=appointment_table.yview)
            appointment_table.heading("first_name", text="Name")
            appointment_table.heading("phone", text="Contact No.")
            appointment_table.heading("start_time", text="Meeting Time")
            appointment_table.column("first_name", width=100)
            appointment_table.column("phone", width=150)
            appointment_table.column("start_time", width=120)
            appointment_table['show'] = 'headings'
            appointment_table.pack(fill=BOTH, expand=1)
            fetch()

        def manage(self):

            class Management:
                def __init__(self, Management):
                    self.root = Management
                    self.root.title("Management")
                    self.root.geometry("1200x600+0+0")

                    # --------------------------------PatientData----------------------------------------
                    serial = Label(Management, text="Serial :", font='Verdana 10 bold')
                    serial.place(x=65, y=100)

                    first_name = Label(Management, text="First Name :", font='Verdana 10 bold')
                    first_name.place(x=65, y=130)

                    last_name = Label(Management, text="Last Name :", font='Verdana 10 bold')
                    last_name.place(x=65, y=160)

                    age = Label(Management, text="Age :", font='Verdana 10 bold')
                    age.place(x=65, y=190)

                    gender = Label(Management, text="Gender :", font='Verdana 10 bold')
                    gender.place(x=65, y=220)

                    city = Label(Management, text="City :", font='Verdana 10 bold')
                    city.place(x=65, y=250)

                    mail = Label(Management, text="E-mail :", font='Verdana 10 bold')
                    mail.place(x=65, y=280)

                    phone = Label(Management, text="Phone Number :", font='Verdana 10 bold')
                    phone.place(x=65, y=310)

                    address = Label(Management, text="Address :", font='Verdana 10 bold')
                    address.place(x=65, y=340)

                    reason = Label(Management, text="Reason for visit :", font='Verdana 10 bold')
                    reason.place(x=65, y=370)

                    start_time = Label(Management, text="Starting time :", font='Verdana 10 bold')
                    start_time.place(x=600, y=220)

                    end_time = Label(Management, text="Ending :", font='Verdana 10 bold')
                    end_time.place(x=600, y=320)

                    # --------------------------------------EntryBox---------------------------------------------
                    id = StringVar()
                    serial = StringVar()
                    first_name = StringVar()
                    last_name = StringVar()
                    age = StringVar()
                    city = StringVar()
                    mail = StringVar()
                    phone = StringVar()
                    address = StringVar()
                    reason = StringVar()
                    start_time = StringVar
                    end_time = StringVar

                    id = Entry(Management, width=40, textvariable=id)
                    id.place(x=122200, y=133)

                    serial = ttk.Combobox(Management, textvariable=serial, width=37, state='readonly')
                    serial['values'] = (
                    "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16")
                    serial.place(x=200, y="103")

                    first_name = Entry(Management, width=40, textvariable=first_name)
                    first_name.place(x=200, y=133)

                    last_name = Entry(Management, width=40, textvariable=last_name)
                    last_name.place(x=200, y=163)

                    age = Entry(Management, width=40, textvariable=age)
                    age.place(x=200, y=193)

                    gender = ttk.Combobox(Management, textvariable=gender, width=37, state='readonly')
                    gender['values'] = ("", "male", "female")
                    gender.place(x=200, y="223")

                    city = Entry(Management, width=40, textvariable=city)
                    city.place(x=200, y=253)

                    mail = Entry(Management, width=40, textvariable=mail)
                    mail.place(x=200, y=283)

                    phone = Entry(Management, width=40, textvariable=phone)
                    phone.place(x=200, y=313)

                    address = Entry(Management, width=40, textvariable=address)
                    address.place(x=200, y=343)

                    reason = Entry(Management, width=40, textvariable=reason)
                    reason.place(x=200, y=373)

                    start_time = ttk.Combobox(Management, textvariable=start_time, width=37, state='readonly')
                    start_time['values'] = (
                    "", "8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "6:00", "6:30", "7:00",
                    "7:30", "8:00", "8:30", "9:00", "9:30")
                    start_time.place(x=735, y="223")

                    end_time = ttk.Combobox(Management, textvariable=end_time, width=37, state='readonly')
                    end_time['values'] = (
                    "", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "6:30", "7:00", "7:30",
                    "8:00", "8:30", "9:00", "9:30", "10:00")
                    end_time.place(x=735, y="323")

                    # -----------------------------------commands----------------------------------------------
                    def action():
                        if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or mail.get() == "" or phone.get() == "" or address.get() == "" or reason.get() == "":
                            messagebox.showerror("Error", "All Fields Are Required", parent=Management)
                        else:
                            try:
                                con = pymysql.connect(host="localhost", user="root", password="", database="scheduler")
                                cur = con.cursor()
                                cur.execute("select * from patient_info where mail=%s", mail.get())
                                row = cur.fetchone()
                                if row is not None:
                                    messagebox.showerror("Error", "You've already submitted a requested",
                                                         parent=Management)
                                else:
                                    cur.execute(
                                        "insert into patient_info(serial,first_name,last_name,age,gender,city,mail,phone,address,reason,start_time,end_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (

                                            serial.get(),
                                            first_name.get(),
                                            last_name.get(),
                                            age.get(),
                                            gender.get(),
                                            city.get(),
                                            mail.get(),
                                            phone.get(),
                                            address.get(),
                                            reason.get(),
                                            start_time.get(),
                                            end_time.get()
                                        ))
                                    con.commit()
                                    clear()
                                    con.close()

                                    messagebox.showinfo("Success",
                                                        parent=Management)
                            except Exception as es:
                                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=Management)

                    # clear data function

                    def clear():
                        id.delete(0, END)
                        serial.delete(0, END)
                        first_name.delete(0, END)
                        last_name.delete(0, END)
                        age.delete(0, END)
                        gender.delete(0)
                        city.delete(0, END)
                        mail.delete(0, END)
                        phone.delete(0, END)
                        address.delete(0, END)
                        reason.delete(0, END)
                        start_time.delete(0, END)
                        end_time.delete(0, END)
                        row_id = new_table.selection()
                        select = new_table.set(row_id)

                        id.insert(0, select['id'])
                        serial.insert(0, select['serial'])
                        first_name.insert(0, select['first_name'])
                        last_name.insert(0, select['last_name'])
                        age.insert(0, select['age'])
                        gender.insert(0, select['gender'])
                        city.insert(0, select['city'])
                        mail.insert(0, select['mail'])
                        phone.insert(0, select['phone'])
                        address.insert(0, select['address'])
                        reason.insert(0, select['reason'])
                        start_time.insert(0, select['start_time'])
                        end_time.insert(0, select['end_time'])


                    # --------------------------------------buttons---------------------------------------------
                    # btn_confirm = Button(Management, text="Confirm", font='Verdana 10 bold', command=action)
                    # btn_confirm.place(x=450, y=413)
                    #
                    # btn_clear = Button(Management, text="Clear", font='Verdana 10 bold', command=clear)
                    # btn_clear.place(x=550, y=413)

                    def update():
                        con = pymysql.connect(host="localhost", user="root", password="", database="scheduler")
                        cur = con.cursor()
                        cur.execute(
                            "update patient_info set serial=%s, first_name=%s,last_name=%s,age=%s,gender=%s,city=%s,mail=%s,phone=%s,address=%s,reason=%s,start_time=%s,end_time=%s where id=%s",
                            (
                                serial.get(),
                                first_name.get(),
                                last_name.get(),
                                age.get(),
                                gender.get(),
                                city.get(),
                                mail.get(),
                                phone.get(),
                                address.get(),
                                reason.get(),
                                start_time.get(),
                                end_time.get(),
                                id.get()
                            ))

                        fetch_data()
                        con.commit()
                        clear()
                        con.close()

                    def delete():
                        con = pymysql.connect(host="localhost", user="root", password="", database="scheduler")
                        cur = con.cursor()
                        cur.execute("delete from patient_info where serial=%s", serial.get())
                        con.commit()
                        con.close()
                        fetch_data()
                        clear()

                    def fetch_data():
                        con = pymysql.connect(host="localhost", user="root", password="", database="scheduler")
                        cur = con.cursor()
                        cur.execute("select  * from patient_info")
                        rows = cur.fetchall()
                        if len(rows) != 0:
                            new_table.delete(*new_table.get_children())
                            for row in rows:
                                new_table.insert("", END, values=row)
                                con.commit()
                            con.close()

                    def get_cursor(e):
                        clear()

                    TABLE4 = Frame(self.root)
                    TABLE4.place(x=0, y=0, width=1200, height=100)

                    table4_frame = Frame(TABLE4)
                    table4_frame.place(x=0, y=0, width=1200, height=100)

                    new_table = ttk.Treeview(table4_frame, columns=(
                    "id","serial", "first_name", "last_name", "age", "gender", "city", "mail", "phone", "address",
                    "reason", "start_time", "end_time"))

                    new_table.heading("id", text="id")
                    new_table.heading("serial", text="serial")
                    new_table.heading("first_name", text="first")
                    new_table.heading("last_name", text="last")
                    new_table.heading("age", text="age")
                    new_table.heading("gender", text="gender")
                    new_table.heading("city", text="city")
                    new_table.heading("mail", text="mail")
                    new_table.heading("phone", text="phone")
                    new_table.heading("address", text="address")
                    new_table.heading("reason", text="reason")
                    new_table.heading("start_time", text="Start")
                    new_table.heading("end_time", text="End")
                    new_table.column("id", width=5)
                    new_table.column("serial", width=40)
                    new_table.column("first_name", width=100)
                    new_table.column("last_name", width=100)
                    new_table.column("age", width=30)
                    new_table.column("gender", width=100)
                    new_table.column("city", width=80)
                    new_table.column("mail", width=100)
                    new_table.column("phone", width=120)
                    new_table.column("address", width=100)
                    new_table.column("reason", width=160)
                    new_table.column("address", width=100)
                    new_table.column("reason", width=160)
                    new_table.column("start_time", width=80)
                    new_table.column("end_time", width=80)

                    new_table['show'] = 'headings'
                    new_table.pack()
                    new_table.bind("<ButtonRelease-1>", get_cursor)
                    fetch_data()

                    btn_confirm = Button(Management, text="Update", font='Verdana 10 bold', command=update)
                    btn_confirm.place(x=450, y=413)

                    btn_clear = Button(Management, text="Refresh", font='Verdana 10 bold', command=fetch_data)
                    btn_clear.place(x=550, y=413)

                    updatebtn = Button(Management, text="Add", font='Verdana 10 bold', command=action, width=10).place(
                        x=370, y=460)
                    delbtn = Button(Management, text="Delete", font='Verdana 10 bold', command=delete, width=10).place(
                        x=490, y=460)
                    refbtn = Button(Management, text="Clear", font='Verdana 10 bold', command=clear, width=10).place(
                        x=610, y=460)

            root = Tk()
            ob = Management(root)
            root.mainloop()

    root = Tk()
    ob = Doctor(root)
    root.mainloop()



buttonControl4= Button(tab4, text="Jump to appointment window", command=doctor).place(x=235,y=285)



root.mainloop()
