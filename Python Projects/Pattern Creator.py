pattern = int(input("Enter Pattern Number of Your Choice: "))
variation = int(input("Enter Number: "))

if pattern == 1:
    print("\n PATTERN 1: \n")
    for x in range(1, variation + 1):
        for a in range(1, x + 1):
            print(a, end=" ")
        print()
elif pattern == 2:
    print("\n PATTERN 2: \n")
    for x in range(variation, 0, -1):
        for a in range(1, x + 1):
            print(a, end=" ")
        print()

if pattern == 3:
    print("\n PATTERN 3: \n")
    for x in range(1, variation + 1):
        for a in range(variation - x, 0, -1):
            print(" ", end=" ")
        for c in range(x, 0, -1):
            print(c, end=" ")
        print()
elif pattern == 4:
    print("\n PATTERN 4: \n")
    for x in range(variation, 0, -1):
        for a in range(variation - x):
            print(" ", end=" ")
        for c in range(x, 0, -1):
            print(c, end=" ")
        print()
elif pattern == 5:
    print("\n PATTERN 5: \n")
    for x in range(variation, 0, -1):
        for a in range(1, x):
            print(" ", end=" ")

        print(x)