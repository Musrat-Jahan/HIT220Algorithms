class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node into the BST
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        elif key > root.val:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    # In-order traversal
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        if root:
            return self._inorder(root.left) + [root.val] + self._inorder(root.right)
        else:
            return []

    # Delete a node from the BST
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Search for a node
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

# Driver code
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert values
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for value in values_to_insert:
        bst.insert(value)
        print(f"After inserting {value}\n In-order traversal: {bst.inorder()}")


    # Delete value 70
    bst.delete(70)
    print("After deleting 70, in-order traversal:", bst.inorder())

    # Search for value 20
    result = bst.search(20)
    if result:
        print("Value 20 found in the BST.",  bst.inorder())
    else:
        print("Value 20 not found in the BST.",  bst.inorder())
