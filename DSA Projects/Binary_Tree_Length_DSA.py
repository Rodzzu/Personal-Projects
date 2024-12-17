class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.data = x

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is not None:
                queue.append(temp.left)
            else:
                temp.left = Node(x)
                return

            if temp.right is not None:
                queue.append(temp.right)
            else:
                temp.right = Node(x)
                return

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data, end=' ')
        self.in_order(node.right)

    def pre_order(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=' ')

    def search(self, value):
        if self.root is None:
            return False

        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.data == value:
                return True
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return False

    def calculate_height(self, node):
        if node is None:
            return -1
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        return 1 + max(left_height, right_height)


# Values: 10, 6, 15, 3, 8, 12, 20

x = BinaryTree()
x.insert(10)
x.insert(6)
x.insert(15)
x.insert(3)
x.insert(8)
x.insert(12)
x.insert(20)

print("In-Order Traversal:", end=' ')
x.in_order(x.root)
print("\nPre-Order Traversal:", end=' ')
x.pre_order(x.root)
print("\nPost-Order Traversal:", end=' ')
x.post_order(x.root)

# Search
print("\nSearching for 6:", x.search(6))
print("Searching for 21:", x.search(21))

# Calculate Height
print("Height of the Tree:", x.calculate_height(x.root))

