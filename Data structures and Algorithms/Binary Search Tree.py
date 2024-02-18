# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 06:30:01 2023

@author: HP
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = Node(data)
            
    def printTree(self):
        if self.data:
            if self.left:
                self.left.printTree()
            print(self.data)
            if self.right:
                self.right.printTree()
                
    def traverse(self, root):
        res = [ ]
        if root:
           res = self.traverse(root.left) 
           res.append(root.data)
           res.extend(self.traverse(root.right))
        return res
    
    def findValue(self, value):
        if self.data:
            if value < self.data:
                if self.left:
                    return self.right.findValue(value)
                else:
                    
                    print('not found')
            elif value > self.data:
                if self.right:
                    return self.right.datafindValue(value)
                else:
                    
                    print('not found')
            else:
                print('found')
                
    def delNode(self, root, value):
        if not root:
            return
        if value < root.data:
            root.left = self.delNode(root.left, value)
        elif value > root.data:
            root.right = self.delNode(root.right, value)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            current = root.data
            while current.left:
                current = current.left
            root.data = current.data
            root.right = self.delNode(root.right, root.data)
        return root
            
                
                
                
                
                
                
                
                
                
                
                
                
                
root = Node(4)
root.insert(5)
root.insert(6)
root.insert(3)
root.insert(2)
root.delNode(root, 2)
root.traverse(root)