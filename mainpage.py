from tkinter import *
from PIL import Image, ImageTk
import student as sru
import stuff as sff
import libarary as bibl
import exam as cntr
    
class University:
    def __init__(self,university ):
        self.university = university
        self.university.title("Gestion University")
        self.university.geometry("1920x1080")
        self.trt = Label(self.university, text="Gestion University", fg="#028391", font=('Playfair Display',50,'bold'))
        self.trt.pack()
        self.frames = Frame(self.university, height=350)
        self.frames.pack(fill=X)
# Infos students
        self.infosstudent = Frame(self.frames, padx=200, pady=80)
        self.infosstudent.grid(row=0, column=0)
        self.img = Image.open('imageu/student2.jpg')
        self.img.thumbnail((300, 300))
        self.img_new = ImageTk.PhotoImage(self.img)
        self.imgstudent = Label(self.infosstudent, image=self.img_new)
        self.imgstudent.pack()
        self.btnstudent = Button(self.infosstudent,font=('Playfair Display',10,'bold'), text="students University", bg="#028391", fg="white", padx=10, pady=10, command=self.openstudents)
        self.btnstudent.pack() 
# Infos stuffc
        self.infosstuff = Frame(self.frames, padx=400, pady=80)
        self.infosstuff.grid(row=0, column=1)
        self.img1 = Image.open("imageu/stuff.jpg")
        self.img1.thumbnail((250, 300))
        self.img1_new = ImageTk.PhotoImage(self.img1)
        self.imgstuff = Label(self.infosstuff, image=self.img1_new)
        self.imgstuff.pack()
        self.btnstuff = Button(self.infosstuff, text="stuff University",font=('Playfair Display',10,'bold'), bg="#028391", fg="white", padx=10, pady=10, command=self.openstuff)
        self.btnstuff.pack()

        self.frames2 = Frame(self.university, height=350)
        self.frames2.pack(fill=X)
        
 # Infos library
        self.infoslibrary = Frame(self.frames2, padx=200, pady=50)
        self.infoslibrary.grid(row=1, column=0)
        self.img3 = Image.open("imageu/library.jpg")
        self.img3.thumbnail((300, 250))
        self.img3_new = ImageTk.PhotoImage(self.img3)
        self.imglibrary = Label(self.infoslibrary, image=self.img3_new)
        self.imglibrary.pack()
        self.btnlibrary = Button(self.infoslibrary, text="Library University",font=('Playfair Display',10,'bold'), bg="#028391", fg="white", padx=10, pady=10 , command=self.openlibarary)
        self.btnlibrary.pack()

# Infos exam
        self.infosexam = Frame(self.frames2, padx=400, pady=40)
        self.infosexam.grid(row=1, column=1)
        self.img4 = Image.open("imageu/exam.jpg")
        self.img4.thumbnail((300,250))
        self.img4_new = ImageTk.PhotoImage(self.img4)
        self.imgexam = Label(self.infosexam, image=self.img4_new)
        self.imgexam.pack()
        self.btnexam = Button(self.infosexam, text="Exam University",font=('Playfair Display',10,'bold'), bg="#028391", fg="white", padx=10, pady=10, command=self.openexam)
        self.btnexam.pack()

    def openstudents(self):
        study=sru.student()
    
    def openstuff(self):
        stf=sff.stuff()
    
    def openlibarary(self):
        lbr=bibl.libarary()
    
    def openexam(self):
        xm=cntr.exam()


if __name__ == "__main__":
    window = Tk()
    university = University(window)
    window.mainloop()
