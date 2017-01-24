'''
Created on 2016/06/21

@author: 大地
'''
from BasicShape.Base import Base
import numpy as np
import bgl  # @UnresolvedImport


class Arrow(Base):
    '''
    矢印描写クラス
    '''


    def __init__(self, start, end, line_width, triangle_width, height, color, wire=False):
        '''
        *第一引数:始点
        *第二引数:終点
        *第三引数:線幅
        *第四引数:先端の三角形の底辺の幅
        *第五引数:先端の三角形の高さ
        *第六引数:色
        第七引数:ワイヤー表示の有無
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.start = start
        self.end = end
        self.line_width = line_width
        self.triangle_width = triangle_width
        self.height = height
        self.color = color
        self.wire = wire

    def draw(self):
        self.animationDraw()
        self.prepare2d()

        start_np = np.array(self.start)
        end_np = np.array(self.end)

        vec = end_np - start_np
        length = np.linalg.norm(vec)
        unit_vec = vec / length
        normal_vec = np.array([-unit_vec[1], unit_vec[0]])

        v1 = (self.line_width / 2) * normal_vec
        v2 = (length - self.height) * unit_vec
        v3 = (self.triangle_width / 2) * normal_vec
        v4 = self.height * unit_vec
        # 色
        bgl.glColor4f(*self.color)

        if not self.wire:
            bgl.glBegin(bgl.GL_QUADS)
            bgl.glVertex2f(start_np[0] - v1[0], start_np[1] - v1[1])
            bgl.glVertex2f(start_np[0] - v1[0] + v2[0], start_np[1] - v1[1] + v2[1])
            bgl.glVertex2f(start_np[0] + v1[0] + v2[0], start_np[1] + v1[1] + v2[1])
            bgl.glVertex2f(start_np[0] + v1[0], start_np[1] + v1[1])
            bgl.glEnd()

            bgl.glBegin(bgl.GL_TRIANGLES)
            bgl.glVertex2f(end_np[0], end_np[1])
            bgl.glVertex2f(end_np[0] + v3[0] - v4[0], end_np[1] + v3[1] - v4[1])
            bgl.glVertex2f(end_np[0] - v3[0] - v4[0], end_np[1] - v3[1] - v4[1])

        else:
            bgl.glBegin(bgl.GL_LINE_LOOP)
            bgl.glVertex2f(start_np[0] - v1[0], start_np[1] - v1[1])
            bgl.glVertex2f(start_np[0] - v1[0] + v2[0], start_np[1] - v1[1] + v2[1])
            bgl.glVertex2f(end_np[0] - v3[0] - v4[0], end_np[1] - v3[1] - v4[1])
            bgl.glVertex2f(end_np[0], end_np[1])
            bgl.glVertex2f(end_np[0] + v3[0] - v4[0], end_np[1] + v3[1] - v4[1])
            bgl.glVertex2f(start_np[0] + v1[0] + v2[0], start_np[1] + v1[1] + v2[1])
            bgl.glVertex2f(start_np[0] + v1[0], start_np[1] + v1[1])

        bgl.glEnd()
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


