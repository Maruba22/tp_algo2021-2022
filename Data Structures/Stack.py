# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:26:31 2023

@author: Maruba
"""
import unittest

class ArrayStack:
  """LIFO pile basée sur Python"""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # 

  def top(self):
    """Return (but do not remove) the element at the top of the stack.
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty("Stack is empty")
    return self._data[-1]                 

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty("Stack is empty")
    return self._data.pop()               # remove last item from list






if __name__ == '__main__':
    unittest.main()
    
    p1 = ArrayStack()
    p1.push(19)
    p1.push(20)
    print(p1.__len__())
    p1.pop()
    print(p1.__len__())
    p1.top()
    
    for x in range(12,54):
        p1._data.append(x)
    
    for y in p1._data:
        print(y)
        
  
        
  
    
    
    
    
    

