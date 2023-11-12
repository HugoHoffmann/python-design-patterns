from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import List

class Strategy(ABC):
  @abstractclassmethod
  def sorter(self, list1: List) -> List: 
    pass

class Context(): 
  def __init__(self, strategy: Strategy) -> None:
    self._strategy = strategy

  @property
  def strategy(self) -> Strategy:
    return self._strategy
  
  @strategy.setter
  def strategy(self, strategy: Strategy) -> None:
    self._strategy = strategy

  def sorter(self, list1: List) -> List: 
    return self._strategy.sorter(list1)

class AscOrderStrategy(Strategy): 
  def sorter(self, list1: List) -> List : 
    copyList = list1.copy()
    copyList.sort()
    return copyList

class DescOrderStrategy(Strategy): 
  def sorter(self, list1: List) -> List : 
    copyList = list1.copy()
    copyList.sort()
    return copyList

class DuplicateListStrategy(Strategy): 
  def sorter(self, list1: List) -> List :
    copyList = list1.copy()
    newList = []
    for item in copyList:
      newList.append(item * 2)
    return newList
  
class RemoveRepeatedListStrategy(Strategy): 
  def sorter(self, list1: List) -> List :
    copyList = list1.copy()
    return list(set(copyList))

aux = [5,1,2,3,4,4,5,5,5]
context = Context(DuplicateListStrategy())
result = context.sorter(aux)
print('The list was:')
print(aux)
print('now is: ')
print(result)