###
# Procedural approach
import math
def perimeter(polygon):
    """Given a list of vector vertices (in proper order), 
    returns the perimeter for the associated polygon."""
    sum = 0
    for i in range(len(polygon)):
        vertex1 = polygon[i]
        vertex2 = polygon[(i+1) % len(polygon)]
        distance = math.sqrt(pow(vertex2[0]-vertex1[0],2) + \
                             pow(vertex2[1]-vertex1[1],2))
        sum += distance
    return sum 

perimeter([[0,0],[1,0],[1,1],[0,1]])	# Returns 4.0
perimeter([[0,-2],[1,1],[3,3],[5,1],[4,0],[4,-3]])
# Returns 17.356451097651515

###
# Object-oriented approach
class Polygon:
    """A new class named Polygon."""
    def __init__(self, vertices=[]):
        self.vertices = vertices
        print "(Creating an instance of the class Polygon)"
    def perimeter(self):
        sum = 0
        for i in range(len(self.vertices)):
            vertex1 = self.vertices[i]
            vertex2 = self.vertices[(i+1) % len(self.vertices)]
            distance = math.sqrt(pow(vertex2[0]-vertex1[0],2)+\
                                 pow(vertex2[1]-vertex1[1],2))
            sum += distance
        return sum

a = Polygon([[0,-2],[1,1],[3,3],[5,1],[4,0],[4,-3]])
a.perimeter()
# Returns 17.356451097651515

