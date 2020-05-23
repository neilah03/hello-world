import pytest

def add(x):
  return x + 1
  
def sub(x):
  return x - 1
  
def doub(x):
  return x * 2
    
def test_add():
  assert add(3) == 4
  
def test_sub():
  assert sub(9) == 8
  
def test_doub():
  assert doub(6) == 12
