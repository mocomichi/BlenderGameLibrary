'''
Created on 2016/06/22

@author: 大地
'''
from BasicShape.Base import Base
import bgl  # @UnresolvedImport


class Cube(Base):
    '''
    立方体描写クラス
    '''


    def __init__(self, pos, size, rot=[0, 0, 0, 1]):
        '''
        *第一引数:位置(中心基準)
        *第二引数:サイズ（辺の長さは２倍になります）
        第三引数:クオータニオン形式で回転;例（30,1,0,0)→x軸回り30度回転
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.pos = pos
        self.size = size
        self.rot = rot

    def draw(self):
        self.animationDraw()
        self.prepare3d()

        A = (self.pos[0] - self.size, self.pos[1] + self.size, self.pos[2] + self.size)
        B = (self.pos[0] + self.size, self.pos[1] + self.size, self.pos[2] + self.size)
        C = (self.pos[0] + self.size, self.pos[1] + self.size, self.pos[2] - self.size)
        D = (self.pos[0] - self.size, self.pos[1] + self.size, self.pos[2] - self.size)
        E = (self.pos[0] - self.size, self.pos[1] - self.size, self.pos[2] + self.size)
        F = (self.pos[0] + self.size, self.pos[1] - self.size, self.pos[2] + self.size)
        G = (self.pos[0] + self.size, self.pos[1] - self.size, self.pos[2] - self.size)
        H = (self.pos[0] - self.size, self.pos[1] - self.size, self.pos[2] - self.size)

        bgl.glRotatef(*self.rot)

        # Top face
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glColor3f(0.0, 1.0, 0.0)
        bgl.glVertex3f(*A)
        bgl.glVertex3f(*B)
        bgl.glVertex3f(*C)
        bgl.glVertex3f(*D)
        bgl.glEnd()

        # Bottom face
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glColor3f(1.0, 0.5, 0.0)
        bgl.glVertex3f(*E)
        bgl.glVertex3f(*H)
        bgl.glVertex3f(*G)
        bgl.glVertex3f(*F)
        bgl.glEnd()

        # Front face
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glColor3f(1.0, 0.0, 0.0)
        bgl.glVertex3f(*A)
        bgl.glVertex3f(*E)
        bgl.glVertex3f(*F)
        bgl.glVertex3f(*B)
        bgl.glEnd()

        # Back face
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glColor3f(1.0, 1.0, 0.0)
        bgl.glVertex3f(*D)
        bgl.glVertex3f(*C)
        bgl.glVertex3f(*G)
        bgl.glVertex3f(*H)
        bgl.glEnd()

        # Left face
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glColor3f(0.0, 0.0, 1.0)
        bgl.glVertex3f(*A)
        bgl.glVertex3f(*D)
        bgl.glVertex3f(*H)
        bgl.glVertex3f(*E)
        bgl.glEnd()

        # Right face
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glColor3f(1.0, 0.0, 1.0)
        bgl.glVertex3f(*B)
        bgl.glVertex3f(*F)
        bgl.glVertex3f(*G)
        bgl.glVertex3f(*C)
        bgl.glEnd()

        self.end3d()

    def move(self, movement):
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]
        self.pos[2] += movement[2]

    def rotate(self, angle):
        self.rot[0] += angle

