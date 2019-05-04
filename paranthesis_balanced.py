#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stack import Stack

def is_paranthesis_balanced(s):
    pass

    open_b = ['(','[','{','<']
    matches = [('{','}'), ('[',']'), ('(',')'), ('<','>')]
    stack = Stack(len(s))

    for i in s:
        if i in open_b:
            stack.push(i)
        else:
            if len(stack) == 0 :
                return False
            last_b = stack.pop()
            if (last_b, i) not in matches:
                return False
    return len(stack) == 0