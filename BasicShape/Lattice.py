'''
Created on 2016/06/22

@author: 大地
'''
from BasicShape.Base import Base
import bgl  # @UnresolvedImport


class Lattice(Base):
    '''
    格子描写クラス
    '''


    def __init__(self, bounds, wseg, hseg, color):
        '''
        *第一引数:位置(左下基準)と大きさ;(x,y,width,height)
        *第二引数:横分割線の数
        *第三引数:縦分割線の数
        *第四引数:色
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.self.bounds = bounds
        self.wseg = wseg
        self.hseg = hseg
        self.color = color
        self.rot = [0, 0, 0, 1]

    def draw(self):
        self.animationDraw()
        self.prepare2d()
        bgl.glRotatef(*self.rot)

        bgl.glColor4f(*self.color)
        bgl.glBegin(bgl.GL_LINES)
        for i in range(self.wseg + 1):
            bgl.glVertex2f(self.bounds[0] + (i * self.bounds[2] / (self.wseg + 1)), self.bounds[1])
            bgl.glVertex2f(self.bounds[0] + (i * self.bounds[2] / (self.wseg + 1)), self.bounds[1] + self.bounds[3])
        for i in range(self.hseg + 1):
            bgl.glVertex2f(self.bounds[0], self.bounds[1] + (i * self.bounds[3] / (self.hseg + 1)))
            bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1] + (i * self.bounds[3] / (self.hseg + 1)))
        bgl.glEnd()
        bgl.glEnable(bgl.GL_CULL_FACE)

    def move(self, movement):
        self.bounds[0] += movement[0]
        self.bounds[1] += movement[1]

    def rotate(self, angle):
        self.rot[0] += angle
