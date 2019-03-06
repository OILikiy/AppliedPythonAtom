#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    # operator = ["plus", "minus", "mlt", "divide"]
    if type(x) in {int, float, None} and type(y) in {int, float, None} and \
            type(operator) is str:
        if operator == "plus":
            return x + y
        if operator == "minus":
            return x - y
        if operator == "mult":
            return x * y
        if operator == "divide" and y != 0:
            return x / y
        else:
            return None
    else:
        return None
    # raise NotImplementedError
