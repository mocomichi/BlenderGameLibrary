'''
Created on 2016/09/21

@author: 大地
'''
from BehaviorTree.Root import Root
from BehaviorTree.Status import Status
import sys
import random

class Selector(Root):
    '''
    セレクターノード
    '''

    def __init__(self):
        super().__init__()
        self._decorators = []
        self._RunningIndex = 0
        self.status = Status.FAILURE

    def check(self):
        if len(self.array) == 0:
            sys.stderr.write('There is no node under Selector')

    def _GoNextNode(self):
        if len(self.array) == self._RunningIndex + 1:
            self.status = Status.FAILURE
            self._RunningIndex = 0
            return
        self.status = Status.RUNNING
        self._RunningIndex += 1

    def run(self):
        if self.array[self._RunningIndex].decorators == []:
            for deco in self.array[self._RunningIndex].decorators:
                if not deco.run():
                    self._GoNextNode()
                    return

        self.array[self._RunningIndex].run()

        if self.array[self._RunningIndex].status == Status.FAILURE:
            self._GoNextNode()
            return

        elif self.array[self._RunningIndex].status != Status.RUNNING:
            self.status = self.array[self._RunningIndex].status
            self._RunningIndex = 0
            return

        else:
            self.status = Status.RUNNING
            return


    @property
    def decorators(self):
        return None
    @decorators.setter
    def decorators(self, decos):
        self._decorators.append(decos)
    @decorators.getter
    def decorators(self):
        return self._decorators


class Sequence(Root):
    '''
    シークエンスノード
    '''

    def __init__(self):
        super().__init__()
        self._decorators = []
        self._RunningIndex = 0
        self.status = Status.FAILURE

    def check(self):
        if len(self.array) == 0:
            sys.stderr.write('There is no node under Sequence')

    def _GoNextNode(self):
        if len(self.array) == self._RunningIndex + 1:
            self.status = Status.SUCCESS
            self._RunningIndex = 0
            return
        self.status = Status.RUNNING
        self._RunningIndex += 1

    def run(self):
        if self.array[self._RunningIndex].decorators == []:
            for deco in self.array[self._RunningIndex].decorators:
                if not deco.run():
                    self.status = Status.FAILURE
                    self._RunningIndex = 0
                    return

        self.array[self._RunningIndex].run()

        if self.array[self._RunningIndex].status == Status.SUCCESS:
            self._GoNextNode()
            return

        elif self.array[self._RunningIndex].status != Status.RUNNING:
            self.status = self.array[self._RunningIndex].status
            self._RunningIndex = 0
            return

        else:
            self.status = Status.RUNNING
            return

    @property
    def decorators(self):
        return None
    @decorators.setter
    def decorators(self, decos):
        self._decorators.append(decos)
    @decorators.getter
    def decorators(self):
        return self._decorators


class Random(Root):
    '''
    ランダムノード
    '''
    def __init__(self):
        super().__init__()
        self._decorators = []
        self.status = Status.FAILURE
        self._RunningIndex = 0
        random.seed()

    def run(self):
        if self.status != Status.RUNNING:
            self._RunningIndex = random.randrange(0,len(self.array))
        if self.array[self._RunningIndex].decorators == []:
            for deco in self.array[self._RunningIndex].decorators:
                if not deco.run():
                    self.status = Status.FAILURE
                    return
        self.array[self._RunningIndex].run()
        self.status = self.array[self._RunningIndex].status


    @property
    def decorators(self):
        return None
    @decorators.setter
    def decorators(self, decos):
        self._decorators.append(decos)
    @decorators.getter
    def decorators(self):
        return self._decorators


# class SimpleParallel:
#     '''
#     シンプルパラレルノード
#     メインツリーとセカンダリツリーすべてを実行します
#     '''
#
#     def __init__(self):
#         super().__init__()
#         self._decorators = None
#
#     def run(self):
#         length = len(self.array)
#         assert length < 3
#         count = 0
#         for node in self.array:
#             if node.run():
#                 count++
#         if count == length:
#             return True
#         return False