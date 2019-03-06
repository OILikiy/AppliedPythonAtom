#!/usr/bin/env python
# coding: utf-8
import re


def find_numbers(eq):
    # return re.search(r'(?<=\/)[+-]?\d+(?:\.\d+)?',eq)
    return re.split(r'[+-/*^()\s]+', eq)


def find_operators(eq):
    # return re.findall(r'[+-/*^]+|[()]', eq)
    lst = re.findall(r'.', eq)
    numbers = find_numbers(eq)
    stack = []
    num = ""
    for i in lst:
        if i not in {"(", ")", "+", "-", "*", "/", "^"}:
            num += i
            if num in numbers:
                stack.append(num)
            else:
                continue
        else:
            stack.append(i)
            num = ""
    return stack


def advanced_calculator(eq):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    line = find_operators(eq)
    num = []
    oper = []
    braces = []
    for i in range(len(line)):
        if line[i] not in {"(", ")", "+", "-", "*", "/", "^"}:
            num.append(line[i])
            print(num)
        else:
            oper.append(line[i])
            print(oper)
            if line[i] == "(":
                while line[i] == ")":
                    braces.append(line[i])
                    print("br: ", braces)
            if line[i] == "*":
                num.append(line[i + 1])
                print(float(num.pop()) * float(num.pop()))
    # for item in line:
    #     if item not in {"(", ")", "+", "-", "*", "/", "^"}:
    #         num.append(item)
    #         print(num)
    #     else:
    #         oper.append(item)
    #         print(oper)
    #         if item == "*":
    #             print(num)
    #             print(float(num.pop()))

    # return line
    raise NotImplementedError
