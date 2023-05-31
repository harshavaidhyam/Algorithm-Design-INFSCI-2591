
from contextlib import nullcontext


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def areMirror(a, b):
	

	if a is None and b is None:
		return True
	

	if a is None or b is None:
		return False
	

	return (a.data == b.data and
			areMirror(a.left, b.right) and
			areMirror(a.right , b.left))

#test case 1
# root1 = Node(1)
# root2 = Node(1)

# root1.left = Node(2)
# root1.right = Node(3)
# root1.left.left = Node(4)
# root1.left.right = Node(5)
# root1.right.left = Node(6)
# root1.right.right = Node(7)

# #root2
# root2.left = Node(3)
# root2.right = Node(2)
# root2.left.left = Node(7)
# root2.left.right = Node(6)
# root2.right.left = Node(5)
# root2.right.right = Node(4)


#test case 2
root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(2)
root1.left.left = Node(3)
root1.right.left = Node(3)

#root2
root2.left = Node(2)
root2.right = Node(2)
root2.left.right = Node(3)
root2.right.right = Node(3)


if areMirror(root1, root2):
	print ("Mirror Image")
else:
	print ("Not a Mirror Image")


