#!/usr/bin/env python3
# Soroban worksheet generator
from random import triangular, seed, sample, randint
import math


def get_digit():
    return int(round(triangular(3.2, 4.4, 5)))


def get_operator():
    op = sample([1, 1, 1, 1, 1, 1, 1, -1, -1, -1], 1)[0]
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
    ret = ''
    for operand in ex['numbers']:
        ret += '{:=8d}'.format(operand) + '\n'
    ret += '-'*8 + '\n'
    # ret += '{:=8d}'.format(ex['result']) + '\n'
    return(ret)


def get_result(ex):
    ret = ''
    ret += '{:=8d}'.format(ex['result'])
    return(ret)


# CLI proof of concept
def poc():
    for _ in range(3):
        g = gen_excercise(3)
        ex = next(g)
        format_excercise(ex)
