
import mysql.connector
mydb=mysql.connector.connect(user="root",database="empm")
mycur=mydb.cursor()

#create
C="create table emp(EMPID integer not null primary key, EMPNAME char(20) not null, DESIG char(20) not null, HIREDATE char(10) not null, SALARY decimal not null)"

mycur.execute(C)

#show
def showt():
   print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
   print("\t\t\t\t\t\tx             EMPLOYEE LIST            x")
   print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
   C="SELECT * FROM emp"
   mycur.execute(C)
   
   K=mycur.fetchall()
   
   if mycur.rowcount==0:     
      print("\t\t\t\t\t\t\tOops!!! SOMETHING WENT WRONG, NO MATCHING RECORDS")
            
   else:
      for i in K:
         print("\t\t\t\t\t\t\t",i[0],i[1],i[2])
        
#add
def addemp():
   C="INSERT INTO emp(EMPID,EMPNAME,DESIG,HIREDATE,SALARY)VALUES(%s,%s,%s,%s,%s)"
   mycur.execute(C,(id,n,desig,hdate,sal))
   print('successfully added')
     
   mydb.commit()

#search by id
def searchemp1():
   C="SELECT * FROM emp WHERE EMPID LIKE '%s' "
   mycur.execute(C%(empid))
   result=mycur.fetchall()
   
   st=''
   for j in result:
      for u in j:
         st+=str(u)+' '
  
   if st=='':      
      print("\t\t\t\t\t\t\tOops!!! INVALID ENTRY TRY AGAIN ")
      
                  
   else:
      print("\t\t\t\t\t\tEmployee ID:", j[0])
      print("\t\t\t\t\t\tEmployee name:", j[1])
      print("\t\t\t\t\t\tDesignation:", j[2])         
      print("\t\t\t\t\t\tHiredate:",j[3])
      print("\t\t\t\t\t\tSalary", j[4])
     
#search by name
def searchemp2():
   C="SELECT * FROM emp WHERE EMPNAME LIKE '%s' "
   mycur.execute(C%(empn))
   result=mycur.fetchall()
   
   st=''
   for j in result:
      for u in j:
         st+=str(u)+' '

      
   if st=='':      
      print("\t\t\t\t\t\t\tOops!!! INVALID ENTRY TRY AGAIN ")
      
            
   else:
      print("\t\t\t\t\t\tEmployee ID:", j[0])
      print("\t\t\t\t\t\tEmployee name:", j[1])
      print("\t\t\t\t\t\tDesignation:", j[2])
      print("\t\t\t\t\t\tHiredate:",j[3])
      print("\t\t\t\t\t\tSalary", j[4])

#update desig
def updateemp1():
   C="UPDATE emp SET DESIG=%s WHERE EMPNAME=%s"
   u=(empd,empn)
   mycur.execute(C,u)
   x=mycur.rowcount

   if x==0:      
      print("\t\t\t\t\t\t\tOops!!! INVALID ENTRY TRY AGAIN ")
      
   else:
      print('successfully updated')
     
   mydb.commit()

#update salary
def updateemp2():
   C="UPDATE emp SET SALARY=%s WHERE EMPNAME=%s"
   u=(empsal,empn)
   mycur.execute(C,u)
   x=mycur.rowcount
   
   if x==0:      
      print("\t\t\t\t\t\t\tOops!!! INVALID ENTRY TRY AGAIN ")
           
   else:
      print('successfully updated')
     
   mydb.commit()

#delete
def delemp():
   C="DELETE FROM emp WHERE EMPNAME=%s"
   mycur.execute(C,(empn,))
   x=mycur.rowcount
   
   if x==0:      
      print("\t\t\t\t\t\t\tOops!!! INVALID ENTRY TRY AGAIN ")    

   else:
      print('successfully deleted')
         
   mydb.commit()

#payslip
def payslip():
   C="SELECT * FROM emp WHERE EMPNAME LIKE '%s' "
   mycur.execute(C%(empn))
   result=mycur.fetchall()

   st=''
   for j in result:
      for u in j:
         st+=str(u)+' '

   if st=='':     
      print("\t\t\t\t\t\t\tOops!!! INVALID ENTRY TRY AGAIN ")
      
   else:
      for j in result:
         print('---------------------------------------------------------')
         print('\tRIVERA Computer Solutions Pvt Ltd')
         print('\t       Novel Business Center')
         print('---------------------------------------------------------')

         print('\tPayslip for the period of October 2020')
         print("Employee ID:", j[0])
         print("Employee name:", j[1])
         print("Designation:", j[2])   
         print("Hiredate:",j[3])
         print('---------------------------------------------------------')
         print('EARNINGS                  AMOUNT')
         print('---------------------------------------------------------')
         print('Basic Pay                ',j[4])            
         print('Medical Allowance        ',200)
         print('Overtime Allowance       ',ext/24*1000)
         print('---------------------------------------------------------')
         print('TOTAL EARNINGS           ',int(j[4])+200+(ext/24*1000))
         print('---------------------------------------------------------')

#functioncall
while True:  
   print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
   print("\t\t\t\t\t\tx             MAIN MENU                x")
   print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
   print("\t\t\t\t\t\t            1.ADMIN MODE                ")
   print("\t\t\t\t\t\t            2.USER MODE                 ")
   print("\t\t\t\t\t\t            3.EXIT                      ")
   print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")                                      
   print("\t\t\t Welcome to RIVERA Computer Solutions Pvt Ltd, please choose appropriate mode to continue _/\_")
   ch1=int(input('\t\t\t\t\t\tEnter your choice (1/2/3) :'))   
   while ch1>3 or ch1<1:
      ch1=int(input('\t\t\t\t\t\tEnter a valid choice :'))

   if ch1==1:
      while True:           
         print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
         print("\t\t\t\t\t\tx             ADMIN MODE               x")
         print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
         print("\t\t\t\t\t\t          1.ADD NEW RECORD              ")
         print("\t\t\t\t\t\t          2. EDIT EMPLOYEE              ")
         print("\t\t\t\t\t\t       3.DELETE EMPLOYEE RECORD         ")
         print("\t\t\t\t\t\t         4.BACK TO MAIN MENU            ")
         print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")                                      
         ch=int(input('\t\t\t\t\t\tEnter your choice (1/2/3) :'))
         while ch>4 or ch<1:
            ch=int(input('\t\t\t\t\t\tEnter a valid choice :'))

      
         #ADD   
         if ch==1:
            id=int(input('\t\t\t\t\t\tEnter 3 digit employee id :'))
            while len(str(id))>=4 or len(str(id))<=2:
               id=int(input('\t\t\t\t\t\tEnter a valid 3 digit employee id :'))
               
            n=input('\t\t\t\t\t\tEnter employee name:')
            desig=input('\t\t\t\t\t\tEnter employee designation (CLERK/SALESMAN/MANAGER/ANALYST/PRESIDENT) :')
            while desig not in 'clerk salesman manager analyst president CLERK SALESMAN MANAGER ANALYST PRESIDENT':
               desig=input('\t\t\t\t\t\tEnter a valid employee designation (CLERK/SALESMAN/MANAGER/ANALYST/PRESIDENT) :')
            hdate=input('\t\t\t\t\t\tEnter employee hiredate (dd-mm-yyyy) :')
            while len(hdate)>=11 or len(hdate)<=9:
               hdate=input('\t\t\t\t\t\tEnter a valid employee hiredate (dd-mm-yyyy) :')
               
            sal=float(input('\t\t\t\t\t\tEnter employee salary :'))
           
            addemp()
    
         #EDIT 
         elif ch==2:           
            print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("\t\t\t\t\t\tx                EDIT                  x")
            print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("\t\t\t\t\t\t      1.EDIT EMPLOYEE DESIGATION        ")
            print("\t\t\t\t\t\t       2. EDIT EMPLOYEE SALARY          ")
            print("\t\t\t\t\t\t               3. BACK                  ")
            print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            chE=int(input('\t\t\t\t\t\tEnter your choice (1/2/3) :'))
            while chE>3 or chE<1:
               chE=int(input('\t\t\t\t\t\tEnter a valid choice :'))

            
               #EDITDESIG
               
            if chE==1:
               empn=input('\t\t\t\t\t\tEnter name of the employee :')
               empd=input('\t\t\t\t\t\tEnter employee new designation :')
               desig=input('\t\t\t\t\t\tEnter employee designation (CLERK/SALESMAN/MANAGER/ANALYST/PRESIDENT) :')
               while desig not in 'clerk salesman manager analyst president CLERK SALESMAN MANAGER ANALYST PRESIDENT':
                  desig=input('\t\t\t\t\t\tEnter a valid employee designation (CLERK/SALESMAN/MANAGER/ANALYST/PRESIDENT) :')              
               updateemp1()


               #EDITSAL
            elif chE==2:
               empn=input('\t\t\t\t\t\tEnter name of the employee :')
               empsal=float(input('\t\t\t\t\t\tEnter salary to be updated :'))
              
               updateemp2()
            elif chE==3:
               continue

            else:               
               print("\t\t\t\t\tOops!!! SOMETHING WENT WRONG, INVALID INPUT")      
                                                   
         #DELETE               
         elif ch==3:
            empn=input('\t\t\t\t\t\tEnter name of employee whose record is to be deleted :')               
            delemp()

         elif ch==4:
            break

         else:           
            print("\t\t\t\t\tOops!!! SOMETHING WENT WRONG, INVALID INPUT")      
               
   elif ch1==2:
      while True:
         print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
         print("\t\t\t\t\t\tx              USER MODE               x")
         print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
         print("\t\t\t\t\t\t        1.SHOW LIST OF EMPLOYEES        ")
         print("\t\t\t\t\t\t           2.SEARCH EMPLOYEE            ")
         print("\t\t\t\t\t\t          3.GENERATE PAY SLIP           ")
         print("\t\t\t\t\t\t          4.BACK TO MAIN MENU           ")
         print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
         ch2=int(input('\t\t\t\t\t\tEnter your choice (1/2/3) :'))
         while ch2>4 or ch2<1:
            ch1=int(input('\t\t\t\t\t\tEnter a valid choice :'))

         #SHOW
                  
         if ch2==1:
            showt()
           
         #SEARCH               
         elif ch2==2:           
            print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("\t\t\t\t\t\tx               SEARCH                 x")
            print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("\t\t\t\t\t\t        1.SEARCH BY EMPLOYEE ID         ")
            print("\t\t\t\t\t\t        2.SEARCH BY EMPLOYEE NAME       ")
            print("\t\t\t\t\t\t              3. BACK                   ")
            print("\t\t\t\t\t\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            chS=int(input('\t\t\t\t\t\tEnter your choice (1/2/3) :'))
            while chS>3 or chS<1:
               chS=int(input('\t\t\t\t\t\tEnter a valid choice :'))


         #SEARCHID             
            if chS==1:
               empid=int(input('\t\t\t\t\t\tEnter 3 digit employee id to be searched:'))
               while len(str(id))>=4 or len(str(id))<=2:
                  id=int(input('\t\t\t\t\t\tEnter a valid 3 digit employee id :'))              
               searchemp1()
            #SEARCHNAME                        
            elif chS==2:
               empn=input('\t\t\t\t\t\tEnter employee name to be searched:')              
               searchemp2()

            elif chS==3:             
               continue                                      
            else:              
               print("\t\t\t\t\tOops!!! SOMETHING WENT WRONG, INVALID INPUT")      
                     
         #PAYSLIP                     
         elif ch2==3:
            empn=input('\t\t\t\t\t\tEnter employee name to generate a pay slip:')
            ext=float(input('\t\t\t\t\t\tEnter extra hours worked :'))
                           
            payslip()                
         elif ch2==4:
            break
         else:          
            print("\t\t\t\t\t\t\tOops!!! SOMETHING WENT WRONG, INVALID INPUT")
               
   else:
      print("\t\t\t\t\t\texiting...")  
      break

mydb.close()  
