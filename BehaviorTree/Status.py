'''
Created on 2016/10/02

@author: 大地
'''
import enum


class Status(enum.IntEnum):
    FAILURE = 0
    SUCCESS = 1
    RUNNING = 2
    INVALID = 3
    ABORTED = 4

