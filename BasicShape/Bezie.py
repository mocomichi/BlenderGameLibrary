'''
Created on 2016/06/21

@author: 大地
'''
from BasicShape.Base import Base
import numpy as np
import bgl  # @UnresolvedImport


class Bezie(Base):
    """
    ベジェ曲線描写クラス
    """

    def __init__(self, start, end, color, seg=32):
        '''
        *第一引数:始点
        *第二引数:終点
        *第三引数:色
        第四引数:分割数
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.start = start
        self.end = end
        self.color = color
        self.seg = seg
        self.t = 1;

    def draw(self):
        self.animationDraw()
        self.prepare2d()

        P0 = np.array(self.start)
        P3 = np.array(self.end)
        # P1,P2は横幅の4分の一
        P1 = np.array(((2 * P0[0] + P3[0]) / 3), P0[1])
        P2 = np.array(((P0[0] + 2 * P3[0]) / 3), P3[1])

        bgl.glColor4f(*self.color)
        bgl.glEnable(bgl.GL_LINE_SMOOTH)
        bgl.glBegin(bgl.GL_LINE_STRIP)

        for i in range(self.seg + 1):
            P4 = (1.0 - i / self.seg) * P0 + (i / self.seg) * P1
            P5 = (1.0 - i / self.seg) * P1 + (i / self.seg) * P2
            P6 = (1.0 - i / self.seg) * P2 + (i / self.seg) * P3

            P7 = (1.0 - i / self.seg) * P4 + (i / self.seg) * P5
            P8 = (1.0 - i / self.seg) * P5 + (i / self.seg) * P6

            P9 = (1.0 - i / self.seg) * P7 + (i / self.seg) * P8
            bgl.glVertex2f(P9[0], P9[1])
        bgl.glEnd()
        bgl.glDisable(bgl.GL_LINE_SMOOTH)
        bgl.glEnable(bgl.GL_CULL_FACE)

    def animation(self):
        self.prepare2d();
        P0 = np.array(self.start)
        P3 = np.array(self.end)
        # P1,P2は横幅の3分の一
        P1 = np.array(((2 * P0[0] + P3[0]) / 3), P0[1])
        P2 = np.array(((P0[0] + 2 * P3[0]) / 3), P3[1])

        bgl.glColor4f(*self.color)
        bgl.glEnable(bgl.GL_LINE_SMOOTH)
        bgl.glBegin(bgl.GL_LINE_STRIP)

        for i in range(self.t):
            P4 = (1.0 - i / self.seg) * P0 + (i / self.seg) * P1
            P5 = (1.0 - i / self.seg) * P1 + (i / self.seg) * P2
            P6 = (1.0 - i / self.seg) * P2 + (i / self.seg) * P3

            P7 = (1.0 - i / self.seg) * P4 + (i / self.seg) * P5
            P8 = (1.0 - i / self.seg) * P5 + (i / self.seg) * P6

            P9 = (1.0 - i / self.seg) * P7 + (i / self.seg) * P8
        bgl.glVertex2f(P9[0], P9[1])
        bgl.glEnd()
        bgl.glDisable(bgl.GL_LINE_SMOOTH)

        if self.t < self.seg + 1:
            self.t += 1
