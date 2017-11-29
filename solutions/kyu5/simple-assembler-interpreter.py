# encoding: UTF-8

import codewars


class Machine:
    def __init__(self):
        self.variables, self.pc, self.code = {}, 0, []

    def compile(self, asm: [str]):
        for line in asm:
            line = line.strip()
            if not line:
                continue
            instruction, *args = line.split()
            self.code.append((getattr(self, instruction), *args))
        return self

    def run(self) -> {str: int}:
        while self.pc < len(self.code):
            instruction, *args = self.code[self.pc]
            instruction(*args)
        return self.variables

    def mov(self, dest: str, source: str):
        self.variables[dest] = self.eval(source)
        self.pc += 1

    def inc(self, operand: str):
        self.variables[operand] += 1
        self.pc += 1

    def dec(self, operand: str):
        self.variables[operand] -= 1
        self.pc += 1

    def jnz(self, cond: str, offset: str):
        if self.eval(cond) != 0:
            self.pc += self.eval(offset)
        else:
            self.pc += 1

    def eval(self, what: str) -> int:
        try:
            return int(what)
        except ValueError:
            return self.variables[what]


def simple_assembler(program: [str]):
    return Machine().compile(program).run()


with codewars.Test(namespace=globals()) as Test:
    code = '''
    mov a 5
    inc a
    dec a
    dec a
    jnz a -1
    inc a'''
    Test.assert_equals(simple_assembler(code.splitlines()), {'a': 1})

    code = '''
    mov c 12
    mov b 0
    mov a 200
    dec a
    inc b
    jnz a -2
    dec c
    mov a b
    jnz c -5
    jnz 0 1
    mov c a'''
    Test.assert_equals(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})
