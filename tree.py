#==============================
# Laby class
# - Create a Binary tree
# - Chose the content of the node by adding attribut
#==============================

class Node():
	def __init__(self,data):
		# Minimum to create a binary tree
		self.right = None
		self.left = None
		self.data = data

		# Other variable for the use in maze.py
		self.wall = None #wall orientation
		self.x = 0 #absolute coordinates of start of box represented by the node
		self.y = 0 #seWidth, Height : Positive; -- widht and height of box
		self.width = None
		self.height = None
		self.wallOffset = 0  #offset of wall with respect to box start
		self.doorOffset = 0 #offset of door with respect to box start

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