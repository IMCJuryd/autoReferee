#Author: Yifan Xu
#Date: 11/11/2017
#Serve for ball tracking and Points determination

#Point is a class to store points and x and y coordiates
class Point:

	#Constructor, takes in two floats as x and y coordinates, store them
	def __init__(self, ptx, pty):
		self.ptx = ptx
		self.pty = pty

	#call x-coordinate from outerside
	def x(self):
		return self.ptx

	#call y-coordinate from outerside
	def y(self):
		return self.pty

	# spec: calculate a relative relation for self object and a line formed by mid1 and mid2 
	# param: self, (Point)mid1, (Point)mid2
	# returns:	"Left" if self is to the left or up to the line
	#			 "Right" if self is to the right or down to the line
	#			 "Center" if self is on the line
	def getDirection(self, mid1, mid2):
		newPt = Point(0,0)
		if (mid1.x() == mid2.x()):
			newx = mid1.x()
			newy = self.y()
			newPt = Point(newx, newy)
		elif (mid1.y() == mid2.y()):
			newy = mid1.y()
			newx = self.x()
			newPt = Point(newx, newy)
		else:
			slope = (mid1.y()-mid2.y())/(mid1.x()-mid2.x())
			offset = mid1.y() - slope*mid1.x()
			newslope = -1/slope
			new_off = self.y() - newslope*self.x()
			newx = (offset-new_off)/(newslope-slope)
			newy = newslope*newx + new_off
			newPt = Point(newx, newy)
		vel = self.Velocity(newPt)
		if (vel.x() < 0 or (vel.x()==0 and vel.y() > 0)):
			return "Left"
		elif (vel.x() > 0 or (vel.x()==0 and vel.y() < 0)):
			return "Right"
		else:
			return "Center"

	# spec: get the middle point of a line given start point and end point
	# param: self@a Point object, start point of a line
	#		pt2@a Point obejct, end point of a line
	# returns: Point, the middle point object
	def MidPoint(self, pt2):
		newp = Point((self.x()+pt2.x())/2, (self.y()+pt2.y())/2)
		return newp

	# spec: get the velocity/vector between two points
	# param: self, (Point)pre_
	# returns: the vector from pre_ to self
	def Velocity(self, pre_):
		return Point((self.x()-pre_.x()), (self.y() - pre_.y()))


class Table:

	# constructor, takes in four points to form a table board
	# param:	left_up@the left upper point
	#			left_down@the left down point
	#			right_up@the right upper point
	#			right_down@the right down point
	def __init__(self, left_up, left_down, right_up, right_down):
		self.leftup = left_up
		self.leftdn = left_down
		self.rightup = right_up
		self.rightdn = right_down

	#returns leftup Point
	def getLeftUp(self):
		return self.leftup

	#returns leftdown Point
	def getLeftDown(self):
		return self.leftdn

	#returns rightup Point
	def getRightUp(self):
		return self.rightup

	#returns rightdown Point
	def getRightDown(self):
		return self.rightdn

	#spec: calculate the general position of a point on a table (left or right to the net)
	#param:	self@a table
	#		pt@a point
	#returns: 	"Out" if point is out of the board
	#			"Left" if ballpoint is left to the net
	#			"Right" if ballpoint is right to the net
	def Position(self,pt):
		if (self.OutBoard(pt)):
			return "Out"
		mid1 = self.getLeftUp().MidPoint(self.getRightUp())
		mid2 = self.getLeftDown().MidPoint(self.getRightDown())
		return pt.getDirection(mid1, mid2)


	# spec: check if ballpoint is outside the board or not
	# Notice: if it hits the board, it counts as in board
	# param:	self@a Table obejct
	#		pt@a Point object
	# returns: 	True if ball is out of the board
	#			False if ball is inside the board
	def OutBoard(self, pt):
		lu = self.getLeftUp()
		rd = self.getRightDown()
		ld = self.getLeftDown()
		ru = self.getRightUp()
		# print(pt.getDirection(lu, ru))
		# print(pt.getDirection(lu, ld))
		# print(pt.getDirection(rd, ru))
		# print(pt.getDirection(ld, rd))
		if (pt.getDirection(lu, ru)=="Right" and pt.getDirection(lu, ld)=="Right" and pt.getDirection(rd, ru)=="Left" and pt.getDirection(ld, rd)=="Left"):
			return False
		elif (pt.getDirection(lu, ru)=="Center" or pt.getDirection(lu, ld)=="Center" or pt.getDirection(rd, ru)=="Center" or pt.getDirection(ld, rd)=="Center"):
			return False
		else:
			return True


#Main: Test Codes

#Test Case 1
# 4—————————6—————————2
# |		 	|	      |
# |		 	|	      |
# |		 	|	      |
# |		 	|	      |
# 1—————————5—————————3
point1 = Point(0,0)
point2 = Point(6,4)
point3 = Point(6,0)
point4 = Point(0,4)


newtable = Table(point4, point1, point2, point3)

pt1 = Point(0.5,0.1)
pt2 = Point(1,2)
pt3 = Point(3.5,1)
pt4 = Point(1,0)
print(pt1.x(), pt1.y())
print(newtable.OutBoard(pt1))
print(newtable.OutBoard(pt2))
print(newtable.Position(pt1))
print(newtable.Position(pt2))
print(newtable.Position(pt3))
print(newtable.Position(pt4))


#Test Case 2
point1 = Point(1,0)
point2 = Point(6,4)
point3 = Point(7,0)
point4 = Point(0,4)

anothertable = Table(point4, point1, point2, point3)

print(pt1.x(), pt1.y())
print(anothertable.OutBoard(pt1))
print(anothertable.OutBoard(pt2))
print(anothertable.Position(pt1))
print(anothertable.Position(pt2))
print(anothertable.Position(pt3))

