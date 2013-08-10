#==============================
# Laby class
# - Create a Binary tree
# - Chose the content of the node by adding attribut
#==============================

class Node():
	def __init__(self,data):
		self.right = None
		self.left = None
		self.data = data
		self.walltype = None #wall orientation
		self.x = None #absolute coordinates of start of box represented by the node
		self.y = None #seWidth, Height : Positive; -- widht and height of box
		self.width = None
		self.height = None
		self.wallOffset = None  #offset of wall with respect to box start
		self.doorOffset = None #offset of door with respect to box start

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
node = T.addNode(1)
root.left = node
node2 = T.addNode(2)
root.right = node2
T.printTree(root)