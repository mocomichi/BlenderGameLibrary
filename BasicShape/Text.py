'''
Created on 2016/06/20

@author: 大地
'''
from BasicShape.Base import Base
import bgl  # @UnresolvedImport
import blf  # @UnresolvedImport


class Text(Base):
    """
    テキストを描写します。基本図形の上に描写する場合、一番最後にdrawを書く必要があります。

    """


    def __init__(self, pos, size, text, color, text_align=0, vertical_align=0,
             fontPath="C:\Windows\Fonts\Meiryo.ttc", shadow=False):
        '''
        *第一引数:位置;(x,y)
        *第二引数:サイズ
        *第三引数:テキスト
        *第四引数:色;(Red,Green,Blue,Alpha), 各0.0~1.0
        第五引数:そろえ方(左、中央、右の順に0,1,2)(デフォルト:左)
        第六引数:縦のベースライン(下、中央、上の順に0,1,2)(デフォルト:下)
        第七引数:フォントパス(デフォルトでメイリオ)
        第八引数:影の有無
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}
        self.pos = pos
        self.size = size
        self.text = text

        self.color = color
        self.text_align = text_align
        self.vertical_align = vertical_align
        self.fontPath = fontPath
        self.shadow = shadow

    def draw(self):
        self.animationDraw()
        self.prepare2d()

        fid = blf.load(self.fontPath)
        # テキスト整理
        self.texts = str(self.text).split("\n")
        # サイズ
        blf.size(fid, self.size, 72)
        # 色
        bgl.glColor4f(*self.color)
        # 影
        if self.shadow:
            blf.enable(fid, blf.SHADOW)
            blf.shadow(fid, 3, 0.0, 0.0, 0.0, 1.0)
            blf.shadow_offset(fid, 0, -1)
        else:
            blf.disable(fid, blf.SHADOW)
        # テキストそろえ、改行設定
        h = blf.dimensions(fid, self.text)[1]

        if self.vertical_align == 0:
            yn = -h
        elif self.vertical_align == 1:
            yn = -h / 2
        elif self.vertical_align == 2:
            yn = 0

        for i in range(len(self.texts)):
            w = blf.dimensions(fid, self.texts[i])[0]
            xn = 0
            if self.text_align == 0:
                xn = 0
            elif self.text_align == 1:
                xn = -w / 2
            elif self.text_align == 2:
                xn = -w

            blf.position(fid, self.pos[0] + xn, self.pos[1] - i * h + yn, 1)
            blf.draw(fid, self.texts[i])
        bgl.glEnable(bgl.GL_CULL_FACE)

    def addtext(self, txt):
        self.text += txt

