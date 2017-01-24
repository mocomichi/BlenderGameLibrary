'''
Created on 2016/06/21

@author: 大地
'''
from BasicShape.Base import Base
import bgl  # @UnresolvedImport
import math


class Arc(Base):
    '''
    扇形描写クラス
    '''


    def __init__(self, center, radius, start_angle, angle, color, wire=False, seg=32):
        '''
        *第一引数:中心;(x,y)
        *第二引数:半径
        *第三引数:開始角度;radian
        *第四引数:中心角;radian
        *第五引数:色
        第六引数:ワイヤー表示の有無
        第七引数:分割数(デフォルトで32)
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.center = center
        self.radius = radius
        self.start_angle = start_angle
        self.angle = angle
        self.color = color
        self.wire = wire
        self.seg = seg
        self.rot = [0, 0, 0, 1]

    def draw(self):
        self.animationDraw()
        self.prepare2d()
        bgl.glRotatef(*self.rot)

        bgl.glColor4f(*self.color)
        if not self.wire:
            bgl.glEnable(bgl.GL_POLYGON_SMOOTH)
            bgl.glBegin(bgl.GL_POLYGON)
        else:
            bgl.glEnable(bgl.GL_LINE_SMOOTH)
            bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2f(self.center[0], self.center[1])

        for i in range(self.seg + 1):
            x = self.center[0] + self.radius * math.cos(self.start_angle + self.angle * (i / self.seg))
            y = self.center[1] + self.radius * math.sin(self.start_angle + self.angle * (i / self.seg))
            bgl.glVertex2f(x, y)
        bgl.glEnd()
        bgl.glDisable(bgl.GL_POLYGON_SMOOTH)
        bgl.glDisable(bgl.GL_LINE_SMOOTH)
        bgl.glEnable(bgl.GL_CULL_FACE)

    def move(self, movement):
        self.center[0] += movement[0]
        self.center[1] += movement[1]

    def rotate(self, angle):
        self.rot[0] += angle

    def scaleUp(self, scale):
        self.radius += scale

    def updateAngle(self, angle):
        self.angle += angle


