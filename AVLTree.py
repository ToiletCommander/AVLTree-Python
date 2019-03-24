# -*- coding: utf-8 -*-
# This AVL Tree referes information from https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

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
        self.rootNode = Node(None,None,None,0,None)
    
    def __put(self, number):
        searchedNode = self.search(number)
        if searchedNode.number is None:
            if searchedNode.parentNode is None:
                self.rootNode = Node(number,None,None,0,None)
            else:
                searchedNode.number = number
                if number < searchedNode.parentNode.number:
                    searchedNode.parentNode.leftSubNode = searchedNode
                    searchedNode.parentNode.recursiveAddBalanceToLeft()
                else:
                    searchedNode.parentNode.rightSubNode = searchedNode
                    searchedNode.parentNode.recursiveAddBalanceToRight()
            swappingNode = None
            tempNode = searchedNode
            while not(tempNode is None):
                if tempNode.offset < -1 or tempNode.offset > 1:
                    swappingNode = tempNode
                tempNode = searchedNode.parentNode
            if not swappingNode is None:
                self.__autoRotate(swappingNode)


    def __autoRotate(self,node):
        if node is None:
            return False
        if (node.offset >= -1 and node.offset <= 1):
            return True
        
        parent = node.parentNode
        if parent is None:
            return False

        if (node.offset < -1 and parent.offset > 1):
            self.__rotateRight(parent)
        elif (node.offset > 1 and parent.offset < -1):
            self.__rotateLeft(node)
            self.__rotateRight(parent)
        elif (node.offset > 1 and parent.offset > 1):
            self.__rotateLeft(parent)
        elif (node.offset < -1 and parent.offset > 1):
            self.__rotateRight(node)
            self.__rotateLeft(parent)
        return True
    
    def __recalculateBalance(self,node):
        leftNum = 0
        if not(node.leftSubNode is None):
            leftNum = node.leftSubNode.getMostSubNodeLevelNum() + 1
        
        rightNum = 0
        if not(node.rightSubNode is None):
            rightNum = node.rightSubNode.getMostSubNodeLevelNum() + 1
        
        node.offset = rightNum - leftNum
        
        if not(node.leftSubNode is None):
            self.__recalculateBalance(node.leftSubNode)
        
        if not(node.rightSubNode is None):
            self.__recalculateBalance(node.rightSubNode)
        
    def __rotateRight(self,node):
        if node.leftSubNode is None:
            return

        y = node.leftSubNode
        parent = node.parentNode
        node.leftSubNode = y.rightSubNode
        y.rightSubNode = node
        y.parentNode = parent
        node.parentNode = y
        if not parent is None:
            if parent.leftSubNode == node:
                parent.leftSubNode = y
            else:
                parent.rightSubNode = y
        return
    
    def __rotateLeft(self,node):
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
    
