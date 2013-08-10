#=============
# Laby.py
# - Create the binary to represent the laby
# - Create the SVG file
#=============

import random
import tree
import svg
from my_log import *

def alea(a,b):
	return random.randint(a,b)



class Lab():

	def __init__(self,W,H):
		self.T = tree.BinaryTree()
		self.W = W
		self.H = H
		self.root = self.Lab_Random(W,H)

	def Lab_Random(self,W,H):
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
			logging.info('horizontal')
			Height_Left = alea(1,H-1)
			Height_Right = (H - Height_Left)
			Door_Offset = alea(1,W)
			Wall = 'horizontal'
			Wall_Offset = Height_Left
		elif (W > H):
			logging.info('vertical')
			Width_Left = alea(1,W-1)
			Width_Right = W - Width_Left
			Door_Offset = alea(1,H)
			Wall = 'vertical'
			Wall_Offset = Width_Left
		else:
			if alea(0,1) == 1:
				logging.info('horizontal')
				Height_Left = alea(1,H-1)
				Height_Right = (H - Height_Left)
				Door_Offset = alea(1,W)
				Wall = 'horizontal'
				Wall_Offset = Height_Left
			else:
				logging.info('vertical')
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

		Node.left = self.Lab_Random(Width_Left,Height_Left)
		Node.right = self.Lab_Random(Width_Right,Height_Right)

		return Node;

	def printLab(self,name):
		self.F = svg.SVGFile(name)
		Pas = 10
		self.F.write_header(self.W*Pas,self.H*Pas)
		self.Tree_SVG(self.root)
		self.F.write_footer()
		self.F.write_in_file()
		

	def Tree_SVG(self,Node):
		Constante_Pas = 10
	
		if Node.wall == 'no_wall':
			return
		elif Node.wall == 'horizontal':	
			logging.info('svg : horizontal')    
			A_X = Node.x
			A_Y = Node.y + (Node.wallOffset)*Constante_Pas
			B_Y = A_Y
			B_X = A_X + (Node.width)*Constante_Pas
			
			C_Y = A_Y
			D_Y = B_Y
			C_X = A_X + (Node.doorOffset-1)*Constante_Pas
			D_X = A_X + (Constante_Pas)
			
			self.F.write_line(A_X,A_Y,C_X,C_Y)
			self.F.write_line(D_X,D_Y,B_X,B_Y)
			
			Node.left.x = Node.x
			Node.left.y = Node.y
			Node.right.x = Node.x
			Node.right.y = A_Y
		else:
			logging.info('svg : vertical')
			A_Y = Node.y
			A_X = Node.x + (Node.wallOffset)*Constante_Pas
			B_X = A_X
			B_Y = A_Y + (Node.height)*Constante_Pas
			
			C_X = A_X
			D_X = B_X
			C_Y = A_Y + (Node.doorOffset-1)*Constante_Pas
			D_Y = A_Y + (Constante_Pas)
			
			self.F.write_line(A_X,A_Y,C_X,C_Y)
			self.F.write_line(D_X,D_Y,B_X,B_Y)
			
			Node.left.x = Node.x
			Node.left.y = Node.y
			Node.right.x = Node.x
			Node.right.y = A_X
	    

		self.Tree_SVG(Node.left)
		self.Tree_SVG(Node.right)


S = Lab(3,3)
S.printLab('lab10.svg')
