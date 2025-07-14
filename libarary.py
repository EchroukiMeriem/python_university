
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector as conn
import re
from tkcalendar import Calendar
import datetime

class libarary:
    def __init__(self):
        self.university = Toplevel()
        self.university.title("Students Information")
        self.university.geometry("1200x600")
        
        # Start frame
        self.frameleft = Frame(self.university, width=500)
        self.frameleft.pack(side=LEFT, fill=Y)
        self.frameright = Frame(self.university, width=700)
        self.frameright.pack(side=RIGHT, fill=Y)
        
        # Start inputs
        self.id_label = Label(self.frameleft, text="Id ", font=('Playfair Display', 10, 'bold'))
        self.id_label.place(x=10, y=30)
        self.namestudent_label = Label(self.frameleft, text="Name stdent ", font=('Playfair Display', 10, 'bold'))
        self.namestudent_label.place(x=10, y=70)
        self.cinstudent_label = Label(self.frameleft, text="CIN student", font=('Playfair Display', 10, 'bold'))
        self.cinstudent_label.place(x=10, y=110)
        self.email_label = Label(self.frameleft, text="Email", font=('Playfair Display', 10, 'bold'))
        self.email_label.place(x=10, y=150)
        self.namebook_label = Label(self.frameleft, text="Name Book ", font=('Playfair Display', 10, 'bold'))
        self.namebook_label.place(x=10, y=190)
        self.datedilaviry_label = Label(self.frameleft, text="Date Dilaviry ", font=('Playfair Display', 10, 'bold'))
        self.datedilaviry_label.place(x=10, y=240)
        self.datereturn_label = Label(self.frameleft, text="Date return ", font=('Playfair Display', 10, 'bold'))
        self.datereturn_label.place(x=10, y=350)
        
        self.id = StringVar()
        self.namestudent = StringVar()
        self.cinstudent = StringVar()
        self.email = StringVar()
        self.namebook= StringVar()
        self.datedilaviry= StringVar()
        self.datereturn= StringVar()
 
        
        self.id_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.id)
        self.id_entry.place(x=120, y=30, width=300, height=30)
        self.namestudent_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.namestudent)
        self.namestudent_entry.place(x=120, y=70, width=300, height=30)
        self.cinstudent_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.cinstudent)
        self.cinstudent_entry.place(x=120, y=110, width=300, height=30)
        self.email_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.email)
        self.email_entry.place(x=120, y=150, width=300, height=30)
        self.namebook_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.namebook)
        self.namebook_entry.place(x=120, y=190, width=300, height=30)
        # self.datedilaviry_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.datedilaviry)
        # self.datedilaviry_entry.place(x=120, y=150, width=300, height=30)
        # self.datereturn_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.datereturn)
        # self.datereturn_entry.place(x=120, y=150, width=300, height=30)
        # self.datedilaviry_entry=Calendar(self.frameleft,year = 2021,textvariable=self.datedilaviry,mindate=datetime.date.today())
        # self.datedilaviry_entry.place(x=120, y=230,width=200,height=200)
        # self.datereturn_entry = Calendar(self.frameleft,year = 2021,textvariable=self.datereturn)
        # self.datereturn_entry.place(x=120, y=340, width=200, height=200)
        self.datedilaviry_entry = Calendar(self.frameleft, year=2021, mindate=datetime.date.today())
        self.datedilaviry_entry.place(x=120, y=230, width=300, height=100)
        self.datereturn_entry = Calendar(self.frameleft, year=2021)
        self.datereturn_entry.place(x=120, y=450, width=300, height=100)
        # Start buttons
        self.addbtn = Button(self.frameleft, text="Add staff", command=self.add_libarary, bg="#1a7277", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.addbtn.place(x=10, y=480)
        self.updatebtn = Button(self.frameleft, text="Edit staff", bg="#011f4b", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.updatebtn.place(x=120, y=480)
        self.deletebtn = Button(self.frameleft, text="Delete staff", bg="#C40C0C", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.deletebtn.place(x=230, y=480)
        self.resetbtn = Button(self.frameleft, text="Reset staff", bg="#808080", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.resetbtn.place(x=360, y=480)
        self.showbtn = Button(self.frameleft, text="Show staff" , bg="#6f42c1", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.showbtn.place(x=490, y=480)
        
        # Frame for table view
        self.framecenter = Frame(self.frameright)
        self.framecenter.place(x=10, y=370, width=700, height=250)
        
        # Create Table
        self.tableview = ttk.Treeview(self.framecenter, columns=("Id", "Name student", "CIN student", "Email", "Name Book", "Date dilaviry","Date return"), show="headings")
        self.tableview.pack(fill=BOTH, expand=True)
        self.tableview.heading("Id", text="Id")
        self.tableview.heading("Name student", text="Name student")
        self.tableview.heading("CIN student", text="CIN student")
        self.tableview.heading("Email", text="Email")
        self.tableview.heading("Name Book", text="Name Book")
        self.tableview.heading("Date dilaviry", text="Date dilaviry")
        self.tableview.heading("Date return", text="Date return")
        self.tableview.column("Id", width=80)
        self.tableview.column("Name student", width=150)
        self.tableview.column("CIN student", width=150)
        self.tableview.column("Email", width=90)
        self.tableview.column("Name Book", width=110)
        self.tableview.column("Date dilaviry", width=80)
        self.tableview.column("Date return", width=80)
        self.tableview.bind("<ButtonRelease-1>", self.read_staff)
        self.show_staff()
        
        # Search section
        self.frametop = Frame(self.frameright, height=100)
        self.frametop.pack(fill=X)
        self.searchstaff = Entry(self.frametop, font=('Playfair Display', 10), width=55)
        self.searchstaff.grid(row=0, column=0, padx=10, pady=10)
        self.searchbtn = Button(self.frametop, command=self.search_staff, font=('Playfair Display', 10), text="Search", width=5, bg="#0056b3")
        self.searchbtn.grid(row=0, column=1, padx=10, pady=10)


        # Frame for displaying student info
        self.framebottom = Frame(self.frameright, height=300, bg="lightgray")
        self.framebottom.pack(fill=BOTH, expand=True)
        
        self.profile_image = Label(self.framebottom)
        self.profile_image.grid(row=0, column=0, padx=10, pady=10)
        
        self.staff_info = Label(self.framebottom, font=('Playfair Display', 10,'bold'),width=40,height=10)
        self.staff_info.grid(row=1, column=0, padx=10, pady=5, sticky=W)
    # Connect and add student
    def add_libarary(self):
        database = conn.connect(
            host="localhost",
            database="university",
            user="root",
            password=""
        )
        myconn = database.cursor()
        
        # Validate information (not empty)
        if (len(self.id_entry.get()) == 0 or len(self.namestudent_entry.get()) == 0 or len(self.cinstudent_entry.get()) == 0 or len(self.email_entry.get()) == 0 or len(self.namebook_entry.get()) == 0) or len(self.datedilaviry_entry.get()) == 0 or len(self.datereturn1_entry.get()) == 0:
            messagebox.showerror("Error", "All information is required")
        # Validate name (only letters and spaces)
        elif not re.match(r"^[A-Za-z\s]+$", self.namestudent_entry.get()):
            messagebox.showerror("Error", "Name must contain only letters and spaces")
        # Validate email
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
            messagebox.showerror("Error", "Invalid email format")
        else:
            sql = "INSERT INTO library(namestudent,cinstudent ,email, namebook,datedilaviry, datereturn) VALUES(NULL,%s, %s, %s, %s, %s, %s)"
            val = (
                self.namestudent_entry.get(),
                self.cinstudent_entry.get(),
                self.email_entry.get(),
                self.namebook_entry.get(),
                self.datedilaviry_entry.get(),
                self.datereturn.get()
            )
            myconn.execute(sql, val)
            database.commit()
            database.close()
            
            # Clear the entries after successful insertion
            self.namestudent_entry.delete(0, "end")
            self.cinstudent_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.namebook_entry.delete(0, "end")
            self.datedilaviry_entry.delete(0, "end")
            self.datereturn.set("Female")
            self.show_staff()
            self.reset_staff()
    
    # Show data
    def show_staff(self):
        database = conn.connect(
            host="localhost",
            database="university",
            user="root",
            password=""
        )
        myconn = database.cursor()
        sql = "SELECT * FROM stuff"
        myconn.execute(sql)
        results = myconn.fetchall()
        
        # Clear existing rows
        self.tableview.delete(*self.tableview.get_children())
        for result in results:
            self.tableview.insert('', 'end', values=result)
        database.commit()
        database.close()
    
    # Read data
#     def read_staff(self, event=None):
#         datastd = self.tableview.focus()
#         alldata = self.tableview.item(datastd)
#         value = alldata["values"]
        
#         # Check if value is not empty
#         if len(value) > 0:
#             self.cin.set(value[0])
#             self.nomcomplet.set(value[1])
#             self.email.set(value[2])
#             self.phone.set(value[3])
#             self.job.set(value[4])
#             self.gendervar.set(value[5])
    
#     # Edit student data
#     def edit_staff(self):
#         database = conn.connect(
#             host="localhost",
#             database="university",
#             user="root",
#             password=""
#         )
#         myconn = database.cursor()
#         sql = "UPDATE stuff SET nomcomplet=%s, email=%s, phone=%s, job=%s, gender=%s WHERE cin=%s"
#         val = (
#             self.nomcomplet_entry.get(),
#             self.email_entry.get(),
#             self.phone_entry.get(),
#             self.job_entry.get(),
#             self.gendervar.get(),
#             self.cin_entry.get()
#         )
#         myconn.execute(sql, val)
#         database.commit()
#         database.close()
#         self.show_staff()
#         self.reset_staff()
    
#     # Delete student data
#     def delete_staff(self):
#         database = conn.connect(
#             host="localhost",
#             database="university",
#             user="root",
#             password=""
#         )
#         myconn = database.cursor()
#         sql = "DELETE FROM stuff WHERE cin=%s"
#         val = (self.cin_entry.get(),)
#         myconn.execute(sql, val)
#         database.commit()
#         database.close()
        
#         # Clear the entries after successful deletion
#         self.cin_entry.delete(0, "end")
#         self.nomcomplet_entry.delete(0, "end")
#         self.email_entry.delete(0, "end")
#         self.phone_entry.delete(0, "end")
#         self.job_entry.delete(0, "end")
#         self.gendervar.set("Female")
#         self.show_staff()
#         self.reset_staff()
    
#     # Reset student entries
#     def reset_staff(self):
#         self.cin_entry.delete(0, "end")
#         self.nomcomplet_entry.delete(0, "end")
#         self.email_entry.delete(0, "end")
#         self.phone_entry.delete(0, "end")
#         self.job_entry.delete(0, "end")
#         self.gendervar.set("Female")
    
#     # Search student data and display profile
#     def search_staff(self):
#         database = conn.connect(
#             host="localhost",
#             database="university",
#             user="root",
#             password=""
#         )
#         myconn = database.cursor()
#         search_value = self.searchstaff.get()
#         sql = "SELECT * FROM stuff WHERE cin=%s OR nomcomplet LIKE %s OR phone=%s"
#         val = (search_value, f"%{search_value}%", search_value)
#         myconn.execute(sql, val)
#         results = myconn.fetchall()
        
#         # Clear existing rows
#         self.tableview.delete(*self.tableview.get_children())
#         if results:
#             for result in results:
#                 self.tableview.insert('', 'end', values=result)
#             self.display_profile(results[0])
#         else:
#             messagebox.showinfo("No Results", "No matching student found")
        
#         database.commit()
#         database.close()
# #   profike
#     def display_profile(self, staff_data):
#         self.cin, nomcomplet, email, phone, job, gender = staff_data
    
#     # Display the student's profile image based on gender
#         if gender == "female":
#             profile_image = Image.open("imageu/female.png")
#         else:
#             profile_image = Image.open("imageu/man.png")
    
#         profile_image = profile_image.resize((150, 150), Image.BICUBIC)
#         profile_photo = ImageTk.PhotoImage(profile_image)
#         self.profile_image.configure(image=profile_photo)
#         self.profile_image.image = profile_photo
    
#     # Display the student's information
#         staff_info_text = f"CIN: {self.cin}\nName: {nomcomplet}\nDate of Birth: {email}\nPhone: {phone}\nEmail: {job}\nGender: {gender}"
#         self.staff_info.configure(text=staff_info_text)
