from typing import Union, Any
from tkinter import *
import mysql.connector
from mysql.connector import CMySQLConnection, MySQLConnection

P_NAME = []
P_NUMBER = []
P_ADDRESS = []
P_EMAIL = []
P_AGE = []
P_MOBILE_NUMBER = []
P_DISEASE = []
a = []
q = []
d = []
bpb=[]
lpb=[]
rpb=[]
seb=[]
def bmi(w, h):
    b = w / (h * h)
    b = float(f'{b:.2f}')
    return b
class HEALTHISWEALTH():


    def ADD_PATIENT_INFORMATION(self):
        print("ADDING PATIENT INFORMATION : \n")
        print("ENTER PATIENT NAME :", end=" ")
        NAME = input().upper()
        P_NAME.append(NAME)

        print("ENTER PATIENT NUMBER :", end=" ")
        NUMBER = int(input())
        P_NUMBER.append(NUMBER)

        print("ENTER PATIENT AGE :", end=" ")
        AGE = int(input())
        P_AGE.append(AGE)

        print("ENTER PATIENT DISEASE :", end=" ")
        DISEASE = input().upper()
        P_DISEASE.append(DISEASE)

        print("ENTER PATIENT E-MAIL ID :", end=" ")
        EMAIL_ID = input().upper()
        P_EMAIL.append(EMAIL_ID)

        print("ENTER PATIENT ADDRESS :", end=" ")
        ADDRESS = input().upper()
        P_ADDRESS.append(ADDRESS)

        print("ENTER PATIENT MOBILE NUMBER :", end=" ")
        MOBILE_NUMBER = input()



        P_MOBILE_NUMBER.append(MOBILE_NUMBER)
        print("\n")


        mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
        c=mydb.cursor()
        #s1 = "CREATE TABLE IF NOT EXIST PINFO(P_NUMBER INT PRIMARY KEY,P_NAME TEXT,P_MOBILE_NUMBER BIGINT,P_ADDRESS TEXT,P_EMAIL TEXT,P_AGE INT,P_DISEASE TEXT,DOCTOR_NAME TEXT)"

        #cur.execute(s1)

        p1 = "INSERT INTO PINFO(P_NUMBER ,P_NAME,P_MOBILE_NUMBER,P_ADDRESS,P_EMAIL,P_AGE,P_DISEASE) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        b2 = (NUMBER, NAME, MOBILE_NUMBER, ADDRESS, EMAIL_ID, AGE, DISEASE)
        c.execute(p1, b2)
        mydb.commit()
        # mydb.close()



        def BloodProfile():


            print(
                "Complete Blood Profiling (CBP) is a routine screening test done for early onset detection or diagnosis when there are signs and symptoms related to a wide range of conditions and diseases affecting the blood cells (RBCs, WBCs, and platelets")
            print("HAEMOGLOIN LEVELS:")

            print("Normal Haemogloin levels ---- 12.0 - 17.7")
            print("Enter the Observed Haemoglobin levels   (BIOLOGICAL REFERENCE INTERVAL 12.0 - 17.4 gm/dl)")
            ha = float(input("Enter the observed Haemoglobin values"))

            q.append(ha)
            if ha < 12 or ha > 17.7:
                print("Abnormal Haemoglobin levels")
            else:
                print("Haemoglobin levels are normal")

            print("Enter the Observed WBC(WHITE BLOOD CELLS) COUNT (BIOLOGICAL REFERENCE INTERVAL 5000-10000 Cells/cumm)")
            wb = int(input())
            if (wb<5000 or wb>10000):
                print("ABNORMAL WBC COUNT")
            else:
                print("Normal WBC COUNT")

            print("Enter the Observed RBC(RED BLOOD CELLS) COUNT(millon/cumm) (BIOLOGICAL REFERENCE INTERVAL 4.00 - 5.50 Millions/cumm)")
            rb = float(input())
            if (rb<4.00 or rb>5.50):
                print("ABNORMAL RBC COUNT")
            else:
                print("Normal RBC COUNT")

            print("Enter the Observed PLATELET COUNT(lakhs) (BIOLOGICAL REFERENCE INTERVAL 1.5-4.0 Lakhs)")
            pl = float(input())
            if (pl<1.5 or pl> 4.0):
                print("ABNORMAL PLATELET COUNT")
            else:
                print("Normal PLATELET COUNT")

            print("Enter the Observed RANDOM GLUCOSE LEVELS   (BIOLOGICAL REFERENCE INTERVAL <140 mg/dl)")
            gl = float(input())
            if (gl<70 or gl> 140):
                print("ABNORMAL GLUCOSE LEVELS")
            else:
                print("Normal GLUCOSE LEVELS")
            print("Blood Profile values Added Successfully")
            mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
            c=mydb.cursor()


            b1 = "INSERT INTO bloodprofile(pno,haemoglobin,WBC,RBC,platelets,Glucose) VALUES (%s,%s,%s,%s,%s,%s)"
            b3 = (NUMBER,ha,wb,rb,pl,gl)
            c.execute(b1,b3)
            mydb.commit()
            # mydb.close()

        def BMI():
            print("BMI is BODY MASS INDEX")
            print("Having a bad BMI is an early invitation to diseases")
            print("BMI < 25 is NORMAL")
            print("BMI > 25 is considered as pre-obesse")
            print("BMI >29 is considered as Dangerous and over obesse")
            print("Enter your inputs")
            print("Enter weight in kgs")
            w=float(input())
            print("Enter height in m")
            h=float(input())
            aa=bmi(w,h)
            if aa < 25 and aa> 18:
               print(aa)
               print("Your BMI is Normal")

            elif aa<18:
               print(aa)
               print("Your BMI is EXTREMELY LOW")
            else:
                print(aa)
                print("Your BMI is OBESSE")

            a.append(aa)
            print(a)
            print()

        def lipidprofile():
            print("A lipid profile is a combination of blood tests performed to check the cholesterol levels and the level of triglycerides in the blood. ")
            print("These are nothing but fat content present in your bloodstream. Unhealthy levels of lipids can clog your arteries and increase your risk of heart disease and stroke. ")
            print ( "These are also responsible for unhealthy weight gain.")
            print("Enter the Observed Values for Total Cholestrol (BIOLOGICAL REFERENCE INTERVAL 130-200 mg/dl)")
            tc=float(input())
            if (tc<130 or tc> 200):
                print("ABNORMAL TOTAL CHOLESTROL LEVELS")
            else:
                print("NORMAL TOTAL CHOLESTROL LEVELS")
            print("Enter the Observed Values for TRIGLYCERIDES (BIOLOGICAL REFERENCE INTERVAL 40-160 mg/dl)")
            tr=float(input())
            if (tr<40 or tr> 160):
                print("ABNORMAL TOTAL TRIGLYCERIDES LEVELS")
            else:
                print("NORMAL TRIGLYCERIDES LEVELS")

            print("Enter the Observed Values for HDL CHOLESTROL (BIOLOGICAL REFERENCE INTERVAL 35-55 mg/dl)")
            hdl=float(input())
            if (hdl<35 or hdl> 55):
                print("ABNORMAL HDL CHOLESTROL LEVELS")
            else:
                print("NORMAL HDL CHOLESTROL LEVELS")
            print("Enter the Observed Values for LDL CHOLESTROL (BIOLOGICAL REFERENCE INTERVAL 70-170 mg/dl)")
            ldl=float(input())
            if (ldl<35 or ldl> 55):
                print("ABNORMAL LDL CHOLESTROL LEVELS")
            else:
                print("NORMAL LDL CHOLESTRO LEVELS")
            print("Enter the Observed Values for VLDL CHOLESTROL (BIOLOGICAL REFERENCE INTERVAL 35-55 mg/dl)")
            vldl=float(input())
            if (vldl<35 or vldl> 55):
                print("ABNORMAL VLDL CHOLESTROL LEVELS")
            else:
                print("NORMAL VLDL CHOLESTROL LEVELS")

            b5 = "INSERT INTO lipidddprofile(pno,total_cholestrol,triglycerides,hdl_cholestrol,ldl_cholestrol,vldl_cholestrol) VALUES (%s,%s,%s,%s,%s,%s)"
            b6 = (NUMBER,tc,tr,hdl,ldl,vldl)
            c.execute(b5,b6)
            mydb.commit()



            print("LIPID Profile values Added Successfully")

        def renalprofile():
            print("Renal profile is a test to assess kidney health.")
            print( " It is useful to measure kidney function. Renal profile gives information on levels of creatinine, sodium, calcium, chloride, blood urea and potassium.")
            print( " Some laboratory calculates glomerular filtration rate too. Kidney plays an important role in maintaining fluid and electrolyte balance.")
            print("Enter the Observed Values for BLOOD UREA LEVELS (BIOLOGICAL REFERENCE INTERVAL 15-45 mg/dl)")
            bu=float(input())
            if (bu<15 or bu> 45):
                print("ABNORMAL BLOOD UREA LEVELS LEVELS")
            else:
                print("NORMAL BLOOD UREA LEVELS LEVELS")
            print("Enter the Observed Values for SERUM CREATININE (BIOLOGICAL REFERENCE INTERVAL  0.7-1.5 mg/dl)")
            sc=float(input())
            if (sc<0.7 or sc> 1.5):
                print("ABNORMAL SERUM CREATININE LEVELS")
            else:
                print("NORMAL SERUM CREATININE LEVELS")

            print("Enter the Observed Values for URIC ACID (BIOLOGICAL REFERENCE INTERVAL 3.5-8.5 mg/dl)")
            ua=float(input())
            if (ua<3.5 or ua> 8.5):
                print("ABNORMAL URIC ACID  LEVELS")
            else:
                print("NORMAL URIC ACID LEVELS")
            b7 = "INSERT INTO renallprofile(pno,BLOOD_UREA,SERUM_CREATININE,URIC_ACID) VALUES (%s,%s,%s,%s)"
            b8 = (NUMBER,bu,sc,ua)
            c.execute(b7,b8)
            mydb.commit()
            print("RENAL Profile values Added Successfully")
        def serum_electrolytes():
            print("The Serum Electrolyte Test is performed:")

            print("* As a part of a routine health checkup")

            print("* To assess problems in the water and pH balance of the body")

            print("* As a part of the checkup to diagnose kidney diseases")


            print("Upon the appearance of symptoms indicating neuromuscular conditions like muscular weakness, irregular heartbeats or cardiac arrhythmia, etc")

            print("Enter the Observed Values for SODIUM LEVELS (BIOLOGICAL REFERENCE INTERVAL 135-145 mmol/L)")
            sdm=float(input())
            if (sdm<135 or sdm> 145):
                print("ABNORMAL SODIUM LEVELS")
            else:
                print("NORMAL SODIUM LEVELS")
            print("Enter the Observed Values for POTASSIUM LEVELS (BIOLOGICAL REFERENCE INTERVAL 3.5-5.1 mmol/L)")
            pts=float(input())
            if (pts<3.5 or pts> 5.1):
                print("ABNORMAL POTASSIUM LEVELS")
            else:
                print("NORMAL POTASSIUM LEVELS")
            print("Enter the Observed Values for CHLORIDE LEVELS (BIOLOGICAL REFERENCE INTERVAL 98-107 mmol/L)")
            chl=float(input())
            if (chl<98 or chl> 107):
                print("ABNORMAL CHLORIDE LEVELS")
            else:
                print("NORMAL CHLORIDE LEVELS")

            b9 = "INSERT INTO serummelectrolytes(pno,SODIUM,POTASSIUM,CHLORIDE) VALUES (%s,%s,%s,%s)"
            b10 = (NUMBER,sdm,pts,chl)
            c.execute(b9,b10)
            mydb.commit()
            print("SERUM ELECTROLYTE Profile values Added Successfully")

        def doctor_details(self):
            mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
            c=mydb.cursor()
            xun=True
            while xun:

                print("*"*100)
                print("PRESS 1 TO ADD DOCTOR DETAILS")
                print("PRESS 2 TO UPDATE DOCTOR DETAILS")
                print("PRESS 3 TO DISPLAY DOCTOR DETAILS")
                print("PRESS 4 TO DELETE DOCTOR DETAILS")
                print("PRESS 5 TO EXIT")
                print("Enter the input")
                inpp=int(input())
                if inpp==1:

                    print("*"*100)
                    print("Welcome to WELLBEING DIAGNOSTIC LAB ")
                    print("*"*100)
                    print("----DOCTOR DETAILS----")
                    print("ENTER DOCTOR NAME")
                    dname=input()
                    print("ENTER DOCTOR ID")
                    dno=input()
                    print("ENTER DOCTOR SPECIALISATION")
                    dspl=input()
                    print("ENTER PATIENT NUMBER")
                    pnumm=int(input())
                    print("ENTER PATIENT's VISITED DATE")
                    vdate=input()
                    print("ENTER PATIENTS NEXT VISIT DAY")
                    ndate=input()

                    r1 = "INSERT INTO doctor(DOCTORNAME,D_ID,SPECIALISATION,PNO,P_DATE,NEXT_DATE) VALUES (%s,%s,%s,%s,%s,%s)"
                    r2 = (dname,dno,dspl,pnumm,vdate,ndate)
                    c.execute(r1,r2)
                    mydb.commit()
                    print("DOCTOR DETAILS Added Successfully")
                elif inpp==2:
                    c=mydb.cursor()
                    d1="SELECT * FROM doctor"
                    c.execute(d1)
                    r=c.fetchall()
                    print("Already entered Old Data")
                    for rec in r:
                       print(rec)
                    print("Enter the DOCTOR ID ")
                    ennn=int(input())
                    print("ENTER EMPLOYEE DOCTOR ATTRIBUTE YOU WANT TO UPDATE :", end="\n")
                    print("LIKE 'NAME,ID, SPECIALISATION, PNO,VISITEDDATE, NEXTDATE")
                    print("ENTER HERE :", end=" ")
                    ATTRIBUTE = input().upper()
                    if ATTRIBUTE=='NAME':
                    #print("ENTER 'OLD NAME' :", end=" ")
                    #OLD_NAME = input()
                       print("ENTER 'NEW NAME' :", end=" ")
                       NEW_NAME = input()

                       n="UPDATE doctor SET DOCTORNAME = %s WHERE D_ID=%s"
                       value=(NEW_NAME,ennn)
                       c.execute(n,value)
                       mydb.commit()
                       print("\t 'NAME UPDATED SUCCESSFULLY.")
                    elif ATTRIBUTE == 'ID':
                       print("ENTER 'OLD ID' :", end=" ")
                       OLD_ID = int(input())


                       print("ENTER 'NEW ID' :", end=" ")
                       NEW_ID = int(input())


                       n="UPDATE doctor SET D_ID = %s WHERE D_ID=%s AND D_ID=%s"
                       value=(NEW_ID,OLD_ID,ennn)
                       c.execute(n,value)
                       mydb.commit()

                       print("\t DOCTOR ID UPDATED SUCCESSFULLY.")
                       print("\n")
                    elif ATTRIBUTE == 'SPECIALISATION':
                       print("ENTER 'OLD  SPECIALISATION' :", end=" ")
                       OLD_SPL = input()


                       print("ENTER 'NEW SPECIALISATION' :", end=" ")
                       NEW_SPL = input()


                       n="UPDATE doctor SET SPECIALISATION = %s WHERE SPECIALISATION = %s and D_ID=%s"
                       value=(NEW_SPL,OLD_SPL,ennn)
                       c.execute(n,value)
                       mydb.commit()

                       print("\t SPECIALISATION UPDATED SUCCESSFULLY.")
                       print("\n")
                    elif ATTRIBUTE == 'PNO':
                       print("ENTER 'OLD PNO' :", end=" ")
                       OLD_PNO = int(input())


                       print("ENTER 'CORRECTED PNO' :", end=" ")
                       NEW_PNO = int(input())


                       n="UPDATE doctor SET PNO = %s WHERE PNO = %s and D_ID=%s"
                       value=(NEW_PNO,OLD_PNO,ennn)
                       c.execute(n,value)
                       mydb.commit()

                       print("\t GENDER UPDATED SUCCESSFULLY.")
                       print("\n")
                    elif ATTRIBUTE == 'VISITEDDATE':

                       print("ENTER 'OLD VISITEDDATE' :", end=" ")
                       OLD_VD = input()
                       print("ENTER 'CORRECTED VISITEDDATE' :", end=" ")
                       NEW_VD = input()

                       n="UPDATE doctor SET P_DATE = %s WHERE P_DATE = %s and D_ID=%s"
                       value=(NEW_VD,OLD_VD,ennn)
                       c.execute(n,value)
                       mydb.commit()
                       print("\t 'PATIENT VISITED DATE UPDATED SUCCESSFULLY.")
                    elif ATTRIBUTE == 'NEXTDATE':

                       print("ENTER 'OLD NEXT VISIT DATE' :", end=" ")
                       OLD_ND = input()
                       print("ENTER 'CORRECTED NEXT VISIT DATE' :", end=" ")
                       NEW_ND = input()

                       n="UPDATE doctor SET P_DATE = %s WHERE P_DATE = %s and D_ID=%s"
                       value=(NEW_ND,OLD_ND,ennn)
                       c.execute(n,value)
                       mydb.commit()
                       print("\t 'PATIENT NEXT VISIT DATE UPDATED SUCCESSFULLY.")

                elif inpp == 3:
                     print("="*65)
                     print("DISPLAYING DOCTOR INFORMATION : \n")
                     mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
                     c=mydb.cursor()
                     d="SELECT * FROM doctor"
                     c.execute(d)
                     r=c.fetchall()
                     for rec in r:
                        print(rec)
                #print("Enter the Employee Number whose Data you want ")
                #pnh=int(input())
                #dis="select * from employee where Enumber={}".format(pnh)
                #c.execute(dis)
                #data=c.fetchone()
                #print(data)
                     print("="*65)
                elif inpp == 4:
                    mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
                    c=mydb.cursor()
                    d="SELECT * FROM employee"
                    c.execute(d)
                    r=c.fetchall()
                    print("Already entered Old Data")
                    for rec in r:
                       print(rec)
                    print("ENTER DOCTOR's ID WHO YOU WANT TO DELETE :", end=" ")
                    NUMB = int(input())
                    mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
                    o=mydb.cursor()
                    dell="DELETE FROM doctor WHERE D_ID ={}".format(NUMB)

                    o.execute(dell)
                    mydb.commit()

                    print("DOCTOR RECORD DELETED SUCCESSFULLY")
                elif inpp==5:
                     print("THANK YOU")
                     xun=False



































        print("Do you want to add doctors details")
        print("Press 1 TO ADD 2 to NO")
        ans0=int(input())
        if ans0==1:
            doctor_details(self)

        print("="*65)
        print("Enter the observed Test Result Values")
        print("="*65)
        print(" Enter the BMI Values")
        BMI()

        print("Do you want to add Blood Profile Values")
        print("Press 1 TO ADD 2 to NO")
        ans1=int(input())
        if ans1==1:
            hy=1
            bpb.append(hy)


            print(" Enter the Blood Profile Values")
            BloodProfile()



        print("Do you want to add Lipid Profile Values")
        print("Press 1 TO ADD 2 to NO")
        ans2=int(input())
        if ans2==1:

            print(" Enter the Lipid Profile Values")
            lipidprofile()
        print("Do you want to add Renal Profile Values")
        print("Press 1 TO ADD 2 to NO")
        ans3=int(input())
        if ans3==1:
            print(" Enter the Renal Profile Values")
            renalprofile()
        print("Do you want to add Serum Electrolyte Values")
        print("Press 1 TO ADD 2 to NO")
        ans4=int(input())
        if ans4==1:
            print(" Enter the Serum Electrolyte Profile Values")
            serum_electrolytes()




    def employee_details(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
        c=mydb.cursor()
        wun=True
        while wun:

            print("*"*100)
            print("PRESS 1 TO ADD EMPLOYEE DETAILS")
            print("PRESS 2 TO UPDATE EMPLOYEE DETAILS")
            print("PRESS 3 TO DISPLAY EMPLOYEE DETAILS")
            print("PRESS 4 TO DELETE EMPLOYEE DETAILS")
            print("PRESS 5 TO EXIT")
            print("Enter the input")
            inpp=int(input())
            if inpp==1:

                print("*"*100)
                print("Welcome to WELLBEING DIAGNOSTIC LAB ")
                print("*"*100)
                print("----EMPLOYEE DETAILS----")
                print("ENTER EMPLOYEE NAME")
                ename=input()
                print("ENTER EMPLOYEE NUMBER")
                eno=input()
                print("ENTER EMPLOYEE AGE")
                eage=int(input())
                print("ENTER EMPLOYEE GENDER")
                egen=input()
                print("ENTER EMPLOYEE MOBILENUMBER")
                emob=input()
                print("ENTER EMPLOYEE DESIGNATION")
                edes=input()
                print("ENTER EMPLOYEE SALARY")
                esal=int(input())
                r1 = "INSERT INTO employee(name,Enumber,Age,Gender,MobileNumber,Designation,Salary) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                r2 = (ename,eno,eage,egen,emob,edes,esal)
                c.execute(r1,r2)
                mydb.commit()
                print("EMPLOYEE DETAILS Added Successfully")
            elif inpp==2:
                c=mydb.cursor()
                d1="SELECT * FROM employee"
                c.execute(d1)
                r=c.fetchall()
                print("Already entered Old Data")
                for rec in r:
                    print(rec)
                print("Enter the Employee Number ")
                enn=int(input())
                print("ENTER EMPLOYEE ATTRIBUTE YOU WANT TO UPDATE :", end="\n")
                print("LIKE 'NAME,NUMBER, AGE, GENDER,MOBILE NUMBER, DESIGNATION, SALARY")
                print("ENTER HERE :", end=" ")
                ATTRIBUTE = input().upper()
                if ATTRIBUTE=='NAME':
                    #print("ENTER 'OLD NAME' :", end=" ")
                    #OLD_NAME = input()
                    print("ENTER 'NEW NAME' :", end=" ")
                    NEW_NAME = input()

                    n="UPDATE employee SET name = %s WHERE Enumber=%s"
                    value=(NEW_NAME,enn)
                    c.execute(n,value)
                    mydb.commit()
                    print("\t 'NAME UPDATED SUCCESSFULLY.")
                elif ATTRIBUTE == 'NUMBER':
                    print("ENTER 'OLD NUMBER' :", end=" ")
                    OLD_NUMBER = int(input())


                    print("ENTER 'NEW NUMBER' :", end=" ")
                    NEW_NUMBER = int(input())


                    n="UPDATE employee SET Enumber = %s WHERE Enumber = %s and Enumber=%s"
                    value=(NEW_NUMBER,OLD_NUMBER,enn)
                    c.execute(n,value)
                    mydb.commit()

                    print("\t NUMBER UPDATED SUCCESSFULLY.")
                    print("\n")
                elif ATTRIBUTE == 'AGE':
                    print("ENTER 'OLD EMPLOYEE AGE' :", end=" ")
                    OLD_AGE = int(input())


                    print("ENTER 'NEW AGE' :", end=" ")
                    NEW_AGE = int(input())


                    n="UPDATE employee SET Age = %s WHERE Age = %s and Enumber=%s"
                    value=(NEW_AGE,OLD_AGE,enn)
                    c.execute(n,value)
                    mydb.commit()

                    print("\t AGE UPDATED SUCCESSFULLY.")
                    print("\n")
                elif ATTRIBUTE == 'GENDER':
                    print("ENTER 'OLD GENDER' :", end=" ")
                    OLD_GENDER = input()


                    print("ENTER 'CORRECT GENDER' :", end=" ")
                    NEW_GENDER = input()


                    n="UPDATE employee SET Gender = %s WHERE Gender = %s and Enumber=%s"
                    value=(NEW_GENDER,OLD_GENDER)
                    c.execute(n,value)
                    mydb.commit()

                    print("\t GENDER UPDATED SUCCESSFULLY.")
                    print("\n")
                elif ATTRIBUTE == 'MOBILENUMBER':

                     print("ENTER 'OLD MOBILENUMBER' :", end=" ")
                     OLD_MB = input()
                     print("ENTER 'NEW NAME' :", end=" ")
                     NEW_MB = input()

                     n="UPDATE employee SET MobileNumber = %s WHERE MobileNumber = %s and Enumber=%s"
                     value=(NEW_MB,OLD_MB,enn)
                     c.execute(n,value)
                     mydb.commit()
                     print("\t 'MOBILE NUMBER UPDATED SUCCESSFULLY.")
                elif ATTRIBUTE == 'DESIGNATION':
                    print("ENTER 'OLD DESIGNATION' :", end=" ")
                    OLD_DESIGNATION = input()
                    print("ENTER 'NEW DESIGNATION' :", end=" ")
                    NEW_DESIGNATION = input()

                    n="UPDATE employee SET Designation = %s WHERE Designation = %s and Enumber=%s"
                    value=(NEW_DESIGNATION,OLD_DESIGNATION,enn)
                    c.execute(n,value)
                    mydb.commit()
                    print("\t 'Designation UPDATED SUCCESSFULLY.")
                elif ATTRIBUTE == 'SALARY':
                    print("ENTER 'OLD SALARY' :", end=" ")
                    OLD_SALARY = int(input())
                    print("ENTER 'NEW SALARY' :", end=" ")
                    NEW_SALARY = int(input())

                    n="UPDATE employee SET Salary = %s WHERE Salary = %s and Enumber=%s"
                    value=(NEW_SALARY,OLD_SALARY,enn)
                    c.execute(n,value)
                    mydb.commit()
                    print("\t 'Salary UPDATED SUCCESSFULLY.")
            elif inpp == 3:
                print("="*65)
                print("DISPLAYING EMPLOYEE INFORMATION : \n")
                mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
                c=mydb.cursor()
                d="SELECT * FROM employee"
                c.execute(d)
                r=c.fetchall()
                for rec in r:
                    print(rec)
                #print("Enter the Employee Number whose Data you want ")
                #pnh=int(input())
                #dis="select * from employee where Enumber={}".format(pnh)
                #c.execute(dis)
                #data=c.fetchone()
                #print(data)
                print("="*65)
            elif inpp == 4:
                mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
                c=mydb.cursor()
                d="SELECT * FROM employee"
                c.execute(d)
                r=c.fetchall()
                print("Already entered Old Data")
                for rec in r:
                   print(rec)
                print("ENTER EMPLOYEE'S NUMBER WHO YOU WANT TO DELETE :", end=" ")
                NUMB = (input())
                mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
                o=mydb.cursor()
                dell="DELETE FROM employee WHERE Enumber ={}".format(NUMB)

                o.execute(dell)
                mydb.commit()

                print("EMPLOYEE RECORD DELETED SUCCESSFULLY")
            elif inpp==5:
                print("THANK YOU")
                wun=False
















    def DELETE_PATIENT_INFORMATION(self):
        print("DELETING PATIENT INFORMATION : \n")

        #if len(P_NAME) == 0 and len(P_NUMBER) == 0 and len(P_AGE) == 0 and len(
                #P_DISEASE) == 0 and len(P_MOBILE_NUMBER) == 0 and len(P_ADDRESS) == 0 and len(
            #P_EMAIL) == 0 and len(a) == 0 and len(q) == 0:
            #print("\n")
           # print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            #print("\n")
        #else:
        mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
        c=mydb.cursor()
        d="SELECT * FROM PINFO"
        c.execute(d)
        r=c.fetchall()
        print("Already entered Old Data")
        for rec in r:
            print(rec)
        print("ENTER PATIENT'S NUMBER :", end=" ")
        NUMB = (input())
        mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
        o=mydb.cursor()
        dell="DELETE FROM PINFO WHERE P_NUMBER ={}".format(NUMB)

        o.execute(dell)
        mydb.commit()

          #  LOC = P_NUMBER.index(NUMBER)

           # P_NUMBER.remove(P_NUMBER[LOC])
           # P_NAME.remove(P_NAME[LOC])
           # P_MOBILE_NUMBER.remove(P_MOBILE_NUMBER[LOC])
            #P_AGE.remove(P_AGE[LOC])
           # P_ADDRESS.remove(P_ADDRESS[LOC])
           # P_EMAIL.remove(P_EMAIL[LOC])
           # P_DISEASE.remove(P_DISEASE[LOC])
            #a.remove(a[LOC])
            #q.remove(q[LOC])

        print("\n")
        print("\t\t PATIENT INFORMATION DELETED SUCCESSFULLY.")
        print("\n")
    @staticmethod
    def DISPLAY_PATIENT_INFORMATION():
        print("DISPLAYING PATIENT INFORMATION : \n")
        mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
        c=mydb.cursor()
        d="SELECT * FROM PINFO"
        c.execute(d)
        r=c.fetchall()

        for rec in r:
            print(rec)


        if r==[]:
            print("No records to display")
        else:

            print("Enter the Patient Number whose Data you want ")
            pnh=int(input())
            dis="select * from pinfo where P_NUMBER={}".format(pnh)
            c.execute(dis)
            data=c.fetchone()
            print("="*65)
            print("PATIENT NUMBER",data[0])
            print("PATIENT NAME",data[1])
            print("PATIENT MOBILE NUMBER",data[2])
            print("PATIENT ADDRESS", data[3])
            print("PATIENT EMAIL", data[4])
            print("PATIENT AGE", data[5])
            print("PATIENT DISEASE", data[6])
            print()



            print("Do you want to see Blood profile ")
            print("Press 1 to YES and 2 to NO")
            anss1=int(input())
            if anss1==1:

                #if ans1==1:

                     #print("No Blood Profile Values Added")
                     #print("="*65)




                #else:

               dis1="select * from bloodprofile where pno={}".format(pnh)

               c.execute(dis1)
               dataa=c.fetchone()
               if not dataa:
                  print("No Blood Profile Values Added")
                  print("="*65)


               else:

                   print("Observed Blood Profile Values of Patient %d are"%(pnh))
                   print("PATIENT NUMBER",dataa[0])
                   print("HAEMOGLOBIN LEVELS",dataa[1])
                   print("WBC COUNT",dataa[2])
                   print("RBC COUNT", dataa[3])
                   print("PLATELETS", dataa[4])
                   print("BLOOD GLUCOSE LEVELS", dataa[5])
                   print()



            print("Do you want to see Lipid profile ")
            print("Press 1 to YES and 2 to NO")
            anss2=int(input())
            if anss2==1:


                dis2="select * from lipidddprofile where pno={}".format(pnh)
                c.execute(dis2)
                dataaa=c.fetchone()
                if not dataaa:
                    print("No Blood Profile Values Added")
                    print("="*65)
                else:
                    print("Observed Lipid Profile Values of Patient %d are"%(pnh))
                    print("="*65)
                    print("PATIENT NUMBER",dataaa[0])
                    print("TOTAL CHOLESTROL LEVELS",dataaa[1])
                    print("TRIGLYCERIDES",dataaa[2])
                    print("HDL CHOLESTROL", dataaa[3])
                    print("LDL CHOLESTROL", dataaa[4])
                    print("VLDL CHOLESTROL", dataaa[5])
                    print()
            print("Do you want to see Renal profile ")
            print("Press 1 to YES and 2 to NO")
            anss3=int(input())
            if anss3==1:


                dis3="select * from renallprofile where pno={}".format(pnh)
                c.execute(dis3)
                dataaaa=c.fetchone()
                if not dataaaa:
                    print("No Renal Profile Values Added")
                    print("="*65)
                else:
                    print("Observed Renal Profile Values of Patient %d are"%(pnh))

                    print("="*65)
                    print("PATIENT NUMBER",dataaaa[0])
                    print("BLOOD UREA ",dataaaa[1])
                    print("SERUM CREATININE",dataaaa[2])
                    print("URIC ACID", dataaaa[3])

                    print()
            print("Do you want to see Serum Electrolyte Profile profile ")
            print("Press 1 to YES and 2 to NO")
            anss4=int(input())
            if anss4==1:

                dis4="select * from serummelectrolytes where pno={}".format(pnh)
                c.execute(dis4)
                dataaaaa=c.fetchone()
                if not dataaaaa:
                    print("No SERUM ELECTROLYTES Values Added")
                else:
                    print("Observed SERUM ELECTROLYTES Values of Patient %d are"%(pnh))
                    print("="*65)
                    print("PATIENT NUMBER",dataaaaa[0])
                    print("SODIUM ",dataaaa[1])
                    print("POTASSIUM",dataaaaa[2])
                    print("CHLORIDE", dataaaaa[3])

                    print()
            print("Do you want to see DOCTOR Profile")
            print("Press 1 to YES and 2 to NO")
            anss5=int(input())
            if anss5==1:
                print("="*65)
                print("DISPLAYING DOCTOR INFORMATION : \n")
                print("Enter the PATIENT NUMBER")
                pnn=int(input())
                mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
                c=mydb.cursor()
                d="SELECT * FROM doctor where PNO ={}".format(pnn)
                c.execute(d)
                r=c.fetchone()
                print(r)



                print("="*65)







    def UPDATE_PATIENT_INFORMATION(self):
       print("UPDATE PATIENT INFORMATION : \n")


       mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
       c=mydb.cursor()
       d="SELECT * FROM PINFO"
       c.execute(d)
       r=c.fetchall()
       print("Already entered Old Data")
       for rec in r:
          print(rec)
          print()
       print("ENTER PATIENT ATTRIBUTE YOU WANT TO UPDATE :", end="\n")
       print("LIKE 'NAME,NUMBER, AGE, BMI,MOBILE NUMBER, ADDRESS, EMAIL, DISEASE.")
       print("ENTER HERE :", end=" ")
       ATTRIBUTE = input().upper()

       if ATTRIBUTE == 'NAME':
          print("ENTER 'OLD NAME' :", end=" ")
          OLD_NAME = input()
        #LOC_NAME = P_NAME.index(OLD_NAME)

          print("ENTER 'NEW NAME' :", end=" ")
          NEW_NAME = input()
        #P_NAME[LOC_NAME] = NEW_NAME
            #print("\t 'NAME UPDATED SUCCESSFULLY.")
            #print("\n")
          mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
          c=mydb.cursor()
          n="UPDATE PINFO SET P_NAME = %s WHERE P_NAME = %s"
          value=(NEW_NAME,OLD_NAME)
          c.execute(n,value)
          mydb.commit()
          print("\t 'NAME UPDATED SUCCESSFULLY.")
       elif ATTRIBUTE == 'BMI':
            print("Enter old BMI\n")
            OLD_BMI = float(input())
            #LOC_BMI = a.index(OLD_BMI)

            print("Enter height and weight again\n")
            w1 = float(input("Enter your weight in kgs\n"))
            h1 = float(input("Enter your height in metres\n"))
            a1 = bmi(w1, h1)
            #a[LOC_BMI] = a1

            print("\t 'BMI UPDATED SUCCESSFULLY.")
            print("\n")

       elif ATTRIBUTE == 'NUMBER':
            print("ENTER 'OLD PATIENT NUMBER' :", end=" ")
            OLD_NUMBER = int(input())
            #LOC_ROLL = P_NUMBER.index(OLD_ROLL_NUMBER)

            print("ENTER 'NEW ROLL NUMBER' :", end=" ")
            NEW_NUMBER = int(input())
            #P_NUMBER[LOC_ROLL] = NEW_ROLL
            mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
            c=mydb.cursor()
            n="UPDATE PINFO SET P_NUMBER = %s WHERE P_NUMBER = %s"
            value=(NEW_NUMBER,OLD_NUMBER)
            c.execute(n,value)
            mydb.commit()

            print("\t NUMBER UPDATED SUCCESSFULLY.")
            print("\n")

       elif ATTRIBUTE == 'AGE':
            print("ENTER 'OLD AGE' :", end=" ")
            OLD_AGE = int(input())
            #LOC_ROLL = P_AGE.index(OLD_AGE)

            print("ENTER 'NEW AGE' :", end=" ")
            NEW_AGE = int(input())
            #P_AGE[LOC_ROLL] = NEW_AGE
            mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
            c=mydb.cursor()
            n="UPDATE PINFO SET P_AGE = %s WHERE P_AGE = %s"
            value=(NEW_AGE,OLD_AGE)
            c.execute(n,value)
            mydb.commit()

            print("\t 'AGE UPDATED SUCCESSFULLY.")
            print("\n")

       elif ATTRIBUTE == 'ADDRESS':
            print("ENTER 'OLD ADDRESS' :", end=" ")
            OLD_ADDRESS = input()
            #LOC_ADDRESS = P_ADDRESS.index(OLD_ADDRESS)

            print("ENTER 'NEW ADDRESS' :", end=" ")
            NEW_ADDRESS = input()
            #P_ADDRESS[LOC_ADDRESS] = NEW_ADDRESS
            mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
            c=mydb.cursor()
            n="UPDATE PINFO SET P_ADDRESS = %s WHERE P_ADDRESS = %s"
            value=(NEW_ADDRESS,OLD_ADDRESS)
            c.execute(n,value)
            mydb.commit()
            print("\t 'ADDRESS UPDATED SUCCESSFULLY.")
            print("\n")

       elif ATTRIBUTE == 'EMAIL':
            print("ENTER 'OLD EMAIL' :", end=" ")
            OLD_EMAIL = input()
            #LOC_EMAIL = P_EMAIL.index(OLD_EMAIL)

            print("ENTER 'NEW EMAIL' :", end=" ")
            NEW_EMAIL = input()
            #P_EMAIL[LOC_EMAIL] = NEW_EMAIL
            mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
            c=mydb.cursor()
            n="UPDATE PINFO SET P_EMAIL = %s WHERE P_EMAIL = %s"
            value=(NEW_EMAIL,OLD_EMAIL)
            c.execute(n,value)
            mydb.commit()
            print("\t 'EMAIL - ID UPDATED SUCCESSFULLY.")
            print("\n")

       elif ATTRIBUTE == 'DISEASE':
            print("ENTER 'OLD DISEASE' :", end=" ")
            OLD_DISEASE = input()
            #LOC_CLASS = P_DISEASE.index(OLD_DISEASE)

            print("ENTER 'NEW DISEASE' :", end=" ")
            NEW_DISEASE = input()
            #P_DISEASE[LOC_CLASS] = NEW_DISEASE
            mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
            c=mydb.cursor()
            n="UPDATE PINFO SET P_DISEASE = %s WHERE P_DISEASE = %s"
            value=(NEW_DISEASE,OLD_DISEASE)
            c.execute(n,value)
            mydb.commit()
            print("\t 'DISEASE UPDATED SUCCESSFULLY.")
            print("\n")
       elif ATTRIBUTE == 'BMI':
            print("Enter old BMI' :", end=" ")
            OLD_BMI = float(input())
            #LOC_BMI = a.index(OLD_BMI)

            print("Enter The New BMI")
            NEW_BMI = input()
            #a.append[LOC_BMI] = NEW_BMI
            print("\t 'BMI UPDATED SUCCESSFULLY.")
            print("\n")
       elif ATTRIBUTE == 'MOBILE NUMBER':
            print("ENTER 'OLD MOBILE NUMBER' :", end=" ")
            OLD_MOBILE = input()

            print("ENTER 'NEW MOBILE NUMBER' :", end=" ")
            NEW_MOBILE = input()




            #LOC_MOBILE = P_MOBILE_NUMBER.index(OLD_MOBILE)
            #P_MOBILE_NUMBER[LOC_MOBILE] = NEW_MOBILE
            mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
            c=mydb.cursor()
            n="UPDATE PINFO SET P_MOBILE_NUMBER = %s WHERE P_MOBILE_NUMBER = %s"
            value=(NEW_MOBILE,OLD_MOBILE)
            c.execute(n,value)
            mydb.commit()
            print("\t 'MOBILE NUMBER UPDATED SUCCESSFULLY.")
            print("\n")




class billing(HEALTHISWEALTH):

    def bills(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='root123', database='patientt')
        c=mydb.cursor()
        b = HEALTHISWEALTH()
        bp=0
        e,f,g,h=0,0,0,0
        print("THANK YOU FOR CHOOSING 'WELLBEING DIAGNOSTIC PORTAL' ")
        print("Enter Pno")
        i = int(input())

        dis="select * from pinfo where P_NUMBER={}".format(i)
        c.execute(dis)
        data=c.fetchone()
        print("="*65)
        print("PATIENT NAME",data[1])
        print("PATIENT CONTACT.NO", data[2])
        dis1="select * from bloodprofile where pno={}".format(i)
        c.execute(dis1)
        dataa=c.fetchone()
        if not dataa:
            bp=bp+0
        else:
            bp=bp+1080
            e=1
        dis3="select * from lipidddprofile where pno={}".format(i)
        c.execute(dis3)
        dataaa=c.fetchone()
        if not dataaa:
            bp=bp+0
        else:
            bp=bp+600
            f=1

        dis4="select * from renallprofile where pno={}".format(i)
        c.execute(dis4)
        dataaaa=c.fetchone()
        if not dataaaa:
            bp=bp+0
        else:
            bp=bp+500
            g=1
        dis4="select * from serummelectrolytes where pno={}".format(i)
        c.execute(dis4)
        dataaaa=c.fetchone()
        if not dataaaa:
            bp=bp+0
        else:
            bp=bp+700
            h=1












        if e==1:

             print("TESTS DONE : BLOOD_PROFILE-----RS 1080 ")
        if f==1:

            print("TESTS DONE : LIPID_PROFILE-----RS 600 ")
        if g==1:

            print("TESTS DONE : RENAL_PROFILE-----RS 500 ")
        if h==1:

            print("TESTS DONE : SERUM_ELECTROLYTE-----RS 700 ")
        if e==0 and f==0 and g==0 and h==0:
            print(" no tests done")



        print("TOTAL BILL IS ", bp)



HIW = HEALTHISWEALTH()
bill = billing()

if __name__ == '__main__':

    print("\n")

    pun=True
    print("\t\t\t\t ' ********** WELCOME TO WELLBEING DIAGNOSTIC PORTAL ********** ' \n")
    while pun:

        print("Enter 1 for ADMIN 2 for PATIENT-GUARDIAN")

        inn=int(input())
        #password=12345

        if(inn==1):
            print("Enter the password")
            p=int(input())
            if (p==12345):
                print("Login succeessful")


                run=True
                while run:



                     print("PRESS FROM THE FOLLOWING OPTION : \n")

                     print("PRESS 1 : TO ADD PATIENT INFORMATION.")
                     print("PRESS 2 : TO DELETE PATIENT INFORMATION.")
                     print("PRESS 3 : TO UPDATE PATIENT INFORMATION.")
                     print("PRESS 4 : TO DISPLAY PATIENT INFORMATION.")
                     print("PRESS 5 : FOR EMPLOYEE DETAILS")
                     print("PRESS 6 : TO BILL")
                     print("PRESS 7: TO EXIT SYSTEM.")

                     OPTION = int(input("ENTER YOUR OPTION : "))
                     print("\n")
                     print(end="\n")

                     if OPTION == 1:
                        HIW.ADD_PATIENT_INFORMATION()
                     elif OPTION == 2:
                        HIW.DELETE_PATIENT_INFORMATION()
                     elif OPTION == 3:
                        HIW.UPDATE_PATIENT_INFORMATION()
                     elif OPTION == 4:
                        HIW.DISPLAY_PATIENT_INFORMATION()
                     elif OPTION == 5:
                         HIW.employee_details()

                     elif OPTION == 6:
                        bill.bills()

                     elif OPTION == 7:
                        print("THANK YOU ! VISIT AGAIN.")
                        run = False

                     else:
                         print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.")
                         print("\n")
            else:
                print("WRONG PASSWORD")
        elif(inn==2):

           print("\n")
           print(end="\n")
           print("PRESS 4 : TO DISPLAY PATIENT INFORMATION.")
           print("PRESS 9 : TO EXIT SYSTEM.")
           OPTION = int(input("ENTER YOUR OPTION : "))
           if OPTION == 4:
              HIW.DISPLAY_PATIENT_INFORMATION()
           elif OPTION == 9:
              print("THANK YOU ! VISIT AGAIN.")
              run = False
           else:

               print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.")
               print("\n")
        elif(inn==3):
            print("THANK YOU ! VISIT AGAIN.")
            pun = False

