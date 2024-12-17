from students import *
from add_student import *
from search import *
import os

def clear():
    os.system('cls') # To clear terminal

stud = StudentInfo()
search = Search()
addStud = AddStudent(stud)

AdminStudent = addStud.add_student('Admin Rodzzu', '21', '2009-2-0001', 'admin@gmail.com', '123456789') # Default Instance for the Admin
NormalStudent = addStud.add_student('Rodney', '19', '2023-2-02298', '2023-2-02298@gmail.com', '09999234567') # Default Instance for students
NormalStudent2 = addStud.add_student('Mary', '19', '2023-2-02299', '2023-2-02299@gmail.com', '09123456789') # No.2 Instance for students

# Log In
attempts = 0

while True:
    print("\nWelcome to the student portal!")
    stud_id = input("Enter ID Number: ")
    
    if stud.login(stud_id): # If stud.login() returns true...
        while True:
            print("\nChoose an option: "
            "\n1.) Check Your Info"
            "\n2.) Check Other Student's Info"
            "\n3.) Register A New Student"
            "\n4.) Print All students"
            "\n5.) Exit")
            
            try:
                choice = int(input("Enter your choice: "))
                    
                if choice == 1:
                    search.ownInfo(stud_id) # To display your own deets
                        
                elif choice == 2:
                    stud.displayInfo() # To display other students

                elif choice == 3:
                    addStud.new_student() # Add new students

                elif choice == 4:
                    stud.display_all() # To display everyone

                elif choice == 5:
                    exit() # Exit the program cuz yes

                else:
                    print("Please enter a valid option.")

                input("\nPress Enter to Continue...")
                clear() 

            except ValueError:
                print("Invalid input. Please enter a number.") # If the user can't read lmao
                input("\nPress Enter to Continue...")
                
    elif stud_id == '00': # Exit Log In
        print("\nExiting...\n")
        exit()
        
    else: # When ID does not exist.
        print("\nThis ID does not exist.")
        attempts += 1
        
        if attempts == 4:
            print("\nYou have reached the maximum attempts.")
            break




    
    
    






