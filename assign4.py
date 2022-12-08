import json

try:
   file_name = "samira.json"
except FileNotFoundError:
    print('File not available')

def Choices():
    print('''___-___CRUD APPLICATION___-___
    CRUD (Create/Read/Update/Delete)
    (1) to Create
    (2) to Read
    (3) to Update
    (4) to Delete
    (5) to Exit from Application''')

def create():
    details={}
    with open (file_name, 'r') as f:
        temp=json.load(f)
    details["name"] = input("Name: ")
    details["age"] = input("Age: ")
    details["dob"] = input("DOB: ")
    details["marks"] = input("Marks: ")
    details["grade"] = input("Grade: ")
    temp.append(details)
    with open(file_name, 'w') as f:
        json.dump(temp, f, indent = 4)

def read():
    with open (file_name, 'r') as f:
        temp=json.load(f)
        i = 1
        for entry in temp:
            name = entry["name"]
            age = entry["age"]
            dob = entry["dob"]
            marks = entry["marks"]
            grade = entry["grade"]
            print(f"Roll Number: {i}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"DOB: {dob}")
            print(f"Marks: {marks}")
            print(f"Grade: {grade}")
            print('\n')
            i=i+1

def update():
    details = []
    with open (file_name, 'r') as f:
        temp=json.load(f)
        data_len=len(temp)
    print("Which roll number would you like to update: ")
    edit = input(f"Choose a number from 1 - {data_len}: \n")
    i = 1
    for entry in temp:
        if i == int(edit):
            name = entry["name"]
            age = entry["age"]
            dob = entry["dob"]
            marks = entry["marks"]
            grade = entry["grade"]
            print(f"Present Name: {name}")
            name = input("What is the new name? ")
            print(f"Present Age: {age}")
            age = input("What is the new age? ")
            print(f"Present DOB: {dob}")
            dob = input("What is the new dob? ")
            print(f"Present Marks: {marks}")
            marks = input("What is the new marks? ")
            print(f"Present Grade: {grade}")
            grade = input("What is the new grade? ")
            details.append({"name": name, "age": age, "dob": dob,"marks": marks, "grade": grade})
            i=i+1
        else:
            details.append(entry)
            i=i+1
    with open(file_name, 'w') as f:
        json.dump(details, f, indent = 4)
        print('\n')

def delete():
    read()
    details = []
    with open (file_name, 'r') as f:
        temp=json.load(f)
        data_len = len(temp)
    print("Which index number would you like to delete?")
    del_option = input(f"Choose a number from 1 to {data_len}: \n")
    i = 1
    for entry in temp:
        if i == int(del_option):
            pass
            i=i+1
        else:
            details.append(entry)
            i=i+1
    with open(file_name, 'w') as f:
        json.dump(details, f, indent = 4)
    print('\n')

while True:
    Choices()
    choice = input("\nEnter your choice: \n")
    if choice == "1":
        create()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print('You have entered the wrong input. Please choose from 1 to 5')