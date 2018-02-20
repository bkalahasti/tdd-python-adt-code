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
# Filename: ADT-Stack-Sample.py
# This Python code creates code for the following purposes:
# - Creates an Abstract Data Type for Stack ADT including operations;
# - Operations include push, pop, top and is_empty. 
############################################################################### 
# Object Pattern:
# - This sample code uses Adapter Pattern that uses an instance of an 
# - existing class as the hidden instance variable and implements the 
# - methods of the new class using methods of the hidden instance variable. 
############################################################################### 

class Empty(Exception):
    """ Exception subclass of the Exception class to define empty Stack state."""
    pass

class ArrayStack:    
        
    def __init__(self):
        """ Create an empty stack. """
        self._data = []
      
    def __len__(self):
        """ Returns the length of the stack. """
        return len(self._data)
    
    def is_empty(self):
        """ Return True if the stack is empty. """
        return (len(self._data) == 0)
    
    def push(self, e):
        """ Push an element to the top of the stack. """
        self._data.append(e)
        
    def pop(self):
        """ Pop the element at the top of the stack. """
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self._data.pop()
    
    def top(self):
        """ Return the element at the top of the stack. """
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self._data[-1]

# Main module namespace.
if (__name__ == "__main__"):
    S = ArrayStack()
#    print("Top: ", S.top())
    S.push(1)
    S.push(2)
    print("Top: ", S.top())
    S.push(3)
    S.push(4)
    print("Top: ", S.top())
    