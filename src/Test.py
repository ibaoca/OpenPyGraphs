
import sys

sys.path.append("Vertex.py")
import Vertex as vt

#
#		 Vertex.py test
#

index = 1
name = "Scruffy Puppy"
obj = "First object"

v = vt.Vertex(name, obj)

print v.setObject("Second object")