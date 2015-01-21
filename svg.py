#==================================
# Python Class to create SVG File
# - SVG Header & Footer
# - Line
#
# nico.vignes@gmail.com
#==================================
import logging 
import os
import sys

class SVGFile():

	def __init__(self,name):
		self._name = name
		self._Header = ''
		self._Footer = ''
		self._Content = ''

	def write_header(self,x_size,y_size):
		self.x_size = x_size
		self.y_size = y_size

		self._Header = "<svg width=\"" + str(self.x_size) + "\" height=\"" + str(self.y_size) + "\">\n"

		logging.info("Header created : Width : " + str(self.x_size) + " height : " + str(self.y_size))

	def write_footer(self):
		self._Footer = "</svg>"

	def write_line(self,x_1,y_1,x_2,y_2):
		self._Content += "<line x1=\"" + str(x_1) + "\" y1=\"" + str(y_1) + "\" x2=\"" + str(x_2) + "\" y2=\"" + str(y_2) + "\" style=\"stroke:rgb(0,0,0);stroke-width:0.8\" />\n"

	def _open(self):
		try:
			self._File = open(self._name,'w')
			logging.info("Successfully open : " + str(self._name))
		except:
			logging.error("Can't open the file" + str(self._name))

	def write_in_file(self):
		self._open()

		self._File.write(self._Header)
		self._File.write(self._Content)
		self._File.write(self._Footer)

		self._File.close()