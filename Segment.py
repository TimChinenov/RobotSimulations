import numpy as np
def rot(theta):
    #Function performs a 2-D matrix rotation based on theta
    R = np.matrix([[np.cos(theta), (-1)*np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
    return R

class Segment:
    length = 0
    angle = 0
    def __init__(self,l,a):
        #zero configuration angle
        self.angle = a
        self.length = np.dot(rot(a),np.matrix([[l],[0]]))


    def getLength(self):
        return self.length
    def getMagnitude(self):
        return np.linalg.norm(self.length)

    def getAngle(self):
        return self.angle

    def setLength(self,l):
        self.length = l;

    def setAngle(self,a):
        self.angle = a;

