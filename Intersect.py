class Intersect:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Given three colinear points b,a, c, the function checks if


# point a lies on line segment 'bc'
def onSegment(a, b, c):
    if ((a.x <= max(b.x, c.x)) and (a.x >= min(b.x, c.x)) and
            (a.y <= max(b.y, c.y)) and (a.y >= min(b.y, c.y))):
        return True
    return False


def orientation(a, b, c):

    val = (float(a.y - b.y) * (c.x - a.x)) - (float(a.x - b.x) * (c.y - a.y))
    if (val > 0):

        # Clockwise orientation
        return 1
    elif (val < 0):

        # Counterclockwise orientation
        return 2
    else:

        # Colinear orientation
        return 0


# The main function that returns true if
# the line segment 'b0a0' and 'b1a1' intersect.
def doIntersect(b0, a0, b1, a1):

    o1 = orientation(b0, a0, b1)
    o2 = orientation(b0, a0, a1)
    o3 = orientation(b1, a1, b0)
    o4 = orientation(b1, a1, a0)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # b0 , a0 and b1 are colinear and b1 lies on segment p1q1
    if ((o1 == 0) and onSegment(b0, b1, a0)):
        return True

    # b0 , a0 and a1 are colinear and a1 lies on segment p1q1
    if ((o2 == 0) and onSegment(b0, b1, a0)):
        return True

    # b1 , a1 and b0 are colinear and b0 lies on segment p2q2
    if ((o3 == 0) and onSegment(b1, b0, a1)):
        return True

    # b1 , a1 and a0 are colinear and a0 lies on segment p2q2
    if ((o4 == 0) and onSegment(b1, a0, a1)):
        return True

    # If none of the cases
    return False



# Points to test
b0 = Intersect(7, 9)
a0 = Intersect(5, 1)
b1 = Intersect(19, 2)
a1 = Intersect(10, 25)

if doIntersect(b0, a0, b1, a1):
    print("Yes")
else:
    print("No")

b0 = Intersect(1, 0)
a0 = Intersect(0, 10)
b1 = Intersect(0, 2)
a1 = Intersect(19, 10)

if doIntersect(b0, a0, b1, a1):
    print("Yes")
else:
    print("No")

b0 = Intersect(1, 0)
a0 = Intersect(1, 0)
b1 = Intersect(1, 0)
a1 = Intersect(1, 0)

if doIntersect(b0, a0, b1, a1):
    print("Yes")
else:
    print("No")

