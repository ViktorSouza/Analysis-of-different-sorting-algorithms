#################################################################
## AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
## DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
## TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
## DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
## DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
## OU PLÁGIO.
## DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
## DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
## SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
## DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
## DIVULGADOS NA PÁGINA DA DISCIPLINA.
## ENTENDO QUE EPS SEM ESTE CABEÇALHO NÃO SERÃO CORRIGIDOS E,
## AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.
## Nome : João Viktor Souza Almeida
## NUSP : 15521614
## Turma: MAC0110-145-2024
## Prof.: Roberto Hirata Jr.
## Referências: Com exceção das rotinas fornecidas no enunciado
## e em sala de aula, caso você tenha utilizado alguma referência,
## liste-as abaixo para que o seu programa não seja considerado
## plágio ou irregular.
## Exemplo:
##- O algoritmo Quicksort foi baseado em
## http://wiki.python.org.br/QuickSort
#################################################################

import matplotlib.pyplot as plt
import random
from multiprocessing import Process
from random import randint
from sys import platform
import ctypes
import json

debug = True


random.seed(32)
import time

mytime = time.perf_counter
plt.style.use("ggplot")

libsort = ctypes.CDLL("./libsortings.so")

libsort.selectionC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.insertionC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.bubbleC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.countingC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]


def mediaT(V, n):
    """
    Retorna a média dos elementos da lista V, ou seja, a soma de todos os elementos de V dividido por n

    Argumentos:
        V(int[]): lista de números
        n(int): número natural que indica a quantidade de elementos em V
    Retorna:
        Média dos valores de V
    """

    values_sum = 0
    for num in V:
        values_sum += num
    return values_sum / n


def varT(V, n):
    """
    Retorna a variância dos elementos da lista V

    Argumentos:
        V(int): lista de números
        n(int[]): número natural que indica a quantidade de elementos em V
    Retorna:
        A variância dos elementos da lista V
    """
    avg = mediaT(V, n)
    std = 0
    for num in V:
        std += (num - avg) ** 2
    std = std / (n - 1)
    return std


def counting(V, n):
    """
    Implementa o algoritmo contagem, bem como ordena a lista V com a implementação realizada.

    Argumentos:
        V(list): lista de números
        n(int): quantidade de elementos em V

    Retorno:
        Esta função não possui retorno
    """
    max_element = max(V)
    hist_list = [0 for _ in range(max_element + 1)]
    for i in range(max_element + 1):
        hist_list[i] = count_element_in_array(i, V)
    index = 0
    for i in range(max_element + 1):
        for _ in range(hist_list[i]):
            V[index] = i
            index += 1


def count_element_in_array(n, V):
    """
    Função auxiliar do algoritmo de contagem. Tem como objetivo identificar o número de vezes que o elemento n aparece na lista V

    Argumentos:
        n(int): elemento a ser contado
        V(list): lista de números
    Retorna:
        int: quantidade de vezes que o elemento n aparece na lista V
    """

    result = 0
    for i in V:
        if i == n:
            result += 1
    return result


def selection(V, n):
    """
    Implementa o algoritmo de seleção, bem como ordena a lista V com a implementação realizada.

    Argumentos:
        V(list): lista de números
        n(int): quantidade de elementos em V

    Retorno:
        Esta função não possui retorno
    """
    for i in range(0, n):
        smallest_num_index = i

        for j in range(i, n):
            if V[j] < V[smallest_num_index]:
                smallest_num_index = j

        V[i], V[smallest_num_index] = V[smallest_num_index], V[i]


def bubble(V, n):
    """
    Implementa o algoritmo de bolha, bem como ordena a lista V com a implementação realizada.

    Argumentos:
        V(list): lista de números
        n(int): quantidade de elementos em V

    Retorno:
        Esta função não possui retorno
    """
    lim = n - 1

    while lim >= 0:
        isIncreasing = True
        for j in range(lim):
            if V[j] > V[j + 1]:
                isIncreasing = False
                V[j], V[j + 1] = V[j + 1], V[j]
        if isIncreasing == True:
            break
        lim -= 1


def insertion(V, n):
    """
    Implementa o algoritmo de inserção, bem como ordena a lista V com a implementação realizada.

    Argumentos:
        V(list): lista de números
        n(int): quantidade de elementos em V

    Retorno:
        Esta função não possui retorno
    """
    last_index = 0
    for i in range(last_index, n - 1):
        if V[i] > V[i + 1]:
            j = i
            # Nesta parte, caso V[i+1] seja menor do que V[i], então o elemento V[i] será colocado uma posição à esquerda quantas vezes forem necessárias até que esteja no lugar correto
            while V[j] > V[j + 1]:
                V[j + 1], V[j] = V[j], V[j + 1]
                if j <= 0:
                    break
                j -= 1


def sort(V, n):
    """
    Implementação do algoritmo nativo do Python.

    Argumentos:
        V(list): lista de números
        n(int): quantidade de elementos em V

    Retorno:
        Esta função não possui retorno
    """
    V.sort()


def countingC(V, n):
    pV = (ctypes.c_int * n)(*V)
    libsort.countingC(pV, n)


def selectionC(V, n):
    pV = (ctypes.c_int * n)(*V)
    libsort.countingC(pV, n)


def insertionC(V, n):
    pV = (ctypes.c_int * n)(*V)
    libsort.countingC(pV, n)


def bubbleC(V, n):
    pV = (ctypes.c_int * n)(*V)
    libsort.countingC(pV, n)


def embaralha(V, n, p):
    """
    Dada uma lista V, são embaralhados p% da lista.

    Argumentos:
        V(list): lista de números
        n(int): quantidade de elementos em V
        p(int): porcentagem de embaralhamento

    Retorno:
        Esta função não possui retorno
    """

    for _ in range(int(n * p / 2)):
        num1 = randint(0, n - 1)
        num2 = randint(0, n - 1)
        V[num1], V[num2] = V[num2], V[num1]


def timeMe(func, V, n, m, p):
    """
    Dada uma lista V, são embaralhados p% da lista.

    Argumentos:
        func(function): algoritmo de ordenação a ser chamado
        V(list): lista de números
        n(int): quantidade de elementos em V
        m(int): número de repetições
        p(int): porcentagem de embaralhamento

    Retorno:
        Esta função não possui retorno
    """
    perf = []
    Vtemp = list(V)

    for _ in range(m):
        start = mytime()
        func(Vtemp, n)
        end = mytime()
        Vtemp = list(V)
        perf.append(end - start)

    return (mediaT(perf, len(perf)), varT(perf, len(perf)))


def GraficaSortings(mpontos, mediaMCMPi, desvioMCMPi):
    """
    Dados os vetores mpontos, mediaMCMPi e desvioMCMPi, é criado um gráfico utilizando uma barra de erro

    Argumentos:
        mpontos(int[]): valores numéricos do eixo x
        mediaMCMPi(int[][]): todas as médias a serem colocadas no gráfico
        mediaMCMPi(int[][]): os respectivos desvios-padrões da mediaMCMPi

    Retorno:
        Esta função não possui retorno
    """
    for i in range(len(mediaMCMPi)):
        plt.errorbar(
            mpontos, mediaMCMPi[i], desvioMCMPi[i], label=algorithms_names[i], fmt="o"
        )
        plt.legend()
    if debug:
        plt.show()
    else:
        plt.savefig(f"./plots/result_{time.time()}.png")

    # plt.clf()


algorithms_names = []


def first_test():
    global algorithms_names
    avg_exp_1 = []
    std_exp_1 = []

    sizes = [200, 500, 1000, 1500] if debug else [1000, 5000, 10000, 50000, 100000]

    algorithms = [counting, countingC, bubbleC, selectionC, insertionC]
    algorithms_names = ["Contagem", "Contagem C", "Bolha C", "Seleção C", "Inserção C"]
    # A fim de diminuir possiveis variâncias, foram criadas as listas antes
    arrays = [[randint(0, 9999) for _ in range(i)] for i in sizes]
    for i, algorithm in enumerate(algorithms):
        avg = []
        std = []
        for j, size in enumerate(sizes):
            Vtmp = list(arrays[j])

            media, var = timeMe(func=algorithm, V=Vtmp, n=size, m=10, p=0)
            avg.append(media)
            std.append(var)
            print(f"Size, {algorithms_names[i]}, {size}", {time.time()})

        avg_exp_1.append(avg)
        std_exp_1.append(std)

        with open("data.json", "r") as f:
            data = json.load(f)
        data["avg_exp_1"] = list(zip(algorithms_names, avg_exp_1))
        data["std_exp_1"] = list(zip(algorithms_names, std_exp_1))
        with open("./data.json", "w") as f:
            json.dump(data, f, indent=4)

    plt.ylabel("Tempo (s)")
    plt.xlabel("Quantidade de elementos")
    GraficaSortings(sizes, avg_exp_1, std_exp_1)


def second_test():
    global algorithms_names
    avg_exp_2 = []
    std_exp_2 = []

    n = 200 if debug else 100000
    percentages = [0.01, 0.03, 0.05, 0.1, 0.5]
    algorithms = [bubble, insertion]
    algorithms_names = ["Bolha", "Inserção"]

    for i, algorithm in enumerate(algorithms):
        avg = []
        std = []
        V = [i for i in range(n)]

        for percent in percentages:
            Vtmp = list(V)
            embaralha(Vtmp, len(Vtmp), percent)
            media, var = timeMe(func=algorithm, V=Vtmp, n=len(Vtmp), m=10, p=percent)
            avg.append(media)
            std.append(var)
            print(f"Percentage, {algorithms_names[i]}, {percent*100}%, {time.time()}")

        avg_exp_2.append(avg)
        std_exp_2.append(std)

    plt.ylabel("Tempo (s)")
    plt.xlabel("Porcentagem de embaralhamento")

    with open("data.json", "r") as f:
        data = json.load(f)
    data["avg_exp_2"] = list(zip(algorithms_names, avg_exp_2))
    data["std_exp_2"] = list(zip(algorithms_names, std_exp_2))
    with open("./data.json", "w") as f:
        json.dump(data, f, indent=4)

    GraficaSortings(percentages, avg_exp_2, std_exp_2)


def main():
    first_test()
    second_test()


main()
