#!/usr/bin/env python
# coding: utf-8


def check_palindrom(string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    if type(string) is str:
        rev_string = string[::-1]
        if string == rev_string:
            return True
        else:
            return False
    else:
        return "value type error"
    # raise NotImplementedError
