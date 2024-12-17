# Stack
stack = [1, 2, 3, 4, 5]

def insert_at_bottom(stack, item):
    # Base case: If stack is empty, insert the item
    if not stack:
        stack.append(item)
    else:
        # Remove the top element and call insert_at_bottom recursively
        temp = stack.pop()
        insert_at_bottom(stack, item)
        # Push the removed item back after the insertion
        stack.append(temp)

# Recursive function to reverse the stack
def reverse_stack(stack):
    # Base case: If stack is empty, return
    if not stack:
        return
    # Remove the top element
    temp = stack.pop()
    # Recursively reverse the remaining stack
    reverse_stack(stack)
    # Insert the removed element at the bottom of the reversed stack
    insert_at_bottom(stack, temp)

# Original Stack
print("Original Stack:", stack)

# Recursive/Reverse Func
reverse_stack(stack)

# Reversed Stack
print("Reversed Stack:", stack)
