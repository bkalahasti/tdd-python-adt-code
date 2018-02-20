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
# Filename: ADT-Queue-Sample.py
# This Python code creates code for the following purposes:
# - Creates an Abstract Data Type for Queue ADT including operations;
# - Operations include enqueue, dequeue, front and is_empty. 
############################################################################### 
# Object Pattern:
# - This sample code uses Adapter Pattern that uses an instance of an 
# - existing class as the hidden instance variable and implements the 
# - methods of the new class using methods of the hidden instance variable. 
############################################################################### 

class Empty(Exception):
    """ Exception subclass of the Exception class to define empty Queue state."""
    pass

class ArrayQueue:    
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        """ Create an empty queue. """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        """ Returns the length of the queue. """
        return self._size
    
    def is_empty(self):
        """ Return True if the queue is empty. """
        return (self._size == 0)
    
    def enqueue(self, e):
        """ Enqueue an element to the front of the queue. """
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def dequeue(self):
        """ Dequeue the element at the rear of the queue. """
        if (self.is_empty()):
            raise Empty("Queue is empty")
        else:
            answer = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
            self._size -= 1
            return answer

# Main module namespace.
if (__name__ == "__main__"):
    Q = ArrayQueue()
#    print("Front: ", Q.dequeue())
    Q.enqueue(1)
    Q.enqueue(2)
    print("Front: ", Q.dequeue())
    Q.enqueue(3)
    Q.enqueue(4)
    print("Front: ", Q.dequeue())
    