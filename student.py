
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector as conn
import re

class student:
    def __init__(self):
        self.university = Toplevel()
        self.university.title("Students Information")
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
        self.datebirth_label = Label(self.frameleft, text="Date of birth", font=('Playfair Display', 10, 'bold'))
        self.datebirth_label.place(x=10, y=110)
        self.phone_label = Label(self.frameleft, text="Phone", font=('Playfair Display', 10, 'bold'))
        self.phone_label.place(x=10, y=150)
        self.email_label = Label(self.frameleft, text="Email ", font=('Playfair Display', 10, 'bold'))
        self.email_label.place(x=10, y=190)
        
        self.cin = StringVar()
        self.nomcomplet = StringVar()
        self.datebirth = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.gendervar = StringVar()
        
        self.cin_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.cin)
        self.cin_entry.place(x=120, y=30, width=300, height=30)
        self.nomcomplet_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.nomcomplet)
        self.nomcomplet_entry.place(x=120, y=70, width=300, height=30)
        self.datebirth_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.datebirth)
        self.datebirth_entry.place(x=120, y=110, width=300, height=30)
        self.phone_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.phone)
        self.phone_entry.place(x=120, y=150, width=300, height=30)
        self.email_entry = Entry(self.frameleft, font=('Playfair Display', 10), textvariable=self.email)
        self.email_entry.place(x=120, y=190, width=300, height=30)
        
        self.gender_label = Label(self.frameleft, text="Gender ", font=('Playfair Display', 10, 'bold'))
        self.gender_label.place(x=10, y=230)
        self.female_rbtn = Radiobutton(self.frameleft, text="Female", variable=self.gendervar, value="Female", font=('Playfair Display', 10))
        self.female_rbtn.place(x=120, y=230)
        self.male_rbtn = Radiobutton(self.frameleft, text="Male", variable=self.gendervar, value="Male", font=('Playfair Display', 10))
        self.male_rbtn.place(x=190, y=230)
        self.gendervar.set("Female")
        
        # Start buttons
        self.addbtn = Button(self.frameleft, text="Add student", command=self.add_student, bg="#1a7277", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.addbtn.place(x=10, y=300)
        self.updatebtn = Button(self.frameleft, text="Edit student", command=self.edit_student, bg="#011f4b", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.updatebtn.place(x=120, y=300)
        self.deletebtn = Button(self.frameleft, text="Delete student", command=self.delete_student, bg="#C40C0C", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.deletebtn.place(x=230, y=300)
        self.reset_studentbtn = Button(self.frameleft, text="Reset student", command=self.reset_student, bg="#808080", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.reset_studentbtn.place(x=360, y=300)
        self.show_studentbtn = Button(self.frameleft, text="Show student", command=self.show , bg="#6f42c1", fg="white", font=('Playfair Display', 10), padx=10, pady=10)
        self.show_studentbtn.place(x=490, y=300)
        
        # Frame for table view
        self.framecenter = Frame(self.frameleft)
        self.framecenter.place(x=10, y=370, width=700, height=250)
        
        # Create Table
        self.tableview = ttk.Treeview(self.framecenter, columns=("CIN", "Name complet", "Date of birth", "Phone", "Email", "Gender"), show="headings")
        self.tableview.pack(fill=BOTH, expand=True)
        self.tableview.heading("CIN", text="CIN")
        self.tableview.heading("Name complet", text="Name complet")
        self.tableview.heading("Date of birth", text="Date of birth")
        self.tableview.heading("Phone", text="Phone")
        self.tableview.heading("Email", text="Email")
        self.tableview.heading("Gender", text="Gender")
        self.tableview.column("CIN", width=90)
        self.tableview.column("Name complet", width=150)
        self.tableview.column("Date of birth", width=90)
        self.tableview.column("Phone", width=90)
        self.tableview.column("Email", width=150)
        self.tableview.column("Gender", width=90)
        self.tableview.bind("<ButtonRelease-1>", self.read)
        self.show()
        
        # Search section
        self.frametop = Frame(self.frameright, height=100)
        self.frametop.pack(fill=X)
        self.searchstudent = Entry(self.frametop, font=('Playfair Display', 10), width=55)
        self.searchstudent.grid(row=0, column=0, padx=10, pady=10)
        self.searchbtn = Button(self.frametop, command=self.search_student, font=('Playfair Display', 10), text="Search", width=5, bg="#0056b3")
        self.searchbtn.grid(row=0, column=1, padx=10, pady=10)


        # Frame for displaying student info
        self.framebottom = Frame(self.frameright, height=300, bg="lightgray")
        self.framebottom.pack(fill=BOTH, expand=True)
        
        self.profile_image = Label(self.framebottom)
        self.profile_image.grid(row=0, column=0, padx=10, pady=10)
        
        self.student_info = Label(self.framebottom, font=('Playfair Display', 20,'bold'))
        self.student_info.grid(row=1, column=0, padx=60, pady=20, sticky=W)
    # Connect and add student
    def add_student(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        
        # Validate information (not empty)
        if (len(self.cin_entry.get()) == 0 or len(self.nomcomplet_entry.get()) == 0 or len(self.datebirth_entry.get()) == 0 or len(self.phone_entry.get()) == 0 or len(self.email_entry.get()) == 0):
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
            sql = "INSERT INTO students(cin, nomcomplet, datebirth, phone, email, gender) VALUES(%s, %s, %s, %s, %s, %s)"
            val = (
                self.cin_entry.get(),
                self.nomcomplet_entry.get(),
                self.datebirth_entry.get(),
                self.phone_entry.get(),
                self.email_entry.get(),
                self.gendervar.get()
            )
            myconn.execute(sql, val)
            database.commit()
            database.close()
            
            # Clear the entries after successful insertion
            self.cin_entry.delete(0, "end")
            self.nomcomplet_entry.delete(0, "end")
            self.datebirth_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.gendervar.set("Female")
            self.show()
            self.reset_student()
    
    # Show data
    def show(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        sql = "SELECT * FROM students"
        myconn.execute(sql)
        results = myconn.fetchall()
        
        # Clear existing rows in the tableview widget
        self.tableview.delete(*self.tableview.get_children())
        # Insert each result row into the tableview
        for result in results:
            self.tableview.insert('', 'end', values=result)
        database.commit()
        database.close()
    
    # Read data
    def read(self, event=None):
        datastd = self.tableview.focus()  # Get the selected row ID
        alldata = self.tableview.item(datastd)  # Get the data for the selected row
        value = alldata["values"]  # Extract the values from the row data
    
    # Check if the values list is not empty
        if len(value) > 0:
            self.cin.set(value[0])  # Set the cin variable
            self.nomcomplet.set(value[1])  # Set the nomcomplet variable
            self.datebirth.set(value[2])  # Set the datebirth variable
            self.phone.set(value[3])  # Set the phone variable
            self.email.set(value[4])  # Set the email variable
            self.gendervar.set(value[5])  # Set the gendervar variable
    
    # Edit student data
    def edit_student(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        sql = "UPDATE students SET nomcomplet=%s, datebirth=%s, phone=%s, email=%s, gender=%s WHERE cin=%s"
        val = (
            self.nomcomplet_entry.get(),
            self.datebirth_entry.get(),
            self.phone_entry.get(),
            self.email_entry.get(),
            self.gendervar.get(),
            self.cin_entry.get()
        )
        myconn.execute(sql,val)
        database.commit()
        database.close()
        self.show()
        self.reset_student()
    
    # Delete student data
    def delete_student(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        sql = "DELETE FROM students WHERE cin=%s"
        val = (self.cin_entry.get(),)
        myconn.execute(sql, val)
        database.commit()
        database.close()
        
        # Clear the entries after successful deletionn
        self.cin_entry.delete(0, "end")
        self.nomcomplet_entry.delete(0, "end")
        self.datebirth_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.gendervar.set("Female")
        self.show()
        self.reset_student()
    
    # Reset student entries
    def reset_student(self):
        self.cin_entry.delete(0, "end")
        self.nomcomplet_entry.delete(0, "end")
        self.datebirth_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.gendervar.set("Female")
    
    # Search student data and display profile
    def search_student(self):
        database = conn.connect(
            host="localhost",
            database="university2",
            user="root",
            password=""
        )
        myconn = database.cursor()
        # Get the search value from the GUI
        search_value = self.searchstudent.get()
        sql = "SELECT * FROM students WHERE cin=%s OR nomcomplet LIKE %s OR phone=%s"
        val = (search_value, f"%{search_value}%", search_value)
        myconn.execute(sql, val)
        results = myconn.fetchall()
        
        # Clear existing rows
        self.tableview.delete(*self.tableview.get_children())
        if results:
         # Display search results in the tableview
            for result in results:
                self.tableview.insert('', 'end', values=result)
            self.display_profile(results[0])
        else:
            messagebox.showinfo("No Results", "No matching student found")
        
        database.commit()
        database.close()
#   profike
    def display_profile(self, student_data):
        self.cin, self.nomcomplet, self.datebirth, self.phone, self.email, self.gender = student_data
    
    # Display the student's profile image based on gender
        if self.gender == "Female":
            profile_image = Image.open("imageu/female.png")
        else:
            profile_image = Image.open("imageu/man.png")
    # Resize the profile image
        profile_image = profile_image.resize((150, 150), Image.BICUBIC)
     # Convert the image to a format compatible with Tkinter
        profile_photo = ImageTk.PhotoImage(profile_image)
        self.profile_image.configure(image=profile_photo)
        self.profile_image.image = profile_photo
    
    # Display the student's information
        student_info_text = f"CIN: {self.cin}\nName: {self.nomcomplet}\nDate of Birth: {self.datebirth}\nPhone: {self.phone}\nEmail: {self.email}\nGender: {self.gender}"
        self.student_info.configure(text=student_info_text)
