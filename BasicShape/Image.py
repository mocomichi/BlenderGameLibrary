'''
Created on 2016/06/25

@author: 大地
'''
from BasicShape.Base import Base
import bge  # @UnresolvedImport
import bgl  # @UnresolvedImport


width = bge.render.getWindowWidth()
height = bge.render.getWindowHeight()

class Image(Base):
    '''
    画像描写クラス
    '''


    def __init__(self, bounds, imagePath, color=[1, 1, 1, 1]):
        '''
        テクスチャIDを作成します
        *第一引数:位置(左下基準)と大きさ;(x,y,width,height)
        *第二引数;画像のパス（日本語パスを回避してください）
        第三引数:色（デフォルトは白不透明）cf.画像では透明度を主に使用します
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}

        if not hasattr(bge.logic, "texture_cache"):
            bge.logic.texture_cache = {}

        self.bounds = bounds
        self.imagePath = imagePath
        self.color = color

        bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)

        # テクスチャID生成
        self.buf_id = bgl.Buffer(bgl.GL_INT, 1)
        bgl.glGenTextures(1, self.buf_id)
        self.tex_id = self.buf_id.to_list()[0]

        # 画像読み込み
        if self.imagePath in bge.logic.texture_cache:
            return
        else:
            img = bge.texture.ImageFFmpeg(self.imagePath)
            img.scale = False
            bge.logic.texture_cache[self.imagePath] = img

        # 読み込みエラーのチェック
        if img.image is None:
            print("Could not load the image", img)
            self.valid = False
            return

        # バインド（idと画像の結びつけ）の開始
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.tex_id)

        # 画像をテクスチャとして登録
        bgl.glTexImage2D(bgl.GL_TEXTURE_2D, 0, bgl.GL_RGBA, img.size[0],
                         img.size[1], 0, bgl.GL_RGBA,
                         bgl.GL_UNSIGNED_BYTE, img.image)

        # 画像の拡大・縮小方法の指定（これがないとピッタリ以外表示できない）
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEAREST)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST)
        # テクスチャの繰り返しを防止
        # bgl.glTexParameteri(bgl.GL_TEXTURE_2D , bgl.GL_TEXTURE_WRAP_S , bgl.GL_CLAMP)
        # bgl.glTexParameteri(bgl.GL_TEXTURE_2D , bgl.GL_TEXTURE_WRAP_T , bgl.GL_CLAMP)

        self.size = img.size[:]

        img = None


    def draw(self):
        self.animationDraw()
        self.prepare2d()

        bgl.glEnable(bgl.GL_TEXTURE_2D)
        bgl.glEnable(bgl.GL_ALPHA_TEST)

        bgl.glBindTexture(bgl.GL_TEXTURE_2D , self.tex_id)

        # bgl.glNormal3d(0.0, 0.0, 1.0)
        bgl.glColor4f(*self.color)
        bgl.glBegin(bgl.GL_QUADS)
        # 四角形の位置、幅、高さ
        bgl.glTexCoord2f(0, 0)
        bgl.glVertex2f(self.bounds[0], self.bounds[1])

        bgl.glTexCoord2f(1, 0)
        bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1])

        bgl.glTexCoord2f(1, 1)
        bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1] + self.bounds[3])

        bgl.glTexCoord2f(0, 1)
        bgl.glVertex2f(self.bounds[0], self.bounds[1] + self.bounds[3])

        bgl.glEnd()

        bgl.glBindTexture(bgl.GL_TEXTURE_2D , 0)
        bgl.glDisable(bgl.GL_ALPHA_TEST)
        bgl.glDisable(bgl.GL_TEXTURE_2D)
        bgl.glEnable(bgl.GL_CULL_FACE)

# class SpriteImage(Image):
#     '''
#     画像描写クラス
#     '''
#
#
#     def __init__(self, bounds, imagePath, color=[1, 1, 1, 1]):
#         '''
#         テクスチャIDを作成します
#         *第一引数:位置(左下基準)と大きさ;(x,y,width,height)
#         *第二引数;画像のパス（日本語パスを回避してください）
#         第三引数:色（デフォルトは白不透明）cf.画像では透明度を主に使用します
#         '''
#         super(SpriteImage,self).__init__(bounds, imagePath, color)
#
#
#
#     def draw(self, coords):
#         '''
#         第一引数:テクスチャ座標の二重配列
#         例：[[左下テクスチャ座標], [右下テクスチャ座標], [右上テクスチャ座標], [左上テクスチャ座標]
#         '''
#         self.animationDraw()
#         self.prepare2d()
#
#         bgl.glEnable(bgl.GL_TEXTURE_2D)
#         bgl.glEnable(bgl.GL_ALPHA_TEST)
#
#         bgl.glBindTexture(bgl.GL_TEXTURE_2D , self.tex_id)
#
#         # bgl.glNormal3d(0.0, 0.0, 1.0)
#         bgl.glColor4f(*self.color)
#         bgl.glBegin(bgl.GL_QUADS)
#         # 四角形の位置、幅、高さ
#         bgl.glTexCoord2f(*coords[0])
#         bgl.glVertex2f(self.bounds[0], self.bounds[1])
#
#         bgl.glTexCoord2f(*coords[1])
#         bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1])
#
#         bgl.glTexCoord2f(*coords[2])
#         bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1] + self.bounds[3])
#
#         bgl.glTexCoord2f(*coords[3])
#         bgl.glVertex2f(self.bounds[0], self.bounds[1] + self.bounds[3])
#
#         bgl.glEnd()
#
#         bgl.glBindTexture(bgl.GL_TEXTURE_2D , 0)
#         bgl.glDisable(bgl.GL_ALPHA_TEST)
#         bgl.glDisable(bgl.GL_TEXTURE_2D)



class ClippedImage(Base):
    '''
    画像のクリップ描写クラス
    '''

    def __init__(self, bounds, imagePath, color=[1, 1, 1, 1]):
        '''
        テクスチャIDを作成します
        *第一引数:位置(左下基準)と大きさ;(x,y,width,height)
        *第二引数;画像のパス（日本語パスを回避してください）
        第三引数:色（デフォルトは白不透明）cf.画像では透明度を主に使用します
        '''
        self.animationsParams = {}
        self.effectFuncDictionary = {}

        if not hasattr(bge.logic, "texture_cache"):
            bge.logic.texture_cache = {}

        self.bounds = bounds
        self.imagePath = imagePath
        self.color = color

        bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)

        # テクスチャID生成
        self.buf_id = bgl.Buffer(bgl.GL_INT, 1)
        bgl.glGenTextures(1, self.buf_id)
        self.tex_id = self.buf_id.to_list()[0]

        # 画像読み込み
        if self.imagePath in bge.logic.texture_cache:
            return
        else:
            img = bge.texture.ImageFFmpeg(self.imagePath)
            img.scale = False
            bge.logic.texture_cache[self.imagePath] = img

        # 読み込みエラーのチェック
        if img.image is None:
            print("Could not load the image", img)
            self.valid = False
            return

        # バインド（idと画像の結びつけ）の開始
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.tex_id)

        # 画像をテクスチャとして登録
        bgl.glTexImage2D(bgl.GL_TEXTURE_2D, 0, bgl.GL_RGBA, img.size[0],
                         img.size[1], 0, bgl.GL_RGBA,
                         bgl.GL_UNSIGNED_BYTE, img.image)

        # 画像の拡大・縮小方法の指定（これがないとピッタリ以外表示できない）
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEAREST)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST)
        # テクスチャの繰り返しを防止
        # bgl.glTexParameteri(bgl.GL_TEXTURE_2D , bgl.GL_TEXTURE_WRAP_S , bgl.GL_CLAMP)
        # bgl.glTexParameteri(bgl.GL_TEXTURE_2D , bgl.GL_TEXTURE_WRAP_T , bgl.GL_CLAMP)

        self.size = img.size[:]

        img = None


    def draw(self, coords):
        '''
        第一引数:表示するテクスチャ座標の二重配列
        例：[[左下テクスチャ座標], [右下テクスチャ座標], [右上テクスチャ座標], [左上テクスチャ座標]
        '''
###
### 深度によるクリッピング
###
        bgl.glEnable(bgl.GL_DEPTH_TEST)
        bgl.glClearDepth(0)
        bgl.glClear(bgl.GL_DEPTH_BUFFER_BIT)

        # 常に成功にして，次のオプションの第三引数を常に実行
        bgl.glDepthFunc(bgl.GL_ALWAYS)
        bgl.glDepthMask(bgl.GL_TRUE)
        bgl.glColorMask(bgl.GL_FALSE, bgl.GL_FALSE, bgl.GL_FALSE, bgl.GL_FALSE)

        self.animationDraw()
        self.prepare2d()

        # クリップ用領域
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glVertex3f(self.bounds[0] + coords[0][0] * self.bounds[2] / 100, self.bounds[1] + coords[0][1] * self.bounds[3] / 100, 0)
        bgl.glVertex3f(self.bounds[0] + coords[1][0] * self.bounds[2] / 100, self.bounds[1] + coords[1][1] * self.bounds[3] / 100, 0)
        bgl.glVertex3f(self.bounds[0] + coords[2][0] * self.bounds[2] / 100, self.bounds[1] + coords[2][1] * self.bounds[3] / 100, 0)
        bgl.glVertex3f(self.bounds[0] + coords[3][0] * self.bounds[2] / 100, self.bounds[1] + coords[3][1] * self.bounds[3] / 100, 0)
        bgl.glEnd()


        bgl.glDepthFunc(bgl.GL_LESS)
        bgl.glColorMask(bgl.GL_TRUE, bgl.GL_TRUE, bgl.GL_TRUE, bgl.GL_TRUE)
        bgl.glDepthMask(bgl.GL_FALSE)

        bgl.glEnable(bgl.GL_TEXTURE_2D)
        bgl.glEnable(bgl.GL_ALPHA_TEST)

        bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.tex_id)

        bgl.glColor4f(*self.color)
        bgl.glBegin(bgl.GL_QUADS)
        # 四角形の位置、幅、高さ
        bgl.glTexCoord3f(0,0,1)
        bgl.glVertex3f(self.bounds[0], self.bounds[1], 1)

        bgl.glTexCoord3f(1,0,1)
        bgl.glVertex3f(self.bounds[0] + self.bounds[2], self.bounds[1], 1)

        bgl.glTexCoord3f(1,1,1)
        bgl.glVertex3f(self.bounds[0] + self.bounds[2], self.bounds[1] + self.bounds[3], 1)

        bgl.glTexCoord3f(0,1,1)
        bgl.glVertex3f(self.bounds[0], self.bounds[1] + self.bounds[3], 1)

        bgl.glEnd()
        bgl.glDepthFunc(bgl.GL_ALWAYS)

        bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)
        bgl.glDisable(bgl.GL_ALPHA_TEST)
        bgl.glDisable(bgl.GL_TEXTURE_2D)
        bgl.glDisable(bgl.GL_DEPTH_TEST)
        bgl.glEnable(bgl.GL_CULL_FACE)

###
### ステンシルによるクリッピング
###
#         bgl.glClearStencil(0)
#         bgl.glClear(bgl.GL_STENCIL_BUFFER_BIT)
#
#         bgl.glEnable(bgl.GL_STENCIL_TEST)
#
#         # 常に成功にして，次のオプションの第三引数を常に実行
#         bgl.glStencilFunc(bgl.GL_ALWAYS, 1, 0xFF)
#         bgl.glStencilOp(bgl.GL_KEEP, bgl.GL_KEEP, bgl.GL_REPLACE)
#
#         bgl.glColorMask(bgl.GL_FALSE, bgl.GL_FALSE, bgl.GL_FALSE, bgl.GL_FALSE)
#         bgl.glDepthMask(bgl.GL_FALSE)
#
#         self.animationDraw()
#         self.prepare2d()
#
#         # クリップ用領域
#         bgl.glBegin(bgl.GL_QUADS)
#         bgl.glVertex2f(self.bounds[0] + coords[0][0] * self.bounds[2] / 100, self.bounds[1] + coords[0][1] * self.bounds[3] / 100)
#         bgl.glVertex2f(self.bounds[0] + coords[1][0] * self.bounds[2] / 100, self.bounds[1] + coords[1][1] * self.bounds[3] / 100)
#         bgl.glVertex2f(self.bounds[0] + coords[2][0] * self.bounds[2] / 100, self.bounds[1] + coords[2][1] * self.bounds[3] / 100)
#         bgl.glVertex2f(self.bounds[0] + coords[3][0] * self.bounds[2] / 100, self.bounds[1] + coords[3][1] * self.bounds[3] / 100)
#         bgl.glEnd()
#
#         bgl.glColorMask(bgl.GL_TRUE, bgl.GL_TRUE, bgl.GL_TRUE, bgl.GL_TRUE)
#         bgl.glDepthMask(bgl.GL_TRUE)
#
#         bgl.glStencilOp(bgl.GL_KEEP, bgl.GL_KEEP, bgl.GL_KEEP)
#         bgl.glStencilFunc(bgl.GL_EQUAL, 1, 0xFF)
#
#         bgl.glEnable(bgl.GL_TEXTURE_2D)
#         bgl.glEnable(bgl.GL_ALPHA_TEST)
#
#         bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.tex_id)
#
#         # bgl.glNormal3d(0.0, 0.0, 1.0)
#         bgl.glColor4f(*self.color)
#         bgl.glBegin(bgl.GL_QUADS)
#         # 四角形の位置、幅、高さ
#         bgl.glTexCoord2f(0,0)
#         bgl.glVertex2f(self.bounds[0], self.bounds[1])
#
#         bgl.glTexCoord2f(1,0)
#         bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1])
#
#         bgl.glTexCoord2f(1,1)
#         bgl.glVertex2f(self.bounds[0] + self.bounds[2], self.bounds[1] + self.bounds[3])
#
#         bgl.glTexCoord2f(0,1)
#         bgl.glVertex2f(self.bounds[0], self.bounds[1] + self.bounds[3])
#
#         bgl.glEnd()
#
#         bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)
#         bgl.glDisable(bgl.GL_ALPHA_TEST)
#         bgl.glDisable(bgl.GL_TEXTURE_2D)
#         bgl.glDisable(bgl.GL_STENCIL_TEST)
#         bgl.glEnable(bgl.GL_CULL_FACE)