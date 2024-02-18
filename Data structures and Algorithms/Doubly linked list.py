# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:39:39 2023

@author: HP
"""
# Python code to demonstrate how parent constructors
# are called.
 
# parent class
class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None
        
        
class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insertStart(self, data):
        current = self.head
        newNode = Node(data)
        if self.size == 0:
            self.head = newNode
        else:
            current.previous_node = newNode
            newNode.next_node = self.head
            self.head = newNode
        self.size += 1
        
    def insertEnd(self, data):
        newNode = Node(data)
        current = self.head
        if self.size == 0:
            self.head = newNode       
        while current.next_node is not None:
            current = current.next_node
        newNode.previous_node = current
        current.next_node = newNode
        self.size += 1 
        
    def insertPos(self, data, pos):
        if pos > self.size:
            raise Exception('Index given is bigger than list size')
        elif pos == 0:
            self.insertStart(data)
        elif pos == self.size:
            self.insertEnd(data)
        else:
            count = 0
            current = self.head
            newNode = Node(data)
            while count < pos-1:
                current = current.next_node
                count += 1
            newNode.previous_node = current
            newNode.next_node = current.next_node
            current.next_node = newNode
        self.size += 1 
        
    def remove(self, data):
        if self.size == 0:
           raise Exception('Invalid operation, list is null') 
        current = self.head
        previous = None
        while current.data != data:
            previous = current
            current = current.next_node
        if previous is None:
            self.head.previous_node = current
            self.head = current.next_node
        else:
            previous.next_node = current.next_node
            current.next_node.previous_node = previous
        self.size -= 1
    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node
    def getSize(self):
        return self.size
#

node = Linkedlist()
node.insertStart(9)
node.insertStart(7)
node.insertStart(5)
node.insertEnd(8)
node.insertPos(10, 2)

node.remove(5)
node.printList()
#node.previous_node