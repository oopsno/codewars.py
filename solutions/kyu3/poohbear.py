# encoding: UTF-8

from collections import defaultdict
from six import StringIO
from enum import Enum
from functools import wraps
import math


class Operand(Enum):
    Imm = 1
    Current = 2
    NegativeCurrent = 4
    Copied = 8
    NegativeCopied = 16


def poohbear_arithmetic(function):
    @wraps(function)
    def __function__(self, tp, *imm):
        if tp == Operand.Current:
            value = int(self.current)
        elif tp == Operand.NegativeCurrent:
            value = -int(self.current)
        elif tp == Operand.Copied:
            value = int(self.copied)
        elif tp == Operand.NegativeCopied:
            value = -int(self.copied)
        elif tp == Operand.Imm:
            value = int(imm[0])
        else:
            raise ValueError('Cannot understand {!r}'.format((tp, *imm)))
        rst = function(self, self.current, value)
        self.current = rst % 256

    return __function__


class Poohbear:
    def __init__(self, code: str):
        # 虚拟机状态
        self.stack = defaultdict(int)
        self.pointer = 0
        self.copied = 0
        self.out = StringIO()
        # 预编译
        self.code = code
        self.bytecode = self.compile(self.code)

    @property
    def current(self) -> int:
        return self.stack[self.pointer]

    @current.setter
    def current(self, value):
        self.stack[self.pointer] = value

    def compile(self, code: str):
        ctx = [[]]
        for c in code:
            if c == '+':  # Add 1 to the current cell
                ctx[-1].append((self.add, Operand.Imm, +1))
            elif c == '-':  # Subtract 1 from the current cell
                ctx[-1].append((self.add, Operand.Imm, -1))
            elif c == '>':  # Move the cell pointer 1 space to the right
                ctx[-1].append((self.seek, +1))
            elif c == '<':  # Move the cell pointer 1 space to the left
                ctx[-1].append((self.seek, -1))
            elif c == 'c':  # "Copy" the current cell
                ctx[-1].append((self.copy,))
            elif c == 'p':  # Paste the "copied" cell into the current cell
                ctx[-1].append((self.paste,))
            elif c == 'W':  # While loop - While the current cell is not equal to 0
                ctx.append([])
            elif c == 'E':  # Closing character for loops
                ctx[-2].append((self.loop, ctx[-1]))
                ctx.pop()
            elif c == 'P':  # Output the current cell's value as ASCII
                ctx[-1].append((self.print, chr))
            elif c == 'N':  # Output the current cell's value as an integer
                ctx[-1].append((self.print, str))
            elif c == 'T':  # Multiply the current cell by 2
                ctx[-1].append((self.add, Operand.Current))
            elif c == 'Q':  # Square the current cell
                ctx[-1].append((self.mul, Operand.Current))
            elif c == 'U':  # Square root the current cell's value
                ctx[-1].append((self.sqrt,))
            elif c == 'L':  # Add 2 to the current cell
                ctx[-1].append((self.add, Operand.Imm, +2))
            elif c == 'I':  # Add 2 to the current cell
                ctx[-1].append((self.add, Operand.Imm, -2))
            elif c == 'V':  # Divide the current cell by 2
                ctx[-1].append((self.half,))
            elif c == 'A':  # Add the copied value to the current cell's value
                ctx[-1].append((self.add, Operand.Copied))
            elif c == 'B':  # Subtract the copied value to the current cell's value
                ctx[-1].append((self.add, Operand.NegativeCopied))
            elif c == 'Y':  # Multiply the copied value to the current cell's value
                ctx[-1].append((self.mul, Operand.Copied))
            elif c == 'D':  # Divide the copied value to the current cell's value
                ctx[-1].append((self.div, Operand.Copied))
        return ctx.pop()

    def run(self, bytecode=None) -> str:
        for opcode, *args in bytecode or self.bytecode:
            opcode(*args)
        return self.out.getvalue()

    @poohbear_arithmetic
    def add(self, lhs, rhs):
        return lhs + rhs

    @poohbear_arithmetic
    def mul(self, lhs, rhs):
        return lhs * rhs

    @poohbear_arithmetic
    def div(self, lhs, rhs):
        return lhs // rhs

    def sqrt(self):
        self.current = int(math.sqrt(self.current))

    def half(self):
        self.current //= 2

    def seek(self, value):
        self.pointer += int(value)

    def loop(self, block):
        while self.current:
            self.run(block)

    def copy(self):
        self.copied = self.current

    def paste(self):
        self.current = self.copied

    def print(self, modifier):
        self.out.write(modifier(self.current))


def poohbear(s):
    return Poohbear(s).run()


import codewars

with codewars.Test(namespace=globals()) as test:
    test.assert_equals(poohbear('LQTcQAP>pQBBTAI-PA-PPL+P<BVPAL+T+P>PL+PBLPBP<DLLLT+P'), 'Hello World!')
    test.assert_equals(poohbear('+LTQII>+WN<P>+E'), ' '.join(map(str, range(1, 256))) + ' ')
    test.assert_equals(poohbear('LQQT+P+P+P+P+P+P'), '!"#$%&')
    test.assert_equals(poohbear('+c BANANA'), '12')
