'''
Created on 2016/09/21

@author: 大地
'''
import numpy as np
import time
import bge  # @UnresolvedImport
import mathutils # @UnresolvedImport
from BehaviorTree.Status import Status

cont = bge.logic.getCurrentController()

class MoveTo:
    '''
    移動ノード
    '''

    def __init__(self, ControlObj, GoalPosObj, MyFront, AccetableRadius, AnimationNames = None, SpeedList=None):
        '''
        AnimationNamesは、Stand、Runの順
        '''
        self._decorators = None
        self.ControlObj = ControlObj
        self.MyFront = MyFront
        self.AccetableRadius = AccetableRadius
        self.GoalPosObj = GoalPosObj
        self.AnimationNames = AnimationNames
        if SpeedList is None:
            SpeedList = [0.1]
        self.SpeedList = SpeedList
        self.status = Status.FAILURE


    def run(self):
        divisor = 5 / self.SpeedList[0]
        vec = self.GoalPosObj.localPosition - self.ControlObj.localPosition
        length = np.linalg.norm(vec)
        unit_vec = vec / length
        # 向き
        f = mathutils.Vector(self.MyFront)
        v = mathutils.Vector(unit_vec)
        quat = f.rotation_difference(v)
        th = quat.to_euler()

        mv = mathutils.Vector(unit_vec / divisor)

        self.ControlObj.applyMovement(mv)
        self.ControlObj.localOrientation = [0,0,th[2]]

        if self.AnimationNames is not None:
            act = cont.actuators[self.AnimationNames[1]]
            cont.activate(act)
            act = cont.actuators[self.AnimationNames[0]]
            cont.deactivate(act)


        if self.ControlObj.getDistanceTo(self.GoalPosObj) < self.AccetableRadius:
            self.status = Status.SUCCESS
            act = cont.actuators[self.AnimationNames[1]]
            cont.deactivate(act)
            act = cont.actuators[self.AnimationNames[0]]
            cont.activate(act)
            return
        self.status = Status.RUNNING


    @property
    def decorators(self):
        return None
    @decorators.setter
    def decorators(self, decos):
        self._decorators = decos
    @decorators.getter
    def decorators(self):
        return self._decorators

class MoveForward:
    '''
    前進ノード
    '''
    def __init__(self, ControlObj, MyFront, TaskTime, AnimationNames = None, SpeedList=None):

        self.ControlObj = ControlObj
        self.MyFront = mathutils.Vector(MyFront)
        self.stop = TaskTime
        self.start = 0.0
        if SpeedList is None:
            SpeedList = [1]
        self.SpeedList = SpeedList
        self.status = Status.FAILURE
        self._decorators = None

    def run(self):
        if self.status != Status.RUNNING:
            self.start = time.time()
            self.status = Status.RUNNING

        divisor = 5 / self.SpeedList[0]


        unit_MyFront = self.MyFront.normalized()
        unit_vec = unit_MyFront.rotate(self.ControlObj.localOrientation)

        mv = mathutils.Vector( unit_vec / divisor)

        self.ControlObj.applyMovement(mv)

        if self.AnimationNames is not None:
            act = cont.actuators[self.AnimationNames[1]]
            cont.deactivate(act)
            act = cont.actuators[self.AnimationNames[0]]
            cont.activate(act)

        if time.time() >= self.start + self.TaskTime:
            cont.activate(act)
            act = cont.actuators[self.AnimationNames[0]]
            cont.deactivate(act)
            self.status = Status.SUCCESS
            self.start = 0
            return

    @property
    def decorators(self):
        return None
    @decorators.setter
    def decorators(self, decos):
        self._decorators = decos
    @decorators.getter
    def decorators(self):
        return self._decorators


class MoveBackward:
    '''
    後退ノード
    '''
    def __init__(self, ControlObj, MyFront, TaskTime, LookingPosList, SpeedList=None):

        self.ControlObj = ControlObj
        self.MyFront = MyFront
        self.stop = TaskTime
        self.start = 0.0
        self.LookingPosList = LookingPosList
        if SpeedList is None:
            SpeedList = [1]
        self.SpeedList = SpeedList
        self.status = Status.FAILURE
        self._decorators = None

    def run(self):
        if self.status != Status.RUNNING:
            self.start = time.time()
            self.status = Status.RUNNING

        divisor = 5 / self.SpeedList[0]
        vec = self.LookingPosList - self.ControlObj.localPosition
        length = np.linalg.norm(vec)
        unit_vec = vec / length
        # 向き
        f = mathutils.Vector(self.MyFront)
        v = mathutils.Vector(unit_vec)
        quat = f.rotation_difference(v)

        mv = mathutils.Vector( -unit_vec / divisor)

        self.ControlObj.applyMovement(mv)
        self.ControlObj.localOrientation *= quat

        if time.time() >= self.start + self.Time:
            self.status = Status.SUCCESS
            self.start = 0
            return
    @property
    def decorators(self):
        return None
    @decorators.setter
    def decorators(self, decos):
        self._decorators = decos
    @decorators.getter
    def decorators(self):
        return self._decorators

class Wait:
    '''
    待機ノード
    '''
    def __init__(self, WaitTime, AnimationName = None):
        self._decorators = None
        self.WaitTime = WaitTime
        self.start = 0.0
        self.AnimationName = AnimationName
        self.status = Status.FAILURE

    def run(self):
        if self.AnimationName is not None:
            act = cont.actuators[self.AnimationName]
            cont.activate(act)
        if self.status != Status.RUNNING:
            self.start = time.time()
            self.status = Status.RUNNING

        if time.time() >= self.start + self.WaitTime:
            self.status = Status.SUCCESS
            self.start = 0
            return

        #待機アニメーション
        return

    @property
    def decorators(self):
        return None
    @decorators.setter
    def decorators(self, decos):
        self._decorators = decos
    @decorators.getter
    def decorators(self):
        return self._decorators
class Turn :
    '''
    旋回クラス
    '''
    def __init__(self, ControlObj, Omega, TaskTime):
        '''
        時計回りはOmegaを負に
        反時計回りはOmegaを正に
        '''
        self.ControlObj = ControlObj
        self.omg = Omega
        self.stop = TaskTime
        self.start = 0.0
        self.status = Status.FAILURE

    def run(self):
        if self.status != Status.RUNNING:
            self.start = time.time()
            self.status = Status.RUNNING
        self.ControlObj.applyRotation([0, 0, self.omg], True)
        if time.time() >= self.start + self.WaitTime:
            self.status = Status.SUCCESS
            self.start = 0
            return



class Attack:
    '''
    攻撃クラス
    '''
    def __init__(self, ControlObj, AnimationName):
        self._decorators = None
        self.ControlObj = ControlObj
        self.ControlObj.isAttacking = False
        self.ControlObj.isAttackHit = False
        self.attackStop = self.ControlObj.attackStop
        self.AnimationName = AnimationName
        self.status = Status.FAILURE

    def _ClearState(self):
            self.ControlObj.isAttacking = False
            self.ControlObj.isAttackHit = False

    def run(self):
        act = cont.actuators[self.AnimationName]
        cont.activate(act)

        if self.status != Status.RUNNING:
            self.ControlObj.isAttacking = True
            self.status = Status.RUNNING
        # 攻撃モーション

        if act.frame >= self.sttackStop and self.ControlObj.isAttackHit:
            self.status = Status.SUCCESS
            self._ClearState()

        elif act.frame >= self.attackStop and not self.ControlObj.isAttackHit:
            self.status = Status.FAILURE
            self._ClearState()

    @property
    def decorators(self):
        return None
    @decorators.setter
    def decorators(self, decos):
        self._decorators = decos
    @decorators.getter
    def decorators(self):
        return self._decorators

class MakeNoise:
    '''
    音感知用の音作成ノード
    '''

    def __init__(self, loudness):
        self.loudness = loudness

    def run(self):
        # bge X-rayで範囲をラウドネスから計算
        return True
