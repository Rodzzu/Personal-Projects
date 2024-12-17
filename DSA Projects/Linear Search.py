arr = ['a', 'b', 'c', 'd', 'e', 'f']

print(arr)

while True:
    print("Options: \n1.) Insert a letter \n2.) Search a letter \n3.) Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        enter = input("Enter a letter to insert: ")
        pos = int(input(f"Enter the index 0 - {len(arr)}: "))
        arr.insert(pos, enter)
        print(arr)

    elif choice == '2':
        search = input(f"Enter the value you'd like to find: ")

        if search in arr:
            index = arr.index(search)
            print(f'Value found! "{search}" is at index: {index}')
        else:
            print('Value not found!')

    elif choice == '3':
        exit()
