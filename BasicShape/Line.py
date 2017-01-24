'''
Created on 2016/06/21

@author: 大地
'''
from BasicShape.Base import Base
import bgl  # @UnresolvedImport


class Line(Base):
    '''
    線描写クラス
    '''


    def __init__(self, start, end, color):
        '''
        *第一引数:始点
        *第二引数:終点
        *第三引数:色
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.start = start
        self.end = end
        self.color = color

    def draw(self):
        self.animationDraw()
        self.prepare2d()

        bgl.glColor4f(*self.color)
        bgl.glEnable(bgl.GL_LINE_SMOOTH)
        bgl.glBegin(bgl.GL_LINES)
        bgl.glVertex2f(self.start[0], self.start[1])
        bgl.glVertex2f(self.end[0], self.end[1])
        bgl.glEnd()
        bgl.glDisable(bgl.GL_LINE_SMOOTH)
        bgl.glEnable(bgl.GL_CULL_FACE)

    def updateStart(self, movement):
        self.start[0] += movement[0]
        self.start[1] += movement[1]

    def updateEnd(self, movement):
        self.end[0] += movement[0]
        self.end[1] += movement[1]

    def update(self, movement):
        self.start[0] += movement[0]
        self.start[1] += movement[1]
        self.end[0] += movement[0]
        self.end[1] += movement[1]
