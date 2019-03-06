#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    number_str = str(number)
    num_lst = []
    number_abs = ''
    for sym in number_str[::-1]:
        num_lst.append(sym)
    print(num_lst)
    if num_lst[-1] is "-":
        num_lst.pop()
        print(num_lst)
        for i in num_lst:
            number_abs += i
        return -1 * int(number_abs)
    else:
        for i in num_lst:
            number_abs += i
        return int(number_abs)
    # raise NotImplementedError
