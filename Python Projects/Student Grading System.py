def Highest_to_Lowest(numbers):
    ace = len(numbers) - 1
    lean = False

    while not lean:
        lean = True
        for j in range(0, ace):
            if numbers[j] < numbers[j + 1]:
                lean = False
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f"Here they are in a descending order: {numbers}")

def mini(numbers):
    ace = len(numbers) - 1
    lean = False

    while not lean:
        lean = True
        for j in range(0, ace):
            if numbers[j] < numbers[j + 1]:
                lean = False
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f"Here is your lowest: {numbers[-1]}")




def maxi(numbers):
    ace = len(numbers) - 1
    lean = False

    while not lean:
        lean = True
        for j in range(0, ace):
            if numbers[j] < numbers[j + 1]:
                lean = False
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f"Here is your highest: {numbers[0]}")





def get_student_info():
    name = input("Enter your name: ")
    subjects = int(input("How many subjects do you have?: "))
    return name, subjects

def get_subject_scores(num_subjects):
    scores = []
    total = 0
    for i in range(num_subjects):
        nums = int(input("Enter your score: "))
        total += nums
        scores.append(nums)
    print(f"These are your scores: {scores}")
    return total, len(scores), scores

def calculate_average(total, length):
    return total / length

def display_result(name, grade):
    print(f"You are {name}, and your average grade is {grade}")

info = get_student_info()
gss = get_subject_scores(info[1])
ave = calculate_average(gss[0], gss[1])
sort = Highest_to_Lowest(gss[2])
minimum = mini(gss[2])
maximum = maxi(gss[2])
display_result(info[0], ave)



