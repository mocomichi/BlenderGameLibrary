'''
Created on 2016/06/20

@author: 大地
'''
from FunctionUnit import Easing_cdef

class Animations:
    '''
    アニメーションについてのMix-inクラス
    '''

    #
    # アニメーションをスタートさせる関数
    #
    def setFadeIn(self, time):
        '''
        フェードインを開始します
        *第一引数:アニメーション時間
        '''
        seg = 1 / (time * 30)
        self.animationsParams["FadeIn"] = {"seg" : seg, "t" : 0}
        self.effectFuncDictionary["FadeIn"] = self.FadeInFunc

    def setFadeOut(self, time):
        '''
        フェードアウトを開始します
        *第一引数:アニメーション時間
        '''
        seg = 1 / (time * 30)
        self.animationsParams["FadeOut"] = {"seg" : seg, "t" : 0}
        self.effectFuncDictionary["FadeOut"] = self.FadeOutFunc

    #
    # アニメーション実行関数(draw内部)
    #
    def FadeInFunc(self):
        '''
        フェードイン関数
        '''
        if self.animationsParams["FadeIn"]["t"] <= 1:
            self.color[3] = Easing_cdef.Linear(0, 1, self.animationsParams["FadeIn"]["t"])
            self.animationsParams["FadeIn"]["t"] += self.animationsParams["FadeIn"]["seg"]

        else:
            self.effectFuncDictionary["FadeIn"] = {}
            self.animationsParams["FadeIn"] = {}

    def FadeOutFunc(self):
        '''
        フェードアウト関数
        '''
        if self.animationsParams["FadeOut"]["t"] <= 1:
            self.color[3] = Easing_cdef.Linear(1, 0, self.animationsParams["FadeOut"]["t"])
            self.animationsParams["FadeOut"]["t"] += self.animationsParams["FadeOut"]["seg"]

        else:
            self.effectFuncDictionary["FadeOut"] = {}
            self.animationsParams["FadeOut"] = {}


