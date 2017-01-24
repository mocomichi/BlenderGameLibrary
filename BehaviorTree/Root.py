'''
Created on 2016/09/21

@author: 大地
'''
from  BehaviorTree.Status import Status

class Root:
    '''
    ルートノード
    Falseが返ってきたら終了
    '''


    def __init__(self):
        self.array = []

    def add(self, *node):
        self.array.extend(node)

    def update(self):
        for x in self.array:
            x.run()
            if x.status == Status.ABORTED:
                break