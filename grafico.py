from pylab import xlabel, ylabel, grid, show, plot, legend, title
from funcoes_auxiliares import tempo, seq


def gera_grafico(*f, N=(500, 5000, 500)):
    n = list(range(N[0], N[1]+1, N[2]))
    cor = ['b', 'r', 'w', 'k', 'g', 'y', 'c']
    linha = ['-', '--', ':', '-.']
    marcador = ['x', 'd', 'D', 's']
    i = 0
    w = list()

    for algoritmo in f:
        T = list()
        for tamanho in n:
            t = tempo(algoritmo, seq(tamanho), True)
            T.append(t)

        plot(n, T, color=cor[i], marker=marcador[i], label=algoritmo.__name__)
        i += 1
        print('{} Sort finalizado: {:.3f}'.format(algoritmo.__name__, sum(T)))

    xlabel('Tamanho')
    ylabel('Tempo')
    legend(loc='upper left')
    grid(True)
    show()
