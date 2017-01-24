'''
Created on 2016/06/21

@author: 大地
'''
from BasicShape.Base import Base
import bgl  # @UnresolvedImport
import math


PI = math.pi

class RoundRect(Base):
    '''
    角丸四角形描写クラス
    '''


    def __init__(self, bounds, radius, color, wire=False):
        '''
        *第一引数:位置(左下基準)と大きさ;(x,y,width,height)
        *第二引数:角半径
        *第三引数:色
        第四引数:ワイヤー表示の有無
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.bounds = bounds
        self.radius = radius
        self.color = color
        self.wire = wire
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

        # 左下
        for i in range(13):
            x = self.bounds[0] + self.radius + self.radius * math.cos(PI + (PI / 2) * (i / 12))
            y = self.bounds[1] + self.radius + self.radius * math.sin(PI + (PI / 2) * (i / 12))
            bgl.glVertex2f(x, y)
        # 右下
        for i in range(13):
            x = self.bounds[0] + self.bounds[2] - self.radius + self.radius * math.cos((-PI / 2) + (PI / 2) * (i / 12))
            y = self.bounds[1] + self.radius + self.radius * math.sin((-PI / 2) + (PI / 2) * (i / 12))
            bgl.glVertex2f(x, y)
        # 右上
        for i in range(13):
            x = self.bounds[0] + self.bounds[2] - self.radius + self.radius * math.cos((PI / 2) * (i / 12))
            y = self.bounds[1] + self.bounds[3] - self.radius + self.radius * math.sin((PI / 2) * (i / 12))
            bgl.glVertex2f(x, y)
        # 左上
        for i in range(13):
            x = self.bounds[0] + self.radius + self.radius * math.cos((PI / 2) + (PI / 2) * (i / 12))
            y = self.bounds[1] + self.bounds[3] - self.radius + self.radius * math.sin((PI / 2) + (PI / 2) * (i / 12))
            bgl.glVertex2f(x, y)
        bgl.glEnd()
        bgl.glDisable(bgl.GL_POLYGON_SMOOTH)
        bgl.glDisable(bgl.GL_LINE_SMOOTH)
        bgl.glEnable(bgl.GL_CULL_FACE)

    def move(self, movement):
        self.bounds[0] += movement[0]
        self.boudns[1] += movement[1]

    def rotate(self, angle):
        self.rot[0] += angle
