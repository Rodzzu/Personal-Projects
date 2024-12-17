import os

from students import StudentInfo

stud = StudentInfo()

class AddStudent:
    def __init__(self, student):
        self.student_data = student

    @staticmethod
    def clear():
        os.system('cls')

    def add_student(self, name, age, idnum, email, phone):
        students = [name, age, idnum, email, phone]
        stud.setName(name)
        stud.setAge(age)
        stud.setID(idnum)
        stud.setEmail(email)
        stud.setPhoneNum(phone)

        self.student_data.allstudents.append(students)  # Update in-memory list
        self.student_data.save_students()  # Save to file
        print(f'\nAdded Student {name} to the list.')

    def new_student(self):
        while True:
            print(f"\n========== Add New Student ==========\n")
            name = input("Enter Full Name: ")
            age = input("Enter Age: ")
            idnum = input("Enter Student ID: ")
            email = input("Enter Email Address: ")
            phone = input("Enter Phone Number: ")

            self.add_student(name, age, idnum, email, phone)
            print(stud.getName())

            choice = input("\nDo you want to add another student?(Y/N): ").lower()

            if choice == 'y':
                self.clear()
                continue
            elif choice == 'n':
                break