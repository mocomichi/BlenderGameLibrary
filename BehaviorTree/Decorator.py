'''
Created on 2016/09/28

@author: 大地
'''

class Blackboard:
    '''
    ブラックボードデコレータ
    '''


    def __init__(self, data, KeyName, mode):
        '''
        第三引数のmodeは
        Is SetモードとIs Not Setモードの切り替え
        Is SetモードはそのキーがあれえばTrueを返し、
        逆にIs Not Setモードはそのキーがない場合にTrueを返す
        Is SetモードならTrue
        Is Not SetモードならFalse
        '''
        self.data = data
        self.KeyName = KeyName
        self.mode = mode

    def run(self):
        if self.KeyName in self.data:
            return not(self.mode ^ True)
        return not(self.mode ^ False)

class CompareBlackboardEntries:
    '''
    Compare Blackboard Entriesデコレータ
    '''

    def __init__(self, data, KeyName1, KeyName2, mode):
        '''
        第四引数のmodeは
        Is Equalモード、Is Not Equalモード、LessThanモード、GreaterThanモード
        の切り替え
        それぞれ 0, 1, 2, 3に対応
        順番は
        KeyName1 is Less(Greater) Than KeyName2
        '''
        self.data = data
        self.KeyName1 = KeyName1
        self.KeyName2 = KeyName2
        self.mode = mode

    def run(self):
        if self.mode == 0:
            return self._IsEqual()
        if self.moce == 1:
            return self._IsNotEqual()
        if self.mode == 2:
            return self._LessThan()
        if self.mode == 3:
            return self._GreaterThan()


    def _IsEqual(self):
        if self.data[self.KeyName1] == self.data[self.KeyName2]:
            return True
        return False

    def _IsNotEqual(self):
        if self.data[self.KeyName1] != self.data[self.KeyName2]:
            return True
        return False

    def _LessThan(self):
        if self.data[self.KeyName1] <= self.data[self.KeyName2]:
            return True
        return False

    def _GreaterThan(self):
        if self.data(self.KeyName1) >= self.data[self.KeyName2]:
            return True
        return False


# class isTouchingWall:
#     '''
#     当たり判定ノード
#     '''
#
#     def __init__(self, data, MyDataKey, WallObjList):
#         self.data = data
#         self.MyDataKey = MyDataKey
#         self.WallObjList = WallObjList
#
#     def run(self):
#         self.data[self.MyDataKey].
