# -*- coding: utf-8 -*-
class Node:
    number = None
    leftSubNode = None
    rightSubNode = None
    offset = 0
    parentNode = None

    def __init__(self, num, leftsub, rightsub, balanceoffset, parent):
        self.number = num
        self.leftSubNode = leftsub
        self.rightSubNode = rightsub
        self.offset = balanceoffset
        self.parentNode = parent


    def getLeftMostChildNode(self):
        tempNode = self
        while not(tempNode.leftSubNode is None):
            tempNode = tempNode.leftSubNode
        return tempNode

    def getRightMostChildNode(self):
        tempNode = self
        while not(tempNode.rightSubNode is None):
            tempNode = tempNode.rightSubNode
        return tempNode

    def recursiveAddBalanceToLeft(self):
        tempNode = self
        while not(tempNode is None):
            tempNode.offset -= 1
            tempNode = tempNode.parentNode
        return
    
    def recursiveAddBalanceToRight(self):
        tempNode = self
        while not(tempNode is None):
            tempNode.offset += 1
            tempNode = tempNode.parentNode
        return

    def getMostSubNodeLevelNum(self):
        leftSubNum = 0
        if self.leftSubNode is None:
            leftSubNum = 0
        else:
            leftSubNum = self.leftSubNode.getMostSubNodeLevelNum() + 1
        
        rightSubNum = 0
        if self.rightSubNode is None:
            rightSubNum = 0
        else:
            rightSubNum = self.leftSubNode.getMostSubNodeLevelNum() + 1
        return max(leftSubNum,rightSubNum)
