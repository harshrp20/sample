from tkinter import *
import sqlite3
import tkinter.messagebox
import os
import smtplib
import webbrowser

#######################################################################################################################################################################
#GLOBAL STUFF
try:
    conn=sqlite3.connect("test_1")
    #conn.execute("drop table t1")
    #conn.execute("drop table t2")
    #conn.execute("drop table t3")
    conn.execute("create table if not exists t1(name varchar(30),email varchar(30),phone varchar(15) primary key,gender varchar(15),donor varchar(5),doctor varchar(30))")
    #conn.execute("delete from t1")
    conn.execute("create table if not exists t2(name varchar(30),username varchar(30) primary key,password varchar(30))")
    #conn.execute("delete from t2")
    conn.execute("create table if not exists t3(pphone varchar(15),ndoctor varchar(30),diagnosis varchar(150));")
    #conn.execute("delete from t3")
    conn.commit()
    print("Blank Tables Created")
except Exception as a:
    print(a)
    conn.rollback()
    print("Blank Tables Not Created")
    conn.close()


#######################################################################################################################################################################
#MENUBAR
class Colour:
    col="Sky Blue"

def menumake1(root):
    menubar=Menu(root)
    root.config(menu=menubar)
    
    filemenu=Menu(menubar)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Quit",command=exit,font=("Lucida Handwriting",9,""))

def menumake(root,a):
    menubar=Menu(root)
    root.config(menu=menubar)
    
    filemenu=Menu(menubar)
    menubar.add_cascade(label="File",menu=filemenu,font=("Lucida Handwriting",9,""))
    filemenu.add_command(label="Back",command=a,font=("Lucida Handwriting",9,""))
    filemenu.add_separator()
    filemenu.add_command(label="Quit",command=exit,font=("Lucida Handwriting",9,""))

    editmenu=Menu(menubar)
    menubar.add_cascade(label="Edit",menu=editmenu)
    colourmenu=Menu(editmenu)
    editmenu.add_cascade(label="Colour Scheme",menu=colourmenu,font=("Lucida Handwriting",9,""))
    
    colourmenu.add_command(label="Sky Blue",command=b,font=("Lucida Handwriting",9,""))
    colourmenu.add_separator()
    colourmenu.add_command(label="Navy Blue",command=c,font=("Lucida Handwriting",9,""))

    menubar.add_command(label="SignOut",command=d)

def b():
    Colour.col="Sky Blue"
def c():
    Colour.col="Navy Blue"
def d():
    try:
        rootnpw.destroy()
    except Exception as e:
        print(e)
    try:
        rootph.destroy()
    except Exception as e:
        print(e)
    try:
        rootpd.destroy()
    except Exception as e:
        print(e)
    try:
        rootsu.destroy()
    except Exception as e:
        print(e)
    try:
        rootdp.destroy()
    except Exception as e:
        print(e)
    loginPage()
        

#######################################################################################################################################################################
#NEW PATIENT ENTRY
def newPatient():
    global rootnpw
    rootnpw=Tk()
    rootnpw.title("New Patient Record")
    rootnpw.resizable(width=False,height=False)
    menumake(rootnpw,npw_back)
    
    radiodata=IntVar()
    checkdata=IntVar()  
    
    npwl1=Label(rootnpw,text="Full Name:",padx=2).grid(row=0,column=0,sticky=W)
    npwe1=Entry(rootnpw,width=50)
    npwe1.grid(row=0,column=1,columnspan=3,padx=2)

    npwl2=Label(rootnpw,text="Email:",padx=2).grid(row=1,column=0,sticky=W)
    npwe2=Entry(rootnpw,width=50)
    npwe2.grid(row=1,column=1,columnspan=3,padx=2)
    
    npwl3=Label(rootnpw,text="Phone Number:",padx=2).grid(row=2,column=0,sticky=W)
    npwe3=Entry(rootnpw,width=50)
    npwe3.grid(row=2,column=1,columnspan=3,padx=2)

    npwl4=Label(rootnpw,text="Gender:",padx=2).grid(row=3,column=0,sticky=W)

    npwr1=Radiobutton(rootnpw,text="Male",variable=radiodata,value=0)
    npwr1.grid(row=3,column=1)
    npwr2=Radiobutton(rootnpw,text="Female",variable=radiodata,value=1)
    npwr2.grid(row=3,column=2)
    npwr3=Radiobutton(rootnpw,text="Transgender",variable=radiodata,value=2)
    npwr3.grid(row=3,column=3)
    
    try:
        load=open("dimage1.png")
        image_d=PhotoImage(load)
        npwl5=Label(rootnpw,image=image_d,padx=2)
        npwl5.image=im_d
        npwl5.grid(row=4,column=0,sticky=W,rowspan=2,columnspan=2)
           
        image_d=PhotoImage(file='dimage1.gif')
        npwl5=Label(rootnpw,image=image_d,padx=2).grid(row=4,column=0,sticky=W,rowspan=2,columnspan=2)

    except Exception as e:
        print(e)
    
    npwc1=Checkbutton(rootnpw, text="Organ Donor",variable=checkdata,onvalue=0,offvalue=1)
    npwc1.grid(row=4,column=2,columnspan=1,rowspan=2,sticky=W)
    npwb1=Button(rootnpw,text="Submit",command=lambda: npw_click1(npwe1.get(),npwe2.get(),npwe3.get(),checkdata.get(),radiodata.get())).grid(row=4,column=3,rowspan=2,columnspan=1,sticky=W+N+E+S,padx=1,pady=1)
    
    rootnpw.mainloop()

def npw_click1(npwd1,npwd2,npwd3,checkdata,radiodata):
    global gend_d
    if npwd1!="":
        print(npwd1)
    if npwd2!="":
        print(npwd2)
    if npwd3!="":
        print(npwd3)
    try:
        if str(checkdata)=='1':
            od_d="No"
            print("Not Organ Donor")
        elif str(checkdata)=='0':
            od_d="Yes"
            print("Organ Donor")
        else:
            print(checkdata)
            print("Not Known")
        print(str(radiodata))
        radiodata1="3"
        if str(radiodata)=='0':
            radiodata1="Male"
            print("Male")
        elif str(radiodata)=='1':
            print("Female")
            radiodata1="Female"
        elif str(radiodata)=='2':
            print("Transgender")
            radiodata1="Transgender"
        else:
            pass
    except Exception as e:
        print(e)
    try:
        conn=sqlite3.connect("test_1")
        conn.execute("insert into t1 values('%s','%s','%s','%s','%s','%s')"%(npwd1,npwd2,npwd3,radiodata1,od_d,Doctor.name))
        conn.commit()
        conn.close()
        print("Complete Insert Done")
        npw_back()
    except NameError:
        try:
            print("Pending")
            conn=sqlite3.connect("test_1")
            conn.execute("insert into t1 values('%s','%s','%s','%s','%s','%s')"%(npwd1,npwd2,npwd3,'DATA NOT AVAILABLE',"Not Organ Donor",Doctor.name))
            conn.commit()
            conn.close()
            print("Insert Done")
            npw_back()
        except sqlite3.IntegrityError as e:
            tkinter.messagebox.showerror("SQL Integrity Error",str.upper(str(e)))
            print(e)
            conn.close()
        except Exception as e:
            conn.rollback()
            print("Pending")
            print(e)
            conn.close()
            print("Insert Not Done")
            npw_back()
    except sqlite3.IntegrityError as e:
        tkinter.messagebox.showerror("SQL Integrity Error",str.upper(str(e)))
        print(e)
        conn.close()
    except Exception as e:
        conn.rollback()
        print("Insert Not Done")
        print(e)
        conn.close()
        npw_back()
            
def npw_back():
    rootnpw.destroy()
    patientHistory()

    
#######################################################################################################################################################################
#PATIENT SEARCH WINDOW
def patientHistory():
    global rootph
    rootph=Tk()
    rootph.title("Search Patient Details")
    rootph.resizable(width=False,height=False)
    menumake(rootph,ph_back)
    
    phl0=Label(rootph,text="Search For Patient Details",fg=Colour.col,font=("Lucida Calligraphy", 11, "bold underline"),anchor=CENTER,padx=4,pady=2)
    phl0.grid(row=0,column=0,columnspan=3,pady=5,sticky=W+N+E+S)
    
    phl1=Label(rootph,text="Patient's Phone Number:").grid(row=1,column=0,sticky=W)

    phdata1=StringVar()
    phe1=Entry(rootph,width=40)
    phe1.grid(row=1,column=1,columnspan=2,padx=1,sticky=W+N+E+S)
    
    phb1=Button(rootph,text="Search",command=lambda: phb1_click(phe1.get())).grid(row=2,column=0,columnspan=3,sticky=W+N+E+S)
    #phb2=Button(rootph,text="Current Patient",width=40).grid(row=3,column=0,columnspan=2)
    phb3=Button(rootph,text="ADD NEW PATIENT",font=("Times New Roman",9,"bold"),bd=0)
    phb3.bind("<ButtonPress-1>",phb3_click)
    phb3.grid(row=3,column=0,columnspan=3,sticky=W+N+E+S)

    rootph.mainloop()
    
def rootph_hide():
    rootph.withdraw()
def rootph_destroy():
    rootph.destroy()
def ph_back():
    rootph.destroy()
    doctorPage()

def phb1_click(phdata1):
    try:
        phdata1_str=phdata1
        print("Search Key=",phdata1_str)
        conn=sqlite3.connect("test_1")
        c=conn.cursor()
        c=conn.execute("select distinct * from t1 where phone='%s' and doctor='%s';"%(phdata1_str,Doctor.name))

        name1="Value Not Given"
        email1="Value Not Given"
        phone1="Value Not Given"
        gender1="Value Not Given"
        donor1="Value Not Given"
        doctor1="Value Not Given"
        count=0

        for row in c:
            count+=1
            #global name1
            name1 = row[0]
            if name1 is None:
                name1="Value Not Given"
            #global email1
            email1 = row[1]
            if email1 is None:
                email1="Value Not Given"
            #global phone1            
            phone1 = row[2]
            if phone1 is None:
                phone1="Value Not Given"
            #global gender1
            gender1 = row[3]
            if gender1 is None:
                gender1="Value Not Given"
            #global donor1
            donor1 = row[4]
            if donor1 is None:
                donor1="Value Not Given"
            doctor1 = row[5]
            if doctor1 is None:
                doctor1="Value Not Given"
            print(name1,email1,phone1,gender1,donor1,doctor1,sep='\n')
        if count==0:
            #print(name1,email1,phone1,gender1,donor1,doctor1,sep='\n')
            tkinter.messagebox.showerror("Invalid","Invalid Patient Number")
            print("Invalid Phone Number")
        else:
            print("Patient Data Extracted")
            rootph_hide()
            patientDetails(name1,email1,phone1,gender1,donor1,doctor1)
        conn.close()
    except Exception as e:
        conn.rollback()
        print("NO EXTRACT")
        print(e)
        conn.close()

def phb3_click(c):
    rootph.destroy()
    newPatient()

    
#######################################################################################################################################################################
#PATIENT DETAILS
def patientDetails(name1,email1,phone1,gender1,donor1,doctor1):
    global rootpd
    rootpd=Tk()
    rootpd.title("Patient Details")
    menumake(rootpd,pd_back)
    '''
    pdd1=StringVar()
    pdd2=StringVar()
    pdd3=StringVar()
    #pdd4=StringVar()
    pddr=IntVar()
    pddc=IntVar()
    '''
    
    pdl1=l1=Label(rootpd,text="Patient Details",fg=Colour.col,font=("Lucida Calligraphy", 12, "bold underline"),anchor=CENTER,width=25,padx=4).grid(row=0,column=0,columnspan=2,pady=1)
        
    pdl2=Label(rootpd,text="Full Name:",padx=2).grid(row=1,column=0,sticky=W)
    pdl3=Label(rootpd,text=name1,padx=4).grid(row=1,column=1,sticky=W)

    pdl4=Label(rootpd,text="Email:",padx=2).grid(row=2,column=0,sticky=W)
    pdl5=Label(rootpd,text=email1,padx=4).grid(row=2,column=1,sticky=W)

    pdl6=Label(rootpd,text="Phone:",padx=2).grid(row=3,column=0,sticky=W)
    pdl7=Label(rootpd,text=phone1,padx=4).grid(row=3,column=1,sticky=W)

    pdl8=Label(rootpd,text="Gender:",padx=2).grid(row=4,column=0,sticky=W)
    pdl9=Label(rootpd,text=gender1,padx=4).grid(row=4,column=1,sticky=W)

    pdl10=Label(rootpd,text="Organ Donor:",padx=2).grid(row=5,column=0,sticky=W)
    pdl11=Label(rootpd,text=donor1,padx=4).grid(row=5,column=1,sticky=W)

    pdl11_1=Label(rootpd,text="Doctor Name",padx=2).grid(row=6,column=0,sticky=W)
    pdl11_2=Label(rootpd,text=doctor1,padx=4).grid(row=6,column=1,sticky=W)
    
    pdl12=Label(rootpd,text="Patient Diagnosis",fg=Colour.col,font=("Lucida Calligraphy", 12, "bold underline"),anchor=CENTER,width=25,padx=4).grid(row=8,column=0,columnspan=2,pady=5)

    pds_1=Scrollbar(rootpd)
    pdt_1=Text(rootpd,height=3,width=45)
    pds_1.grid(row=10,column=2,sticky=E)
    pdt_1.grid(row=10,column=0,columnspan=2)
    pds_1.config(command=pdt_1.yview)
    pdt_1.config(yscrollcommand=pds_1.set)
    
    pdb1=Button(rootpd,text="SAVE DIAGNOSIS",command=lambda:pdb1_click(phone1,pdt_1.get('1.0','end')),width=13).grid(row=11,column=0,columnspan=1,sticky=W+N+E+S)
    pdb2=Button(rootpd,text="DOWNLOAD DIAGNOSIS",command=lambda:pdb2_click(phone1,pdt_1.get('1.0','end')),width=12).grid(row=11,column=1,columnspan=2,sticky=W+N+E+S)

    pdb3=Button(rootpd,text="EMAIL DIAGNOSIS",command=lambda:pdb3_click(email1,phone1,pdt_1.get('1.0','end'))).grid(row=12,column=0,columnspan=1,sticky=W+N+E+S)
    pdb4=Button(rootpd,text="PRINT DIAGNOSIS",command=lambda:pdb4_click(phone1,pdt_1.get('1.0','end'))).grid(row=12,column=1,columnspan=2,sticky=W+N+E+S)

    pdb5=Button(rootpd,text="PATIENT DIAGNOSIS HISTORY",command=lambda:pdb5_click(phone1)).grid(row=13,column=0,columnspan=3,sticky=W+N+E+S)

    rootpd.mainloop()

def pdb1_click(phone1,datapdt_1):
    print(datapdt_1)
    print(len(datapdt_1))
    #dpdt_1=datapdt_1+"\n---XXX---\n"
    if len(datapdt_1)==1:
        tkinter.messagebox.showerror("No Data","Patient Diagnosis Not Entered")
        return
    try:
            conn=sqlite3.connect("test_1")
            conn.execute("insert into t3 values('%s','%s','%s');"%(phone1,Doctor.name,datapdt_1))
            conn.commit()
            conn.close()
            print("Insert Done")
            tkinter.messagebox.showinfo("Insert Successful","Patient Diagnosis Saved")
    except Exception as e:
            conn.rollback()
            print(e)
            conn.close()
            print("Insert Not Done")
            tkinter.messagebox.showerror("Insert Unsuccessfull","Patient Diagnosis Not Saved")
def pd_back():
    rootpd.destroy()
    rootph.deiconify()

def pdb2_click(phone1,datapdt_1):
    #pdb1_click(phone1,datapdt_1)
    if len(datapdt_1)==1:
        tkinter.messagebox.showerror("No Data","Patient Diagnosis Not Entered")
        return
    f1=open("print1.txt","w")
    f1.write(datapdt_1)
    f1.close()
    os.startfile("print1.txt")
    #os.startfile("print1.txt","print")

def pdb3_click(email1,phone1,datapdt_1):
    #pdb1_click(phone1,datapdt_1)
    if len(datapdt_1)==1:
        tkinter.messagebox.showerror("No Data","Patient Diagnosis Not Entered")
        return
    id1="PYTHONCHMS@gmail.com"
    pass1="Python#CHMS"
    f1=open("DIAGNOSIS1.txt","w")
    f1.write(datapdt_1)
    f1.close()
    os.startfile("DIAGNOSIS1.txt")
    try:
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.ehlo()
        s.starttls()
        s.login(id1,pass1)
        message1="Diagnosis and Precription\n\n"+str(datapdt_1)+"\n\nYours Truly,\nDr. %s"%Doctor.name
        s.sendmail(id1,[email1,id1],message1)
        s.quit()
        print("Email Successfully Sent")
        tkinter.messagebox.showinfo("Email Sent","Email Successfully Sent")
    except Exception as e:
        print("Email Unsuccessfull")
        tkinter.messagebox.showerror("Email Not Sent","Email Unsuccessfull")
        print(e)
def pdb4_click(phone1,datapdt_1):
    #pdb1_click(phone1,datapdt_1)
    if len(datapdt_1)==1:
        tkinter.messagebox.showerror("No Data","Patient Diagnosis Not Entered")
        return
    '''f1=open("print1.txt","w")
    f1.write(datapdt_1)
    f1.close()
    os.startfile("print1.txt")
    os.startfile("print1.txt","print")'''
    f1=open("save1.rtf","w")
    f1.write(datapdt_1)
    f1.close()
    #os.startfile("save1.rtf")
    os.startfile("save1.rtf","print")

def pdb5_click(phone1):
    rootdph = Tk()
    rootdph.title("Diagnosis History") 
    S = Scrollbar(rootdph)
    T = Text(rootdph, height=10, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=TOP, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    try:
        conn=sqlite3.connect("test_1")
        c=conn.cursor() 
        c=conn.execute("select diagnosis from t3 where pphone='%s' and ndoctor ='%s';"%(phone1,Doctor.name))
        prntstr=""
        count=0
        for row in c:
            T.insert(END,str(row[0])+"---------\n")
            print(str(row[0])+"--------\n")
            print(type(row))
            print(type(row[0]))
            prntstr+=str(row[0])
            count+=1
        T.insert(END,"------EOF------\n")
        print("Extract Complete")
        if count!=0:
            dphb1=Button(rootdph,text="PRINT DIAGNOSIS HISTORY",command=lambda:dphb1_click(prntstr)).pack(side=BOTTOM,fill=X)
        else:
            print("No history")
            rootdph.destroy()
            tkinter.messagebox.showerror("No history","No past records found")
    except Exception as e:
        conn.rollback()
        print("NO EXTRACT")
        print(e)
        conn.close()
    rootdph.mainloop()

def dphb1_click(prntstr):
    f1=open("print1.rtf","w")
    f1.write(prntstr)
    f1.close()
    #os.startfile("print1.txt")
    os.startfile("print1.rtf","print")


#######################################################################################################################################################################
#SignUp Page

def signUpPage():
    global rootsu
    rootsu=Tk()
    rootsu.title("SignUp Page")

    menumake(rootsu,su_back)
    
    sul0=Label(rootsu,text="Doctors Registeration",font=("Lucida Handwriting", 12, "bold underline"),fg=Colour.col).grid(row=0,column=0,columnspan=3,sticky=W+N+E+S,pady=5)

    sul1=Label(rootsu,text="Name:",padx=1).grid(row=1,column=0,sticky=W,padx=2)
    sue1=Entry(rootsu,width=50)
    sue1.grid(row=1,column=1,sticky=W+N+E+S)

    sul2=Label(rootsu,text="Username:",padx=1).grid(row=2,column=0,sticky=W,padx=2)
    sue2=Entry(rootsu)
    sue2.grid(row=2,column=1,sticky=W+N+E+S)

    sul3=Label(rootsu,text="Password:",padx=1).grid(row=3,column=0,sticky=W,padx=2)
    sue3=Entry(rootsu)
    sue3.grid(row=3,column=1,sticky=W+N+E+S)

    sub1=Button(rootsu,text="Register",command=lambda:sub1_click(sue1.get(),sue2.get(),sue3.get()))
    sub1.grid(row=4,column=0,columnspan=3,sticky=W+N+E+S)
    
    rootsu.mainloop()

def sub1_click(sud1,sud2,sud3):
    print(sud1)
    print(sud2)
    print(sud3)
    try:
            conn=sqlite3.connect("test_1")
            conn.execute("insert into t2 values('%s','%s','%s');"%(sud1,sud2,sud3))
            conn.commit()
            conn.close()
            print("Insert Done")
    except Exception as e:
            conn.rollback()
            print(e)
            conn.close()
            print("Insert Not Done")
    rootsu.destroy()
    loginPage()
def su_back():
    rootsu.destroy()
    loginPage()
def signup(c):
    pass


#######################################################################################################################################################################
#Dashboard

def doctorPage():
    global rootdp
    rootdp=Tk()
    #rootdp.geometry('{}x{}'.format(300,80))
    rootdp.resizable(width=False,height=False)
    rootdp.title("Doctor's Dashboard")
    menumake(rootdp,dp_back)
    
    dpl1=Label(rootdp,text="DASHBOARD",fg=Colour.col,font=("Lucida Calligraphy", 11, "bold underline"),anchor=CENTER,width=25,padx=4).pack(side="top",pady=5)
    dpb1=Button(rootdp,text="LIST OF DOCTORS",padx=4,command=dpb1_click).pack(side="top",fill=X,pady=0)
    dpb2=Button(rootdp,text="PATIENT RECORDS",padx=4,command=dpb2_click).pack(side="top",fill=X)
    rootdp.mainloop()

def dpb1_click():
    rootdpb1 = Tk()
    rootdpb1.title("List Of Doctors") 
    dp_S = Scrollbar(rootdpb1)
    dp_T = Text(rootdpb1, height=10, width=50)
    dp_S.pack(side=RIGHT, fill=Y)
    dp_T.pack(side=TOP, fill=Y)
    dp_S.config(command=dp_T.yview)
    dp_T.config(yscrollcommand=dp_S.set)
    try:
        conn=sqlite3.connect("test_1")
        c=conn.cursor() 
        c=conn.execute("select name from t2")
        prntstr=""
        count=0
        for row in c:
            dp_T.insert(END,str(row[0])+"\n")
            print(str(row[0])+"\n")
            prntstr+=str(row[0])+"\n"
            count+=1
        dp_T.insert(END,"------EOF------\n")
        print("Extract Complete")
        conn.close()
        if count!=0:
            pass
        else:
            print("No records")
            rootdpb1.destroy()
    except Exception as e:
        conn.rollback()
        print("NO EXTRACT")
        print(e)
        conn.close()
    rootdpb1.mainloop()
def dpb2_click():
    rootdp.destroy()
    patientHistory()
def dp_back():
    rootdp.destroy()
    rootlp.deiconify()


#######################################################################################################################################################################
#Login Page

class Doctor:
    name=""

def loginPage():
    global rootlp
    rootlp=Tk()
    rootlp.title("LOGIN PAGE")
    rootlp.resizable(width=False,height=False)
    '''d1=StringVar()
    d2=StringVar()'''
    menumake1(rootlp)

    l0_0=Label(rootlp,text="Clinic/Patient Management System",font=("Lucida Handwriting", 14, "underline"),fg=Colour.col).grid(row=0,column=0,columnspan=2,sticky=W+N+E+S,pady=1)
    l0_1=Label(rootlp,text="Fast Easy Efficiant!",font=("Lucida Handwriting", 10, ""),fg="Navy Blue").grid(row=1,column=0,columnspan=2,sticky=W+N+E+S,pady=1)
    l0_1=Label(rootlp).grid(row=2,column=0,columnspan=2,pady=3)
    l1=Label(rootlp,text="Username:").grid(row=3,column=0,sticky=W,pady=0,padx=1)
    e1=Entry(rootlp,width=50)
    e1.grid(row=3,column=1,sticky=W+N+E+S)

    l2=Label(rootlp,text="Password:").grid(row=4,column=0,sticky=W,padx=1)
    e2=Entry(rootlp,width=50,show="*")
    e2.grid(row=4,column=1,sticky=W+N+E+S)

    b1=Button(rootlp,text="LOGIN",width=60,command=lambda:b1_click(e1.get(),e2.get()))
    b1.grid(row=5,column=0,columnspan=2)
    b2=Button(rootlp,text="New User? - Signup",width=60,bd=0)
    b2.bind("<Button-1>",signup)
    b2.grid(row=6,column=0,columnspan=2)

    b3=Button(rootlp,text="POWERED BY PYTHON",font=("Lucida Handwriting", 6, "underline"),fg="Navy Blue",relief="ridge",bd=0)
    b3.bind("<ButtonPress-1>",lpl3_click)
    b3.grid(row=7,column=0,columnspan=2,sticky=E,pady=0,padx=1)
    rootlp.mainloop()
    
def rootlp_hide():
    rootlp.withdraw()

def lpl3_click(e):
    webbrowser.open("www.python.org", new=1)
    
def b1_click(d1,d2):
    print(d1)
    print(d2)
    count=0
    try:
        conn=sqlite3.connect("test_1")
        c=conn.cursor()
        c=conn.execute("select name from t2 where username ='%s' and password ='%s';"%(d1,d2))
        print(c)
        print(type(c))
        for row in c:
            count+=1
            print(row[0])
            Doctor.name=row[0]
    except Exception as e:
        conn.rollback()
        print("NO EXTRACT")
        print(e)
        conn.close()
    if count!=0:
        rootlp_hide()
        doctorPage()
    else:
        print("Invalid")
        tkinter.messagebox.showerror("Error","Invalid Username Or Password")
    
def signup(c):
    rootlp.destroy()
    signUpPage()


#######################################################################################################################################################################
loginPage()


