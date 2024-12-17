class StudentInfo:
    def __init__(self, file_name='students'):
        self.file_name = file_name
        self.allstudents = self.load_students()

#//
        # Setters Section
#//

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setID(self, idnum):
        self.id = idnum

    def setEmail(self, email):
        self.email = email

    def setPhoneNum(self, num):
        self.num = num

#//
        # Getters Section
#//

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getID(self):
        return self.id

    def getEmail(self):
        return self.email

    def getPhoneNum(self):
        return self.num

    #Display Info

    def load_students(self):
        students = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    # Separation
                    data = line.strip().split(',')
                    if len(data) == 5:  # Proper formatting
                        students.append(data)
        except FileNotFoundError:
            open(self.file_name, 'w').close()  # Create file if not exists
        return students

    def save_students(self):
        with open(self.file_name, 'a+') as file:
            for student in self.allstudents:
                file.write(','.join(student) + '\n')

    def ownInfo(self, stud_id):
        for student in self.allstudents:
            if student[2] == stud_id:
                print('\n========== Your Information ==========')
                print(
                    f'\nName: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail Address: {student[3]}\nPhone Number: {student[4]}')
                print('\n========== Nothing Follows ==========')
                return
        print("\nStudent ID not found.")



    def display_all(self):
        print('\n========== All students Information ==========')

        if not self.allstudents:
            print("\nNo students registered.")
        else:
            for student in self.allstudents:
                print(f"\nName: {student[0]} \nAge: {student[1]} \nID: {student[2]} \nEmail: {student[3]} \nPhone: {student[4]}")

        print('\n========== Nothing Follows ==========')
    def displayInfo(self):
        if not self.allstudents:
            print("\nThe list is empty, please try again.")

        else:
            idnum = input("Enter Student ID: ")

            for student in self.allstudents:
                if student[2] == idnum:  # student[2] is the ID
                    print(f"\n========== {student[0]}'s Information ==========\n")
                    print(f'\nName: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail Address: {student[3]}\nPhone Number: {student[4]}')
                    print('\n========== Nothing Follows ==========')
                    return

            print("\nStudent ID not found.")
            
    def login(self, stud_id):
        for student in self.allstudents:
            if stud_id == student[2]:
                print(f"\nWelcome {student[0]}!")
                return True
        print("\nStudent ID not found.")
        return False