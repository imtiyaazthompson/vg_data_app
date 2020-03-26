# Advanced Terminal Windowing Client
# An object oriented Wrapper for the tui library
from tui import *


class Window:

	def __init__(self,tag,height,width,y,x):
		self.tag = tag
		self.height = height
		self.width = width
		self.y = y # Relative to main window stdscr
		self.x = x # Relative to main window stdscr
		self.instance = window(self.height,self.width,self.y,self.x)
		boxify(self.instance,'-','+')
		self.curs_pos = (1,1) # Track the current position of cursor in window
	
	# Write text to the given window
	# Pass in colors and attr as constants
	# from the tAPP class
	def paint(self,text,color,attr):
		mvrender(self.curs_pos[0],self.curs_pos[1],text,self.instance,color,attr)
		ln,col = (0,0)
		self.curs_pos = cursor_pos(self.instance)
		self.wait()


	# Set the current cursor position of a window
	# to the next line of a window
	def newline(self):
		ln = self.curs_pos[0] + 1
		self.curs_pos = (ln,1)


	# Read input from the user, a limit is the edge of the window
	# Given by the window width	
	def read(self):
		uncloak()
		limit = self.width - self.curs_pos[1] # tui.read() must be fixed TODO
		usr_input = read(self.instance,self.curs_pos[0],self.curs_pos[1],limit)
		self.newline()
		self.paint(usr_input,set_color(1,YLW),BOLD)


	# Blocks application by calling unicurses.getch()
	# Waits for a a key to be pressed
	def wait(self):
		return byte(self.instance)
	

	# Row/Height x Col/Width
	def get_dimensions(self):
		return (self.height,self.width)


	# Relative positioning in main window stdscr
	def get_relative_pos(self):
		return (self.y,self.x)
	
	# Return the window instance of the Window
	def get_instance(self):
		return self.instance


	def get_curs_pos(self):
		return self.curse_pos # Line, Column

# Will be init in tApp class
stdscr = setup()
win = Window('main',30,35,5,5)
win.paint('Hello, World',set_color(1,RED),BOLD)
win.newline()
win.paint('On the next line',set_color(1,GRN),UNDERLN|BOLD)
win.newline()
win.paint('>> ',set_color(1,RED),NORMAL)
win.read()
win.wait()
terminate()


