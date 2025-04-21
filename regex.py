import re
from datetime import datetime

#---------------Person Name Validation--------------------------
x = True
while x:
    pattern = re.compile(r'^[A-Za-z .]+$')# allows name characters and space and . to differ surname
    text = input("Enter Your Name: ")
    res = pattern.fullmatch(text)
    if res != None:
        global name
        name=res.group()
        break
    else:
        print("Enter Name in Correct Format !")

#-------------------------Date of Birth-----------------------------
while True:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    text = input("Enter Date of Birth [dd-mm-yyyy]: ")#date of birth need to enter in dd-mm-yyyy format
    res = pattern.fullmatch(text)
    if res != None:
        global dob
        dob = res.group()
        d=datetime.strptime(dob,"%d-%m-%Y")
        dob=d.strftime("%d %B %Y")
        break
    else:
        print("Enter DOB in Correct Format !")

#-------------------------Email id--------------------------------
        

while True:
    pattern = re.compile(r'[a-z0-9]+@gmail.com\Z')
    text = input("Enter Email id: ")
    res = pattern.fullmatch(text)
    if res != None:
        global mailid
        mailid = res.group()
        break
    else:
        print("Enter Mail id in correct format !")

            
#--------------------Mobile Number---------------------------------
while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    text = input("Enter Mobile Number [XXX-XXX-XXXX]: ")
    res = pattern.fullmatch(text)
    if res != None:
        global mobile
        mobile = res.group().replace("-","")
        break
    else:
        print("Enter Mobile Number in correct Format !")

print(f"Name : {name}")
print(f"Date of Birth: {dob}")
print(f"Mail id: {mailid}")
print(f"Mobile : {mobile}")






    
