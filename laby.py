#==============================
# Laby class
# - Create a Binary tree
#
#==============================

class Node():
	def __init__(self,data):
		self.right = None
		self.left = None
		self.data = data

class BinaryTree():

	def __init__(self): 
		self.root = None 

	def addNode(self,data):
		return Node(data)

	def insert(self,root,data):
		if root == None:
			return self.addNode(data)
		else:
			if data <= root.data:
				root.left = self.insert(root.left,data)
			else:
				root.right = self.insert(root.right,data)

			return root

	def printTree(self, root):
		if root == None:
 			pass
 		else:
  			self.printTree(root.left)
  			print root.data,
   			self.printTree(root.right)

T = BinaryTree()
root = T.addNode(0)
T.insert(root,5)
T.insert(root,5)
T.insert(root,6)
T.insert(root,3)
T.insert(root,(-1))
T.printTree(root)