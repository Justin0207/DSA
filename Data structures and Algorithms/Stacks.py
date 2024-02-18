# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:53:56 2023

@author: HP
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        
    def push(self, data):
        self.stack.append(data)
        self.size += 1
        
    def pop(self):
        data = self.stack[-1]
        del(self.stack[-1])
        self.size -= 1
        return data
    
    def peek(self, data):
        return self.stack[-1]
    
    def reverse(self):
        return self.stack[::-1]
    
    def printStack(self):
        return self.stack
    
    def StackSize(self):
        return self.size
    
stack = Stack()
for i in range (10):
    stack.push(i)
stack.pop()
stack.printStack()
stack.StackSize()