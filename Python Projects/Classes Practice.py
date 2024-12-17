class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Prompt the user to create multiple Person objects
num_people = int(input("How many people do you want to create?: "))

# Create Person objects and prompt user for details
for i in range(num_people):
    print(f"\nEnter details for person {i + 1}:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    # Create a new Person object with the given details
    person = Person(name, age)

    # Display the details of the created person
    print("\nDetails for the created person:")
    person.greet()

# Access and modify specific value of a specific object
index = int(input("\nEnter the index of the person you want to access: "))
if 1 <= index <= num_people:
    print("\nCurrent details:")
    person.greet()

    attribute = input("Enter the attribute you want to access (name/age): ")
    if attribute == 'name':
        print(f"The current name of person {index} is: {person.name}")
        new_name = input("Enter the new name: ")
        person.name = new_name
    elif attribute == 'age':
        print(f"The current age of person {index} is: {person.age}")
        new_age = int(input("Enter the new age: "))
        person.age = new_age
    else:
        print("Invalid attribute.")
else:
    print("Invalid index.")

# Display updated details of the specific person
if 1 <= index <= num_people:
    print("\nUpdated details:")
    person.greet()
