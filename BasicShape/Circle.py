'''
Created on 2016/06/20

@author: 大地
'''
from BasicShape.Base import Base
import bgl  # @UnresolvedImport
import math


class Circle(Base):

    """
    円描写クラス
    楕円の場合、スケールを調整してできます。
    """

    def __init__(self, center, radius, color, scale=[1, 1], gradient=False, wire=False):
        '''
        *第一引数:中心;(x,y)
        *第二引数:半径;(double radius)
        *第三引数:色;(Red,Green,Blue,Alpha), 各0.0~1.0
        第四引数:スケール(x,y)
        第五引数:グラデーションの有無
        第六引数:ワイヤー表示の有無
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.center = center
        self.radius = radius
        self.color = color
        self.gradient = gradient
        self.wire = wire
        self.scale = [scale[0], scale[1], 1]

    def draw(self):
        self.animationDraw()
        self.prepare2d()
        bgl.glScalef(*self.scale)
        # 色
        bgl.glColor4f(*self.color)
        # 円の描写
        if not self.wire:
            bgl.glEnable(bgl.GL_POLYGON_SMOOTH)
            bgl.glBegin(bgl.GL_POLYGON)
        else:
            bgl.glEnable(bgl.GL_LINE_SMOOTH)
            bgl.glBegin(bgl.GL_LINE_LOOP)
        for i in range(64):
            x = self.center[0] + self.radius * math.cos(2.0 * 3.14 * (i / 64))
            y = self.center[1] + self.radius * math.sin(2.0 * 3.14 * (i / 64))
            bgl.glVertex2f(x, y)
        bgl.glEnd()
        bgl.glDisable(bgl.GL_POLYGON_SMOOTH)
        bgl.glDisable(bgl.GL_LINE_SMOOTH)
        bgl.glEnable(bgl.GL_CULL_FACE)

    def move(self, movement):
        self.center[0] += movement[0]
        self.center[1] += movement[1]

    def expand(self, scale):
        self.scale[0] *= scale[0]
        self.scale[1] *= scale[1]

    def scaleUp(self, scale):
        self.radius += scale
