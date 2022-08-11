import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="505050",
    database="covid19_Db",
)
mycursor=mydb.cursor()
# mycursor.execute("create table cases_data(name varchar(100),age int,gender varchar(50),address varchar(200),ph_num DOUBLE PRIMARY KEY, covid_status varchar(200), state varchar(50),zone varchar(50), status varchar(200) )")
# print("successfully table created")
# def Cases_about():
#     print("****Cases regsiter  in India*****")
#     sql="insert into cases_data(name,age,gender,address,ph_num,covid_status,state,zone,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     name=input("enter your Name: ").upper()
#     age=int(input("enter your Age: "))
#     gender=input("enter gender:").upper()
#     address=input("enter your ADDRESS: ").upper()
#     ph=int(input("enter ph_num: "))
#     covid=input("enter positive or negative: ").upper()
#     state=input("enter state name : ").upper()
#     zone=input("enter Zone where are you:  ").upper()
#     status=input("normal or treatment: ").upper()
#     val=(name,age,gender,address,ph,covid,state,zone,status)
#     mycursor.execute(sql,val)
#     mydb.commit()
#     print("data saved suuceesfuuly")
    
def view_about1():
    print("****Cases History in District Wise in India*****")
    print("------- these are restricted areas not allowed to travelled -----------" )
    print("1. please enter city to kown affected or not:        ----->")
    print("2. please enter Corona lists  status                  ---->")
    print("3. please enter tenager age to kown                  ---->")
    print("4. Total SeniorPepole list:                          ---->")
    print("5. covid Male list                                   ----->")
    print("6. covid Female list                                 ----->")
    print("7. exit                                              ----->")
    choice = input("please enter choice : ")
    if choice == '1':
        district_cases()
    elif choice == '2':
        Corona_list()
    elif choice == '3':
        Tenager_list()
    elif choice == '4':
         SeniorPepole_list()
    elif choice == '5':
        Male_ist()
    elif choice=='6':
        Female_list
    elif choice=='7':
        exit
    else:
        print("**mismatch**")
    return view_about1()
# data=(name,age,gender,address,ph_num,covid_status,state,zone,status) 
def district_cases():
    cd=input("enter type area to kown safe or not:  ")
    sql= f"select * from covid19_Db.cases_data where  address ='{cd}'"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for row in myresult:
        print('------------------------------------------')
        print("Name          = ", row[0], )
        print("Address       = ", row[3])
        print("Covid         = ", row[5])
        print("Zone          = ", row[7], "\n")
        print("-----------------------------------------")
        if 'tamilnadu' in row:
            print(mycursor.rowcount,"----- State data is found--------")
    return view_about1()
# data=(name,age,gender,address,ph_num,covid_status,state,zone,status)
def Corona_list():
    print("****** corono Positive list in Around India *******")
    ad=input("enter covid (pos or neg) to avoid contact :  ")
    sql= f"SELECT * FROM covid19_Db.cases_data where covid_status ='{ad}'"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for row in myresult:
        print('------------------------------------------')
        print("Name          = ",row[0], )
        print("Age           =",row[1])
        print("Gender        =",row[2])
        print("Covid         = ",row[4])
        print("zone          =", row[7])
        print("state         = ",row[6], "\n")
        print("-----------------------------------------")
        if 'covid_status' in row:
            print(mycursor.rowcount,"----- restricted area  is found--------")
    return view_about1()
# data=(name,age,gender,address,ph_num,covid_status,state,zone,status)
def Tenager_list():
    print("****** Tenager List in states and Country *******")
    sql= "SELECT * FROM covid19_Db.cases_data WHERE age<18"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for row in myresult:
        print('------------------------------------------')
        print("Name          = ", row[0], )
        print("Age           = ", row[1])
        print("Gender        = ", row[2])
        print("Covid         = ", row[5])
        print("Status        = ", row[8], "\n")
        print("-----------------------------------------")
        if 'age' in row:
            print(mycursor.rowcount,"----- Tenager_Age data is found--------")
    return view_about1()
# data=(name,age,gender,address,ph_num,covid_status,state,zone,status)
def SeniorPepole_list():
    print("****** Seniorpeople List in states and Country *******")
    sql= "SELECT * FROM covid19_Db.cases_data WHERE age>50"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for row in myresult:
        print('------------------------------------------')
        print("Name          = ", row[0], )
        print("Age           = ", row[1])
        print("Gender        = ", row[2])
        print("Covid         = ", row[5])
        print("Status        = ", row[8], "\n")
        print("-----------------------------------------")
        if 'age' in row:
            print(mycursor.rowcount,"----- Tenager_Age data is found--------")
    return view_about1()
# data=(name,age,gender,address,ph_num,covid_status,state,zone,status)   
def Male_ist():
    print("****** Male List in states and Country *******")
    sql= "SELECT * FROM covid19_Db.cases_data  where gender ='male'"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for row in myresult:
        print('------------------------------------------')
        print("Name          = ", row[0], )
        print("Age           = ", row[1])
        print("Gender        = ", row[2])
        print("Covid         = ", row[5])
        print("state        = ",  row[6], "\n")
        print("-----------------------------------------")
        if '' in row:
            print(mycursor.rowcount,"----- Female data is found--------")
    return view_about1()
    
# data=(name,age,gender,address,ph_num,covid_status,state,zone,status)
def  Female_list():
    print("****** Female List in states and Country *******")
    sql= "SELECT * FROM covid19_Db.cases_data  where gender ='female'"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for row in myresult:
        print('------------------------------------------')
        print("Name          = ", row[0], )
        print("Age           = ", row[1])
        print("Gender        = ", row[2])
        print("Covid         = ", row[5])
        print("state        = ",  row[6], "\n")
        print("-----------------------------------------")
        if '' in row:
            print(mycursor.rowcount,"----- Female data is found--------")
    return view_about1()

view_about1()

# ****Cases History in District Wise in India*****
# ------- these are restricted areas not allowed to travelled -----------
# 1. please enter city to kown affected or not:        ----->
# 2. please enter Corona lists  status                  ---->
# 3. please enter tenager age to kown                  ---->
# 4. Total SeniorPepole list:                          ---->
# 5. covid Male list                                   ----->
# 6. covid Female list                                 ----->
# 7. exit                                              ----->
# please enter choice : 1
# enter type area to kown safe or not:  trichy
# ------------------------------------------
# Name          =  FARVIN
# Address       =  TRICHY
# Covid         =  NEG
# Zone          =  YELLOW

# -----------------------------------------
# ------------------------------------------
# Name          =  AMEER
# Address       =  TRICHY
# Covid         =  POS
# Zone          =  RED

# -----------------------------------------
# ****Cases History in District Wise in India*****
# ------- these are restricted areas not allowed to travelled -----------
# 1. please enter city to kown affected or not:        ----->
# 2. please enter Corona lists  status                  ---->
# 3. please enter tenager age to kown                  ---->
# 4. Total SeniorPepole list:                          ---->
# 5. covid Male list                                   ----->
# 6. covid Female list                                 ----->
# 7. exit                                              ----->
# please enter choice : 2
# ****** corono Positive list in Around India *******
# enter covid (pos or neg) to avoid contact :  pos
# ------------------------------------------
# Name          =  RIHAN
# Age           = 5
# Gender        = MALE
# Covid         =  888394155.0
# zone          = YELLOW
# state         =  KERALA

# -----------------------------------------
# ------------------------------------------
# Name          =  NIZAR
# Age           = 14
# Gender        = MALE
# Covid         =  994415987.0
# zone          = YELLOW
# state         =  KARNATAKA

# -----------------------------------------
# ------------------------------------------
# Name          =  AMEER
# Age           = 24
# Gender        = MALE
# Covid         =  7449227915.0
# zone          = RED
# state         =  TAMILNADU

# -----------------------------------------
# ------------------------------------------
# Name          =  RASATHI
# Age           = 40
# Gender        = FEMALE
# Covid         =  7858987845.0
# zone          = YELLOW
# state         =  ANDRAPRADESH

# -----------------------------------------
# ------------------------------------------
# Name          =  FAROOK
# Age           = 55
# Gender        = MALE
# Covid         =  9944156699.0
# zone          = YELLOW
# state         =  KERALA

# -----------------------------------------
# ------------------------------------------
# Name          =  BENNY
# Age           = 17
# Gender        = FEMALE
# Covid         =  9944156762.0
# zone          = RED
# state         =  KERALA

# -----------------------------------------
# ****Cases History in District Wise in India*****
# ------- these are restricted areas not allowed to travelled -----------
# 1. please enter city to kown affected or not:        ----->
# 2. please enter Corona lists  status                  ---->
# 3. please enter tenager age to kown                  ---->
# 4. Total SeniorPepole list:                          ---->
# 5. covid Male list                                   ----->
# 6. covid Female list                                 ----->
# 7. exit                                              ----->
# please enter choice : 3
# ****** Tenager List in states and Country *******
# ------------------------------------------
# Name          =  RIHAN
# Age           =  5
# Gender        =  MALE
# Covid         =  POS
# Status        =  NORMAL

# -----------------------------------------
# ------------------------------------------
# Name          =  NIZAR
# Age           =  14
# Gender        =  MALE
# Covid         =  POS
# Status        =  NORMAL

# -----------------------------------------
# ------------------------------------------
# Name          =  BENNY
# Age           =  17
# Gender        =  FEMALE
# Covid         =  POS
# Status        =  NORMAL

# -----------------------------------------
# ****Cases History in District Wise in India*****
# ------- these are restricted areas not allowed to travelled -----------
# 1. please enter city to kown affected or not:        ----->
# 2. please enter Corona lists  status                  ---->
# 3. please enter tenager age to kown                  ---->
# 4. Total SeniorPepole list:                          ---->
# 5. covid Male list                                   ----->
# 6. covid Female list                                 ----->
# 7. exit                                              ----->
# please enter choice : 4
# ****** Seniorpeople List in states and Country *******
# ------------------------------------------
# Name          =  FAROOK
# Age           =  55
# Gender        =  MALE
# Covid         =  POS
# Status        =  NORMAL

# -----------------------------------------
# ****Cases History in District Wise in India*****
# ------- these are restricted areas not allowed to travelled -----------
# 1. please enter city to kown affected or not:        ----->
# 2. please enter Corona lists  status                  ---->
# 3. please enter tenager age to kown                  ---->
# 4. Total SeniorPepole list:                          ---->
# 5. covid Male list                                   ----->
# 6. covid Female list                                 ----->
# 7. exit                                              ----->
# please enter choice : 5
# ****** Male List in states and Country *******
# ------------------------------------------
# Name          =  SATHICK
# Age           =  24
# Gender        =  MALE
# Covid         =  NEG
# state        =  KARNATAKA

# -----------------------------------------
# ------------------------------------------
# Name          =  RIHAN
# Age           =  5
# Gender        =  MALE
# Covid         =  POS
# state        =  KERALA

# -----------------------------------------
# ------------------------------------------
# Name          =  NIZAR
# Age           =  14
# Gender        =  MALE
# Covid         =  POS
# state        =  KARNATAKA

# -----------------------------------------
# ------------------------------------------
# Name          =  AMEER
# Age           =  24
# Gender        =  MALE
# Covid         =  POS
# state        =  TAMILNADU

# -----------------------------------------
# ------------------------------------------
# Name          =  FAROOK
# Age           =  55
# Gender        =  MALE
# Covid         =  POS
# state        =  KERALA

# -----------------------------------------
# ****Cases History in District Wise in India*****
# ------- these are restricted areas not allowed to travelled -----------
# 1. please enter city to kown affected or not:        ----->
# 2. please enter Corona lists  status                  ---->
# 3. please enter tenager age to kown                  ---->
# 4. Total SeniorPepole list:                          ---->
# 5. covid Male list                                   ----->
# 6. covid Female list                                 ----->
# 7. exit                                              ----->
# please enter choice : 6