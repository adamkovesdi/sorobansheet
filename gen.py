# Soroban worksheet generator
from random import triangular, seed, sample, randint
import math


def get_digit():
    return int(round(triangular(3.2, 4.4, 5)))


def get_operator():
    op = sample([1, 1, 1, 1, 1, -1], 1)[0]
    return op


def get_number(digits):
    lowbound = int(math.pow(10, digits-1))
    highbound = int(math.pow(10, digits)-1)
    absolute = randint(lowbound, highbound)
    return absolute


def gen_excercise(operands):
    while True:
        ex = dict()
        numbers = []
        for i in range(operands):
            n = get_number(get_digit())
            if sum(numbers) > n:
                n = n * get_operator()
            numbers.append(n)
        ex['numbers'] = numbers
        ex['result'] = sum(numbers)
        yield(ex)


def format_excercise(ex):
    for operand in ex['numbers']:
        print('{:=8d}'.format(operand))
    print('-'*8)
    print('{:=8d}'.format(ex['result']))
    print


# CLI proof of concept

for _ in range(3):
    g = gen_excercise(3)
    ex = g.next()
    format_excercise(ex)
