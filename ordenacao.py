#-*- coding: UTF-8 -*-
from funcoes_auxiliares import *

def bsort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(1,n-i):
            if v[j-1]>v[j]: troca(v, j-1, j)


def ssort(v):
    n = len(v)
    for i in reversed(range(1, n)):
        j = seleciona(v, i+1)
        troca(v,i,j)


def isort(v):
    n = len(v)
    for i in range(1, n):
        insere(v[i], v, i-1)


def hsort(v):
    n = len(v)
    amontoa(v)
    for i in reversed(range(n)):
        troca(v, 0, i)
        desce(v, 0, i)


def msort(v):
    ms(v, 0, len(v)-1)


def qsort(v):
    qs(v, 0, len(v)-1)
