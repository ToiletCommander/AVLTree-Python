# -*- coding: utf-8 -*-
from Node import Node
import copy

class AVLTree:
    # This AVL Tree use lists to store datas
    # 0 - own value
    # 1 - left sub-tree
    # 2 - right sub-tree
    # 3 - index
    rootNode = None
    
    def __init__(self):
        self.rootNode = Node()
    
    def __put(self, number):
        searchedNode = self.search(number)
        if searchedNode.number is None:
            if searchedNode.parentNode is None:
                rootNode = Node(number,None,None,0,None)
            else:
                searchedNode.number = number
                if number < searchedNode.parentNode.number:
                    searchedNode.parentNode.leftSubNode = searchedNode
                    searchedNode.parentNode.recursiveAddBalanceToLeft()
                else:
                    searchedNode.parentNode.rightSubNode = searchedNode
                    searchedNode.parentNode.recursiveAddBalanceToRight()
            swappingNodes = []
            tempNode = searchedNode
            while not(tempNode is None):
                if tempNode.offset < -1 or tempNode.offset > 1
                    swappingNodes.append(tempNode)
                tempNode = searchedNode.parentNode
            
    
    def __recalculateBalance(node):
        leftNum = 0
        if not(node.leftSubNode is None):
            leftNum = node.leftSubNode.getMostSubNodeLevelNum() + 1
        
        rightNum = 0
        if not(node.rightSubNode is None):
            rightNum = node.rightSubNode.getMostSubNodeLevelNum() + 1
        
        node.offset = rightNum - leftNum
        
        if not(node.leftSubNode is None):
            __recalculateBalance(node.leftSubNode)
        
        if not(node.rightSubNode is None):
            __recalculateBalance(node.rightSubNode)
        
    def __rotateRight(node):
        if node.leftSubNode is None:
            return

        y = node.leftSubNode
        parent = node.parentNode
        node.leftSubNode = y.rightSubNode
        y.rightSubNode = node
        y.parentNode = parent
        node.parentNode = y
        if not parent is None:
            if parent.leftSubNode == node
                parent.leftSubNode = y
            else:
                parent.rightSubNode = y
        return
    
    def __rotateLeft(node):
        if node.rightSubNode is None:
            return
        y = node.rightSubNode
        parent = node.parentNode
        node.rightSubNode = y.leftSubNode
        y.leftSubNode = node
        y.parentNode = parent
        node.parentNode = y
        if not parent is None:
            if parent.leftSubNode == node:
                parent.leftSubNode = y
            else:
                parent.rightSubNode = y
        return



    def search(self, number):
        tempNode = self.rootNode
        while not(tempNode is None):
            parentNode = tempNode
            if number < tempNode.number:
                tempNode = tempNode.leftSubNode
                tempNode.parentNode = parentNode
            elif number > tempNode.number:
                tempNode = tempNode.rightSubNode
                tempNode.parentNode = parentNode
            else: #number == tempNode.number:
                break
        if(tempNode is None):
            return Node(None,None,None,0,tempNode.parentNode)
        else:
            return tempNode
    
