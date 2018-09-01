#-*- coding: UTF-8 -*-

from random import sample, choice
from time import time


def troca(v, i, j): v[i], v[j] = v[j], v[i]


def seleciona(v, i):
    m = 0
    for j in range(i):
        if v[m]<v[j]: m = j
    return m


def insere(x, v, u):
    while u>=0 and x<v[u]:
        v[u+1] = v[u]
        u -= 1
    v[u+1] = x


def desce(v, i, n):
    while i*2 < n:
        j = i*2
        if j+1 < n and v[j] < v[j+1]: j += 1
        if v[i] >= v[j]: break
        troca(v, i, j)
        i = j


def amontoa(v):
    n = len(v)
    for i in reversed(range(n//2)):
        desce(v, i, n)



def seq(n, *args):
    if len(args) == 0: return sample(list(range(n*10)), n)
    elif len(args) == 2:
        v = [x for x in range(args[0], args[1]+1)]
        return [choice(v) for x in range(n)]
    else: raise Exception('Você digitou os parâmetros errados')


def crescente(v):
    n = len(v)
    for i in range(n-1):
        if v[i]>v[i+1]: return False
    return True


def tempo(f, v):
    t_inicial = time()
    f(v)
    print('Tempo: %.3f' % (time()-t_inicial))