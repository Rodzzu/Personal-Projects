# Define the node for the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Define the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node
            self.head = new_node

        else:
            temp = self.head
            curr = 0

            while temp and curr < position - 1:
                temp = temp.next
                curr += 1

            if temp is None:
                print('Position does not exist.')
                return

        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node
        new_node.prev = temp

        del temp

    def delNode(self, position):
        if position == 0:
            self.delete_from_beginning()
            return

        temp = self.head
        curr = 0

        while temp and curr < position:
            temp = temp.next
            curr += 1

        if temp is None:
            print('Position does not exist.')
            return

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev


    # Insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  # Traverse to the last node
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # Delete a node from the beginning
    def delete_from_beginning(self):
        if self.head is None:  # List is empty
            print("List is empty. No node to delete.")
        else:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            del temp  # Free memory of the deleted node

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("None")

# Create a doubly linked list and perform operations
dll = DoublyLinkedList()

# Insert nodes at the end
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

print("Doubly Linked List after inserting elements:")
dll.display()

# Delete node from the beginning
dll.delete_from_beginning()

print("Doubly Linked List after deleting from beginning:")
dll.display()

print("Inserting a new node: ")
dll.insertNode(10, 2)
dll.insertNode(40, 1)
dll.insertNode(50, 3)
dll.display()

print("Deleting the nodes: ")
dll.delNode(3)
dll.delNode(2)
dll.delNode(1)
dll.display()

