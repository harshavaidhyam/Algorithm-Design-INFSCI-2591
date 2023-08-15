
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def mirror(node):
    if (node == None):
        return
    else:

        temp = node

        mirror(node.left)
        mirror(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp


""" Helper function to print Level order traversal."""


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:

        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


# Driver code
if __name__ == "__main__":
    root1 = newNode(4)
    root1.left = newNode(2)
    root1.right = newNode(7)
    root1.left.left = newNode(1)
    root1.left.right = newNode(3)
    root1.right.left = newNode(6)
    root1.right.right = newNode(9)


    mirror(root1)

    print("\n",
          "the mirror tree(Test Case 1) : ")
    printLevelOrder(root1)

    root2 = newNode(34)
    root2.left = newNode(24)
    root2.right = newNode(96)
    root2.left.left = newNode(10)
    root2.left.right = newNode(None)
    root2.right.left = newNode(None)
    root2.right.right = newNode(None)

    mirror(root2)

    print("\n",
          "the mirror tree(Test Case 2) :")
    printLevelOrder(root2)
