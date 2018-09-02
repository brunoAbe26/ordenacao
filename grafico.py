from pylab import xlabel, ylabel, grid, show, plot, legend, title
from funcoes_auxiliares import tempo, seq, get_nome_algoritmos


def gera_grafico(*f, N=(500, 5000, 500)):
    n = list(range(N[0], N[1]+1, N[2]))
    cor = ['b', 'r', 'g', 'k', 'y', 'c']
    marcador = ['x', 'd', 'D', 's']
    i = 0
    dict_algoritmos = get_nome_algoritmos()

    for algoritmo in f:
        T = list()
        nome = dict_algoritmos[algoritmo.__name__]
        for tamanho in n:
            t = tempo(algoritmo, seq(tamanho), True)
            T.append(t)

        plot(n, T, color=cor[i], marker=marcador[i], label=nome)
        i += 1
        print('{} Sort finalizado: {:.3f}'.format(nome, sum(T)))

    xlabel('Tamanho')
    ylabel('Tempo')
    legend(loc='upper left')
    grid(True)
    show()
