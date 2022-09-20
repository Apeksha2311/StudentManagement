star=100
import re
import mysql.connector as db


class Student:
    def __init__(self):
        self.__adminid = 'admin'
        self.__adminpasswd = 'admin123'



        # create table for 
        mydb = db.connect(host = 'localhost', user = 'root' , passwd = 'root', database = 'StudentManagement')
        cur = mydb.cursor()
        query = '''create table if not exists RegisterStudent(id int primary key auto_increment,Name varchar(100) not null,
        contact bigint not null,email varchar(100) unique not null,password varchar(100));'''
        cur.execute(query)


        query = '''create table if not exists Student(id int primary key auto_increment,Name varchar(100) not null,
        contact bigint not null,email varchar(100) unique not null,password varchar(100));'''
        cur.execute(query) 


        query = '''create table if not exists SApplication(id int primary key auto_increment,Name varchar(100) not null,
        contact bigint not null,email varchar(100) unique not null,password varchar(100));'''
        cur.execute(query)


        mydb.close()



    def connection(self):
        self.mydb = db.connect(host = 'localhost', user = 'root' , passwd = 'root', database = 'StudentManagement')
        self.cur = self.mydb.cursor()

    def AdminLogin(self,adminid,adminpasswd):
        if self.__adminid == adminid:
            if self.__adminpasswd == adminpasswd:
                
                return True
            else:
                return ' Invalid password '

                
        else:
            return ' Invalid Id ' 


    def validateUsername(self,name):
        name_length = len(name)
        x = re.findall('[A-Za-z]+',name)
        
        if len(x[0]) == name_length:
            return True 
        else:
            return False




    #check valid contact no
    def validateContact(self,contact):
        ptr=r"[6-9]\d{9}" 
        x=re.findall(ptr,contact)
        if len(x) > 0:
            return True
        else:
            return False  


    #check valid email id
    def validateEmail(self,email):
        ptr=r"^[a-zA-Z0-9\.]+@[a-z]+\.[a-z]+" 
        x=re.findall(ptr,email)
        if len(x) > 0:
            return True
        else:
            return False   


    #Register Student function
    def StudentRegister(self,name,contact,email,passwd,confirm_pass):
        self.userName_flag = self.validateUsername(name)
        if not self.userName_flag:
            return "Username is not valid try only with alphabets"

        
        self.userContact_flag = self.validateContact(contact)
        if not self.userContact_flag:
            return "Contact Number is not valid"

        
        self.userEmail_flag = self.validateEmail(email)
        if not self.userEmail_flag:
            return "Email Id is not valid" 

                              
                              
        

        if len(passwd)>=8:
            if passwd == confirm_pass :
                self.password_flag = True
            else:
                return "Password MisMatch Plz try again"
        else:
            return "Password should be greater than or equal to 8 characters"


        if self.userName_flag == True and self.userContact_flag == True and self.userEmail_flag == True and self.password_flag == True:
            self.connection()

            try:
                data = (name,email,contact,passwd)
                query = '''insert into  registerstudent(Name,contact,email,password) values(%s,%s,%s,%s);'''

                self.cur.execute(query,data)

                self.cur.execute("commit;")
                self.mydb.close()
            except:
                self.mydb.close()
                return 'Email or contact Already Exists....'
            return f"Student {name} is Successfully Registered"    



            
        
        




#application start from here
app=Student()
print(" STUDENT MANAGEMENT SYSTEM ".center(star, '*'))

while True: 
    print('1-Admin login\n2-Student Login\n3-Exit ') 
    ch=int(input('Enter your Choice:')) 


    #choice @1admin
    if ch == 1:
        print('Admin Login Section'.center(star,"*"))

        adminId=input("Enter Admin Id:")
        adminPwd=input("Enter Admin Password:")

        LoginStatus=app.AdminLogin(adminId,adminPwd)

        if LoginStatus==True:
            print(' Admin Login Succefull  '.center(star,"*"))

            #Admin choice
            while True:  
                print('1-Add Student\n2-Remove Student\n3-List Student\n4-View Pending Applications\n5-Logout') 

                Adch=int(input('Enter your Choice:')) 

                if Adch == 1:
                    print(' Add Student Section '.center(star,"*"))







                elif Adch == 2:
                    print(' Remove Student Section'.center(star,"*"))

                    
                    




                elif Adch == 3:
                    print(' List Student Section'.center(star,"*"))

                    



                elif Adch == 4:
                    print(' View Pending Applications Section'.center(star,"*"))

                    




                elif Adch == 5:
                    print(' Logged Out '.center(star,"*"))
                    break


                else:
                    print(' Invalid Choice '.center(star,"*"))


        else:
            print(f'{LoginStatus}'.center(star,"*"))

            
                              



       


        









    #choice @2student section
    elif ch == 2:
        print('Student Section'.center(star,"*"))

        #student Choice
        while True:
            print('1-Register Student\n2-Student Login\n3-Exit') 

            stuch=int(input('Enter your Choice:')) 

            if stuch == 1:
                print(' Register Student Section '.center(star,"*"))

                SName=input("Enter your name:").strip()
                SPhone=int(input("Enter your Phone no:").strip())

                SEmail=input("Enter your Email:").strip()
                SPassword=input("Enter your Password:").strip()
                SCPassword=input("Confirm Password:").strip()

                regStatus=app.StudentRegister(SName,SPhone,SEmail,SPassword,SCPassword)

                print(f' {regStatus} '.center(star,"*"))












            elif stuch == 2:
                print(' Student Login '.center(star,"*"))

                StudentId=input("Enter Student Id:")
                StudentPwd=input("Enter Student Password:")

                LoginStatus=app.StudentLogin(StudentId,StudentPwd)

                if LoginStatus==True:
                    print(' Student Login Succefull  '.center(star,"*"))



                #student choice After Login
                while True:
            
                    print('1-Submit Application\n2-View Applications status\n3-Logout') 

                    log_st_ch=int(input('Enter your Choice:'))  

                    if log_st_ch == 1:
                        print(' Submit Application Section '.center(star,"*"))







                    elif log_st_ch == 2:
                        print(' Applications status '.center(star,"*"))

                    elif log_st_ch == 3:
                        print(' logout '.center(star,"*")) 
                        break

                    else :
                        print(' Invalid choice '.center(star,"*"))        

                    
                    




            elif stuch == 3:
                print(' Exiting Student Section'.center(star,"*"))
                break

            else:
                print(' Invalid Choice '.center(star,"*"))



        
        
    #Choice @3-Exit
    elif ch == 3:
        print(' Exiting Application '.center(star,"*"))
        break

        
    #Choice @Invlid choice    
    else:
        print(' Invalid Choice '.center(star,"*"))
        
        

   

    


 