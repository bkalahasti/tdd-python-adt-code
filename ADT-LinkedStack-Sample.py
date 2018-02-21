############################################################################### 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
#     http://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License. 
############################################################################### 
# Filename: ADT-StackLinkedList-Sample.py
# This Python code creates code for the following purposes:
# - Creates an Abstract Data Type for Stack ADT including operations;
# - Operations include push, pop, top and is_empty. 
# - The Stack ADT is implemented using a Singly Linked List.
############################################################################### 
# Object Pattern:
# - This sample code uses Composition Pattern that defines a nested, non-public 
# - class inside the main class. 
# - The object of the main class will comprise of instances of the nested class. 
############################################################################### 

class Empty(Exception):
    pass 

class LinkedStack:
    
    class _Node:
        """ Lightweight, non-public class for storing a singly, linked node. """
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """ Create an empty Linked Stack. """
        self._head = None
        self._size = 0
        
    def __len__(self):
        """ Return the number of elements in the Linked Stack. """
        return self._size       
    
    def is_empty(self):
        """ Return True if the Linked Stack is empty. """
        return (self._size == 0)
    
    def push(self, e):
        """ Add element e to the top of the Linked Stack and return nothing. """
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def pop(self):
        """ Remove and return the top element of the Linked Stack. """
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element 
        self._head = self._head._next
        self._size -= 1
        return answer 

    def top(self):
        """ Return but not remove the top element of the Linked Stack. """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element 
    
if (__name__ == "__main__"):
    S = LinkedStack()
#    print("Top element: ", S.top())
    S.push(1)
    S.push(2)
    print("Top element: ", S.top())
    S.push(3)
    print("Top element: ", S.top())
    
    
    
