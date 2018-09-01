#-*- coding: UTF-8 -*-

from random import sample, choice
from time import time


dict_algoritmos = {
    'bsort': 'Bubble',
    'ssort': 'Selection',
    'isort': 'Insertion',
    'hsort': 'Heap',
    'msort': 'Merge'
}

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


def intercala(v, p, m, u):
    n = (u-p)+1
    i, j, k = p, m+1, 0
    w = [0]*n

    while i <= m and j <= u:
        if v[i] < v[j]: w[k], i, k = v[i], i+1, k+1
        else: w[k], j, k = v[j], j+1, k+1

    while i <= m: w[k], i, k = v[i], i+1, k+1
    while j <= u: w[k], j, k = v[j], j+1, k+1

    for k in range(n): v[k+p] = w[k]


def ms(v, p, u):
    if p == u: return
    m = (p+u)//2
    ms(v, p, m)
    ms(v, m+1, u)
    intercala(v, p, m ,u)



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


def decrescente(v):
    n = len(v)
    for i in reversed(range(1, n)):
        if v[i] > v[i-1]: return False
    return True


def tempo(f, v):
    t_inicial = time()
    f(v)
    print('Tempo do {} Sort: {:.3f}'.format(dict_algoritmos[f.__name__], time()-t_inicial))