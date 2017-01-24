'''
Created on 2016/06/20

@author: 大地
'''
from BasicShape.Base import Base
import bgl  # @UnresolvedImport


class Rect(Base):
    """
    四角形描写クラス
    """


    def __init__(self, bounds, color, gradient=False, wire=False):
        '''
        *第一引数:位置(左下基準)と大きさ;(x,y,width,height)
        *第二引数:色;(Red,Green,Blue,Alpha), 各0.0~1.0
        第三引数:グラデーションの有無
        第四引数:ワイヤー表示の有無
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.bounds = bounds
        self.color = color
        self.gradient = gradient
        self.wire = wire
        self.rot = [0, 0, 0, 1]


    def draw(self):
        self.animationDraw()
        self.prepare2d()
        bgl.glRotatef(*self.rot)

        if not self.wire:
            bgl.glBegin(bgl.GL_QUADS)
        else:
            bgl.glBegin(bgl.GL_LINE_LOOP)

        if self.gradient:
            bgl.glColor4f(*self.color[0])
            bgl.glVertex2f(self.bounds[0], self.bounds[1])
            bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1])
            bgl.glColor4f(self.color[1])
            bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1] + self.bounds[3])
            bgl.glVertex2f(self.bounds[0], self.bounds[1] + self.bounds[3])

        else:
            # 色
            bgl.glColor4f(*self.color)
            # 四角形の位置、幅、高さ
            bgl.glVertex2f(self.bounds[0], self.bounds[1])
            bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1])
            bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1] + self.bounds[3])
            bgl.glVertex2f(self.bounds[0], self.bounds[1] + self.bounds[3])
        bgl.glEnd()
        bgl.glEnable(bgl.GL_CULL_FACE)


    def move(self, movement):
        self.bounds[0] += movement[0]
        self.bounds[1] += movement[1]

    def rotate(self, angle):
        self.rot[0] += angle

