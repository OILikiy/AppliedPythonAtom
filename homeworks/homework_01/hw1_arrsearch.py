#!/usr/bin/env python
# coding: utf-8


def find_indices(lst, sm):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
    s = set()
    if len(lst) != 0:
        for i in range(len(lst)):
            if type(lst[i]) is not str:
                num = sm - lst[i]
                if num in s:
                    return i, lst.index(num)
                s.add(lst[i])
            else:
                continue
    else:
        return None
    # raise NotImplementedError
