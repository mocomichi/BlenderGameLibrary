'''
Created on 2016/06/20

@author: 大地
'''
import bge  # @UnresolvedImport
import bgl  # @UnresolvedImport
from BasicShape.Animations import Animations


width = bge.render.getWindowWidth()
height = bge.render.getWindowHeight()

class Base(Animations):
    '''
    ウィンドウへの描写を準備するためのMix-Inクラス
    '''

    def animationDraw(self):
        # 辞書内が空の場合は削除
        self.effectFuncDictionary = { k : v for k,v in self.effectFuncDictionary.items() if v}
        # セットされているアニメーションを順次実行
        for func in self.effectFuncDictionary.values():
            func()

    def prepare2d(self):
        bgl.glMatrixMode(bgl.GL_PROJECTION)
        bgl.glLoadIdentity()
        #  gluOrtho2D(left, right, bottom, top)
        bgl.gluOrtho2D(0, width, 0, height)
        bgl.glMatrixMode(bgl.GL_MODELVIEW)
        bgl.glLoadIdentity()

        bgl.glEnable(bgl.GL_BLEND)
        bgl.glBlendFunc(bgl.GL_SRC_ALPHA, bgl.GL_ONE_MINUS_SRC_ALPHA)
        bgl.glDisable(bgl.GL_CULL_FACE)

    def prepare3d(self, prj):
        # スタックからModelViewMatrixを取り出す
        bgl.glPopMatrix()
        bgl.glMatrixMode(bgl.GL_PROJECTION)
        # ProjectionMatrixを保存したものに置き換える
        bgl.glLoadMatrixd(prj)
        # ModelViewに切り替え
        bgl.glMatrixMode(bgl.GL_MODELVIEW)

    def InitSet(self):
        # これで2Dも3Dも記述順の重なりで表示される
        bgl.glDisable(bgl.GL_DEPTH_TEST)
        prj = bgl.Buffer(bgl.GL_DOUBLE, 16)
        # ProjectionMatirxを保存
        bgl.glGetDoublev(bgl.GL_PROJECTION_MATRIX, prj)
        # ModelViewMatirxをスタックに保存
        bgl.glPushMatrix()

    def end3d(self):
        bgl.glPushMatrix()

    def test(self):
        '''テスト用'''
        mv = bgl.Buffer(bgl.GL_DOUBLE, 16)
        prj = bgl.Buffer(bgl.GL_DOUBLE, 16)
        bgl.glGetDoublev(bgl.GL_MODELVIEW_MATRIX, mv)
        print(mv)
        bgl.glGetDoublev(bgl.GL_PROJECTION_MATRIX, prj)
        print(prj)

