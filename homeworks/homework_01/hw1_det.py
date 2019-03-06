#!/usr/bin/env python
# coding: utf-8
import copy


def minor(list_of_list, i, j):
    m = copy.deepcopy(list_of_list)
    del m[i]
    for i in range(len(list_of_list) - 1):
        del m[i][j]
    return m


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    line_i = len(list_of_lists[0])
    line_j = len(list_of_lists)
    if line_i != line_j:
        return False
    if line_i == 1:
        return list_of_lists[0][0]
    det = 0
    # sigma = 1
    for j in range(line_i):
        sigma = (-1) ** (2 + j)
        det += list_of_lists[0][j] * sigma * calculate_determinant(
            minor(list_of_lists, 0, j))
    return det
    # raise NotImplementedError
