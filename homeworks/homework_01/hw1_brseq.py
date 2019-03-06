#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(braces):
    '''
    Метод проверяющий является ли поданная скобочная
    последовательность правильной (скобки открываются и закрываются)
    не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    brs = {'[': ']', '{': '}', '(': ')'}
    new_br = []
    for j in braces:
        new_br.append(j)
    left = []
    right = []
    flag = True
    for i in range(len(new_br)):
        if new_br[0] not in brs.keys():
            flag = False
            break
        if new_br[i] in brs.keys():
            left.append(new_br[i])
        else:
            right.append(new_br[i])
        if len(right) != 0:
            if len(left) == 0:
                flag = False
            else:
                if brs.get(left[-1]) == right[0]:
                    left.pop()
                    right.pop()
                if len(right) != 0:
                    break

    if flag is True and len(left) == 0 and len(right) == 0:
        return True
    else:
        return False
    # raise NotImplementedError
