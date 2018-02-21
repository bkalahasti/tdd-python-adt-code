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
# Filename: ADT-LinkedQueue-Sample.py
# This Python code creates code for the following purposes:
# - Creates an Abstract Data Type for Queue ADT including operations. 
# - Operations include enqueue, dequeue, front and is_empty. 
# - The Queue ADT is implemented using a Singly Linked List.
############################################################################### 
# Object Pattern:
# - This sample code uses Composition Pattern that defines a nested, non-public 
# - class inside the main class. 
# - The object of the main class will comprise of instances of the nested class. 
############################################################################### 

class Empty(Exception):
    pass 

class LinkedQueue:
    
    class _Node:
        """ Lightweight, non-public class for storing a singly, linked node. """
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """ Create an empty Linked Queue. """
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """ Return the number of elements in the Linked Queue. """
        return self._size       
    
    def is_empty(self):
        """ Return True if the Linked Queue is empty. """
        return (self._size == 0)
    
    def enqueue(self, e):
        """ Add element e to the tail of the Linked Queue and return nothing. """
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new 
        self._tail = new 
        self._size += 1
        
    def dequeue(self):
        """ Remove and return the front element of the Linked Queue. """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element 
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._head = self._tail = None
        return answer 

    def front(self):
        """ Return but not remove the front element of the Linked Queue. """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element 
    
if (__name__ == "__main__"):
    Q = LinkedQueue()
#    print("Front element: ", Q.front())
    Q.enqueue(1)
    Q.enqueue(2)
    print("Front element: ", Q.front())
    Q.enqueue(3)
    Q.enqueue(4) 
    print("Front element: ", Q.front())
    
    
    

