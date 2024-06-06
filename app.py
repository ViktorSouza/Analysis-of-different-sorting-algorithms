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
 ## Turma:
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
from random import randint
from sys import platform
random.seed(32)
import time

mytime = time.perf_counter
plt.style.use("ggplot")
# plt.grid()

def mediaT(V, n):
    values_sum = 0
    for num in V:
        values_sum += num
    return values_sum / n


def varT(V, n):
    avg = mediaT(V, n)
    std = 0
    for num in V:
        std += (num - avg) ** 2
    std = std / n
    std = std ** (1 / 2)
    return std


def counting(V, n):
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
    result = 0
    for i in V:
        if i == n:
            result += 1
    return result


def selection(V, n):
    for i in range(0, n):
        smallest_num_index = i
        for j in range(i, n):
            if V[j] < V[smallest_num_index]:
                smallest_num_index = j
        V[i], V[smallest_num_index] = V[smallest_num_index], V[i]


def bubble(V, n):

    lim = n - 1
    while lim >= 0:
        isIncreasing = True
        for j in range(lim):
            if V[j] > V[j + 1]:
                isIncreasing = False
                V[j], V[j + 1] = V[j + 1], V[j]
        if(isIncreasing==True): 
                break
        lim -= 1


def insertion(V, n):
    last_index = 0
    for i in range(last_index,n - 1):
        if V[i] > V[i + 1]:
            j = i
            while V[j] > V[j + 1]:
                V[j + 1], V[j] = V[j], V[j + 1]
                if j <= 0:
                    break
                j -= 1


def sort(V,n):
    #Native Python algorithm
    V.sort()



def embaralha(V, n, p):
    for _ in range(int(n * p / 2)):
        num1 = randint(0, n - 1)
        num2 = randint(0, n - 1)
        V[num1], V[num2] = V[num2], V[num1]


def timeMe(func, V, n, m, p):
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
    for i in range(len(mediaMCMPi)):
        plt.errorbar(mpontos, mediaMCMPi[i],desvioMCMPi[i],label = algorithms_names[i],fmt='o')
        plt.legend()
    plt.savefig(f'./plots/result_{time.time()}.png')
    # plt.show()
    plt.clf()





sizes = [1000, 5000, 10000, 50000, 100000]
n = 100000
# n = 500
# sizes = [100,200,300,400,500]
percentages = [0.01,0.03,0.05,0.1,0.5]
algorithms = [selection,bubble,insertion,counting,sort]
algorithms_names = ['Seleção','Bolha','Inserção','Contagem','Nativo']

def main():
    # Como não há o parâmetro para colocar as legendas em GraficaSortings, teve-se que colocar os nomes e os algoritmos como variáveis globais.
    global algorithms_names
    global algorithms
    avg_exp_1 = []
    std_exp_1 = []
    avg_exp_2 = []
    std_exp_2 = []

    #A fim de diminuir possiveis variâncias, foram criadas as listas antes
    arrays = [[randint(0,9999) for _ in range(i)] for i in sizes]
    for i,algorithm in enumerate(algorithms):
        avg = []
        std = []
        for j,size in enumerate(sizes):
            Vtmp = list(arrays[j])

            media,var = timeMe(func=algorithm,V=Vtmp,n=size,m=10,p=0)
            avg.append(media)
            std.append(var)
            print(f'Size, {algorithms_names[i]}, {size}', {time.time()})

        avg_exp_1.append(avg)
        std_exp_1.append(std)
        
    plt.ylabel('Tempo')
    plt.xlabel("Quantidade de elementos")
    GraficaSortings(sizes,avg_exp_1,std_exp_1)


    algorithms = [bubble,insertion]
    algorithms_names = ['Bolha','Inserção']
    # for algorithm in algorithms:
    for i,algorithm in enumerate(algorithms):
        avg = []
        std = []
        V  = [i for i in range(n)]
        for percent in percentages:
            Vtmp = list(V)
            embaralha(Vtmp,len(Vtmp),percent)
            media,var = timeMe(func=algorithm,V=Vtmp,n=len(Vtmp),m=10,p=percent)
            avg.append(media)
            std.append(var)
            print(f'Percentage, {algorithms_names[i]}, {percent*100}%, {time.time()}')
        avg_exp_2.append(avg)
        std_exp_2.append(std)
    plt.ylabel('Tempo')
    plt.xlabel("Porcentagem de embaralhamento")
    GraficaSortings(percentages,avg_exp_2,std_exp_2)

        

main()