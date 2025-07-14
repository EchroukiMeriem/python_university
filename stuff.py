
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector as conn
import re

class stuff:
    def __init__(self):
        self.university = Toplevel()
        self.university.title("Stuffs Information")
        self.university.geometry("1200x600")
        
        # Start frame
        self.frameleft = Frame(self.university, width=700)
        self.frameleft.pack(side=LEFT, fill=Y)
        self.frameright = Frame(self.university, width=500)
        self.frameright.pack(side=RIGHT, fill=Y)
        
        # Start inputs
        self.cin_label = Label(self.frameleft, text="CIN ", font=('Playfair Display', 10, 'bold'))
        self.cin_label.place(x=10, y=30)
        self.nomcomplet_label = Label(self.frameleft, text="Name complet ", font=('Playfair Display', 10, 'bold'))
        self.nomcomplet_label.place(x=10, y=70)
        self.email_label = Label(self.frameleft, text="Email", font=('Playfair Display', 10, 'bold'))
        self.email_label.place(x=10, y=110)
        self.phone_label = Label(self.frameleft, text="Phone", font=('Playfair Display', 10, 'bold'))
        self.phone_label.place(x=10, y=150)
        self.job_label = Label(self.frameleft, text="Job ", font=('Playfair Display', 10, 'bold'))
        self.job_label.place(x=10, y=190)
        
        self.cin = StringVar()
        self.nomcomplet = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.job = StringVar()
        self.gendervar = StringVar()
        
        self.cin_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.cin)
        self.cin_entry.place(x=120, y=30, width=300, height=30)
        self.nomcomplet_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.nomcomplet)
        self.nomcomplet_entry.place(x=120, y=70, width=300, height=30)
        self.email_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.email)
        self.email_entry.place(x=120, y=110, width=300, height=30)
        self.phone_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.phone)
        self.phone_entry.place(x=120, y=150, width=300, height=30)
        self.job_entry = ttk.Combobox(self.frameleft,values=["Faculty Members/Professors","Administrative Staff","Support Staff","Admissions Counselors","Library Staff","Human Resources"] ,font=('Playfair Display', 10), textvariable=self.job)
        self.job_entry.place(x=120, y=190, width=300, height=30)
        
        self.gender_label = Label(self.frameleft, text="Gender ", font=('Playfair Display', 10, 'bold'))
        self.gender_label.place(x=10, y=230)
        self.female_rbtn = Radiobutton(self.frameleft, text="Female", variable=self.gendervar, value="Female", font=('Playfair Display', 10))
        self.female_rbtn.place(x=120, y=230)
        self.male_rbtn = Radiobutton(self.frameleft, text="Male", variable=self.gendervar, value="Male", font=('Playfair Display', 10))
        self.male_rbtn.place(x=190, y=230)
        self.gendervar.set("Female")
        
        # Start buttons
        self.addbtn = Button(self.frameleft, text="Add staff", command=self.add_staff, bg="#1a7277", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.addbtn.place(x=10, y=300)
        self.updatebtn = Button(self.frameleft, text="Edit staff", command=self.edit_staff, bg="#011f4b", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.updatebtn.place(x=120, y=300)
        self.deletebtn = Button(self.frameleft, text="Delete staff", command=self.delete_staff, bg="#C40C0C", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.deletebtn.place(x=230, y=300)
        self.resetbtn = Button(self.frameleft, text="Reset staff", command=self.reset_staff, bg="#808080", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.resetbtn.place(x=360, y=300)
        self.showbtn = Button(self.frameleft, text="Show staff", command=self.show_staff , bg="#6f42c1", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.showbtn.place(x=490, y=300)
        
        # Frame for table view
        self.framecenter = Frame(self.frameleft)
        self.framecenter.place(x=10, y=370, width=700, height=250)
        
        # Create Table
        self.tableview = ttk.Treeview(self.framecenter, columns=("CIN", "Name complet", "Email", "Phone", "Job", "Gender"), show="headings")
        self.tableview.pack(fill=BOTH, expand=True)
        self.tableview.heading("CIN", text="CIN")
        self.tableview.heading("Name complet", text="Name complet")
        self.tableview.heading("Email", text="Email")
        self.tableview.heading("Phone", text="Phone")
        self.tableview.heading("Job", text="Job")
        self.tableview.heading("Gender", text="Gender")
        self.tableview.column("CIN", width=80)
        self.tableview.column("Name complet", width=150)
        self.tableview.column("Email", width=150)
        self.tableview.column("Phone", width=90)
        self.tableview.column("Job", width=110)
        self.tableview.column("Gender", width=80)
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
    def add_staff(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        
        # Validate information (not empty)
        if (len(self.cin_entry.get()) == 0 or len(self.nomcomplet_entry.get()) == 0 or len(self.email_entry.get()) == 0 or len(self.phone_entry.get()) == 0 or len(self.job_entry.get()) == 0):
            messagebox.showerror("Error", "All information is required")
        # Validate name (only letters and spaces)
        elif not re.match(r"^[A-Za-z\s]+$", self.nomcomplet_entry.get()):
            messagebox.showerror("Error", "Name must contain only letters and spaces")
        # Validate phone (only digits)
        elif not self.phone_entry.get().isdigit():
            messagebox.showerror("Error", "Phone number must contain only digits")
        # Validate email
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
            messagebox.showerror("Error", "Invalid email format")
        else:
            sql = "INSERT INTO stuff(cin, nomcomplet, email, phone, job, gender) VALUES(%s, %s, %s, %s, %s, %s)"
            val = (
                self.cin_entry.get(),
                self.nomcomplet_entry.get(),
                self.email_entry.get(),
                self.phone_entry.get(),
                self.job_entry.get(),
                self.gendervar.get()
            )
            myconn.execute(sql, val)
            database.commit()
            database.close()
            
            # Clear the entries after successful insertion
            self.cin_entry.delete(0, "end")
            self.nomcomplet_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
            self.job_entry.delete(0, "end")
            self.gendervar.set("Female")
            self.show_staff()
            self.reset_staff()
    
    # Show data
    def show_staff(self):
        database = conn.connect(
            host="localhost",
            database="university2",
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
    def read_staff(self, event=None):
        datastd = self.tableview.focus()  # Get the selected row ID
        alldata = self.tableview.item(datastd)  # Get the data for the selected row
        value = alldata["values"]  # Extract the values from the row data
    
    # Check if the values list is not empty
        if len(value) > 0:
            self.cin.set(value[0])  # Set the cin variable
            self.nomcomplet.set(value[1])  # Set the nomcomplet variable
            self.email.set(value[2])  # Set the datebirth variable
            self.phone.set(value[3])  # Set the phone variable
            self.job.set(value[4])  # Set the email variable
            self.gendervar.set(value[5])  # Set the gendervar variable
    
    # Edit student data
    def edit_staff(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        sql = "UPDATE stuff SET nomcomplet=%s, email=%s, phone=%s, job=%s, gender=%s WHERE cin=%s"
        val = (
            self.nomcomplet_entry.get(),
            self.email_entry.get(),
            self.phone_entry.get(),
            self.job_entry.get(),
            self.gendervar.get(),
            self.cin_entry.get()
        )
        myconn.execute(sql, val)
        database.commit()
        database.close()
        self.show_staff()
        self.reset_staff()
    
    # Delete student data
    def delete_staff(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        sql = "DELETE FROM stuff WHERE cin=%s"
        val = (self.cin_entry.get(),)
        myconn.execute(sql, val)
        database.commit()
        database.close()
        
        # Clear the entries after successful deletion
        self.cin_entry.delete(0, "end")
        self.nomcomplet_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.job_entry.delete(0, "end")
        self.gendervar.set("Female")
        self.show_staff()
        self.reset_staff()
    
    # Reset student entries
    def reset_staff(self):
        self.cin_entry.delete(0, "end")
        self.nomcomplet_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.job_entry.delete(0, "end")
        self.gendervar.set("Female")
    
    # Search student data and display profile
    def search_staff(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        search_value = self.searchstaff.get()
        sql = "SELECT * FROM stuff WHERE cin=%s OR nomcomplet LIKE %s OR phone=%s"
        val = (search_value, f"%{search_value}%", search_value)
        myconn.execute(sql, val)
        results = myconn.fetchall()
        
        # Clear existing rows
        self.tableview.delete(*self.tableview.get_children())
        if results:
            for result in results:
                self.tableview.insert('', 'end', values=result)
            self.display_profile(results[0])
        else:
            messagebox.showinfo("No Results", "No matching student found")
        
        database.commit()
        database.close()
#   profike
    def display_profile(self, staff_data):
        self.cin, self.nomcomplet, self.email, self.phone, self.job, self.gender = staff_data
    
    # Display the student's profile image based on gender
        if self.gender == "female":
            profile_image = Image.open("imageu/female.png")
        else:
            profile_image = Image.open("imageu/man.png")
    
        profile_image = profile_image.resize((150, 150), Image.BICUBIC)
        profile_photo = ImageTk.PhotoImage(profile_image)
        self.profile_image.configure(image=profile_photo)
        self.profile_image.image = profile_photo
    
    # Display the student's information
        staff_info_text = f"CIN: {self.cin}\nName: {self.nomcomplet}\nDate of Birth: {self.email}\nPhone: {self.phone}\nEmail: {self.job}\nGender: {self.gender}"
        self.staff_info.configure(text=staff_info_text)
