# import operator
# from functools import reduce
# lambda
"""
dynamic_reducer([1,2,3], '+') # 6
dynamic_reducer([1,2,3], '-') # -
dynamic_reducer([1,2,3], '*') # -
dynamic_reducer([1,2,3], '/') # -
"""
'''
My failure attempt
import operator, functools
from functools import reduce

nemo = [1, 2, 3]

def drsum():
    functools.reduce(operator.add, nemo, 0)
    return

print(drsum())

def drsub():
    functools.reduce(operator.sub, nemo, 0)

print(drsub())

def drmul():
    functools.reduce(operator.mul, nemo, 0)

print(drmul())

def drdiv():
    functools.reduce(operator.truediv(nemo, 0))

print(drdiv())
'''

# Jordan's solution

import operator, functools
from functools import reduce

def dynamic_reducer(collection, op):
    operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
    }
    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1,2,3], '+'))
print(dynamic_reducer([1,2,3], '-'))
print(dynamic_reducer([1,2,3], '*'))
print(dynamic_reducer([1,2,3], '/'))
