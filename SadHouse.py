
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width ,height= 500 ,500 			# window size

#house
def drawSquare(x ,y ,width ,height):
    glBegin(GL_QUADS) 			# start drawing a square
    glVertex2f(x ,y) 			# bottom left point
    glVertex2f(x + width ,y)		# bottom right point
    glVertex2f(x + width ,y + height)	# top right point
    glVertex2f(x, y + height)		# top left point
    glEnd()				# done drawing
#window
def drawSquare1(x,y,width, height):
    glBegin(GL_QUADS)
    glVertex2f(x,y)
    glVertex2f(x + width, y)
    glVertex2f(x+width, y+height)
    glVertex2f(x,y+height)
    glEnd()
#door
def drawSquare2(x ,y ,width ,height):
    glBegin(GL_QUADS) 			# start drawing a square
    glVertex2f(x ,y) 			# bottom left point
    glVertex2f(x + width ,y)		# bottom right point
    glVertex2f(x + width ,y + height)	# top right point
    glVertex2f(x, y + height)		# top left point
    glEnd()				# done drawing


#left roof
def drawTriangle(x, y , width, height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + width , y)
    glVertex2f(x + width ,y + height)
    glEnd()


#right roof
def drawTriangle1(x ,y ,width ,height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glEnd()


def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 	# clear the screen
    glLoadIdentity() 					# reset position
    refresh2d(width, height)

#house structure
    glColor3f(0,0,128) 				# set color to navy blue
    drawSquare(150 ,150 ,150 ,150) 				# draw a square at (50,50) with width 200, height 200

#first roof
    glColor3f(1.0 ,0.0 ,0.0) 				# set color to red
    drawTriangle(135 ,300 ,100 ,100)

#2nd roof
    glColor3f(250, 250, 0.0)  # set color to yellow
    drawTriangle1(235, 500, 500, 500)

#door

    glColor3f(225 ,225 ,0.0)
    drawSquare2(230 ,150 ,50, 90)

#window
    glColor3f(0,250,0)
    drawSquare1(170,190,40,40)


    glutSwapBuffers() # important for double buffering

def refresh2d(width, height):
    glViewport(0 ,0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


# initialization
glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height)  # set window size
glutInitWindowPosition(0, 0)  # set window position
wind = glutCreateWindow("CSC 322 Fall 2020 HW1")  # create window with title
glutDisplayFunc(drawScene)  # set showScreen function callback
glutIdleFunc(drawScene)  # draw all the time
glutMainLoop()  # start everything