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
# Filename: ADT-Map-Sample.py
# This Python code creates code for the following purposes:
# - Creates an Abstract Data Type for Map ADT including operations;
# - Operations include __setitem__, __getitem__, __delitem__, __len__ and __iter__. 
############################################################################### 
# Object Pattern:
# - This sample code uses Template Method Design Pattern that uses inheritance from
# - from an Abstract Base Class called MapBase. MapBase is derived from 
# - collections.MutableMapping base class. 
# - Abstract behaviors are undefined in the base class MapBase and are defined 
# - in the derived class. 
############################################################################### 

import collections
from collections import *

class MapBase(collections.MutableMapping):
    """Our own abstract base class that includes a nonpublic Item class."""

    #------------------------------- nested Item class -------------------------------
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""

        def __init__ (self, k, v):
            self._key = k
            self._value = v

        def __eq__ (self, other):
            return self._key == other._key # compare items based on their keys

        def __ne__ (self, other):
            return not (self == other) # opposite of eq

        def __lt__ (self, other):
            return self._key < other._key # compare items based on their keys


class UnsortedTableMap(MapBase):
    """ Map implementation using an unordered list."""
    
    def __init__(self):
        """Create an empty map."""
        self._table = []
        
    def __getitem__(self, k):
        """Return value associated with key k"""
        for item in self._table:
            if (k == item._key):
                return item._value
        
        raise KeyError("Key Error: " + repr(k))
        
    
    def __setitem__(self, k, v):
        """ Assign value v to key k"""
        for item in self._table:
            if (k == item._key):
                item._value = v
                return
            
        self._table.append(self._Item(k, v))
        
    def __delitem__(self, k):
        """Remove item associated with key k"""
        
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
            
        raise KeyError("Key Error: " + repr(k))
        
        
    def __len__(self):
        """ Return number of items in the map."""
        return len(self.__table)
    
    def __iter__(self):
        """Generate iteration of the map's keys"""
        for item in self._table:
            yield item._key
            

if __name__ == "__main__":
    m = UnsortedTableMap()
    m[1] = "a"
    m[2] = "b"
    m[3] = "c"
    m[4] = "d"
    
    print("\nBefore deletion:")
    for i in m:
        print("m[" + str(i) + "]" + " =  " + m[i])
        
    del m[1]
    
    print("\nAfter deletion:")
    for i in m:
        print("m[" + str(i) + "]" + " =  " + m[i])
        
        
                