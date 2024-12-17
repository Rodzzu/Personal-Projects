class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, value):
        if not self.head:  # If the list is empty
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != value:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print("None")

linked_list = LinkedList()

linked_list.append(5)
linked_list.append(10)
linked_list.append(15)

print("Linked List after insertion:")
linked_list.print_list()

linked_list.delete_value(10)

print("Linked List after deletion of 10:")
linked_list.print_list()
