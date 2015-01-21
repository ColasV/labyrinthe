#=============
# maze.py
# - Create the binary to represent the maze
# - Create the SVG file corresponding
#=============

import random
import tree
import svg

def alea(a,b):
	return random.randint(a,b)


class Maze():

	def __init__(self,W,H):
		self.T = tree.BinaryTree()
		self.W = W
		self.H = H
		self.root = self.createTree(W,H)

	#============================================
	# Create a random tree to represent the maze
	#============================================
	def createTree(self,W,H):
		Height_Left = H
		Height_Right = H
		Width_Right = W
		Width_Left = W
		Wall = 'no_wall'
		Node = self.T.addNode(W)	
		
		if W <= 1 or H <= 1:
		    Node.width = W
		    Node.height = H
		    Node.wall = Wall
		    
		    return Node;

		if (W < H):
			Height_Left = alea(1,H-1)
			Height_Right = (H - Height_Left)
			Door_Offset = alea(1,W)
			Wall = 'horizontal'
			Wall_Offset = Height_Left
		elif (W > H):
			Width_Left = alea(1,W-1)
			Width_Right = W - Width_Left
			Door_Offset = alea(1,H)
			Wall = 'vertical'
			Wall_Offset = Width_Left
		else:
			if alea(0,1) == 1:
				Height_Left = alea(1,H-1)
				Height_Right = (H - Height_Left)
				Door_Offset = alea(1,W)
				Wall = 'horizontal'
				Wall_Offset = Height_Left
			else:
				Width_Left = alea(1,W-1)
				Width_Right = W - Width_Left
				Door_Offset = alea(1,H)
				Wall = 'vertical'
				Wall_Offset = Width_Left

		Node.width = W
		Node.height = H
		Node.doorOffset = Door_Offset
		Node.wall = Wall
		Node.wallOffset = Wall_Offset

		Node.left = self.createTree(Width_Left,Height_Left)
		Node.right = self.createTree(Width_Right,Height_Right)

		return Node;


	#============================================
	# Method call to create the SVG file
	#============================================
	def createSVG(self,name):
		self.F = svg.SVGFile(name)
		Pas = 10
		self.F.write_header(self.W*Pas,self.H*Pas)
		self._Tree_SVG(self.root)
		self.F.write_footer()
		self.F.write_in_file()
		

	def _Tree_SVG(self,Node):
		Pas = 10
	
		if Node.wall == 'no_wall':
			return
		elif Node.wall == 'horizontal':	
			A_X = Node.x
			A_Y = Node.y + (Node.wallOffset)*Pas
			B_Y = A_Y
			B_X = A_X + (Node.width)*Pas
			
			C_Y = A_Y
			D_Y = B_Y
			C_X = A_X + (Node.doorOffset-1)*Pas
			D_X = C_X + (Pas)
			
			self.F.write_line(A_X,A_Y,C_X,C_Y)
			self.F.write_line(D_X,D_Y,B_X,B_Y)
			
			Node.left.x = Node.x
			Node.left.y = Node.y
			Node.right.x = Node.x
			Node.right.y = A_Y
		else:
			A_Y = Node.y
			A_X = Node.x + (Node.wallOffset)*Pas
			B_X = A_X
			B_Y = A_Y + (Node.height)*Pas
			
			C_X = A_X
			D_X = B_X
			C_Y = A_Y + (Node.doorOffset-1)*Pas
			D_Y = C_Y + (Pas)
			
			self.F.write_line(A_X,A_Y,C_X,C_Y)
			self.F.write_line(D_X,D_Y,B_X,B_Y)
			
			Node.left.x = Node.x
			Node.left.y = Node.y
			Node.right.y = Node.y
			Node.right.x = A_X
	    

		self._Tree_SVG(Node.left)
		self._Tree_SVG(Node.right)


S = Maze(100,100)
S.createSVG('lab500.svg')
