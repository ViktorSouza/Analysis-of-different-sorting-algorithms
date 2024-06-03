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
from random import random
from random import randint
from sys import platform
import time

mytime = time.perf_counter
plt.style.use("seaborn-v0_8")

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
        for j in range(lim):
            if V[j] > V[j + 1]:
                V[j], V[j + 1] = V[j + 1], V[j]
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



def embaralha(V, n, p):
    for _ in range(int(n * p / 2)):
        num1 = randint(0, n - 1)
        num2 = randint(0, n - 1)
        V[num1], V[num2] = V[num2], V[num1]


def timeMe(func, V, n, m, p):
    perf = []
    for _ in range(m):
        start = mytime()
        func(V, n)
        end = mytime()
        perf.append((end - start)/1000)
    return (mediaT(perf, len(perf)), varT(perf, len(perf)))


def GraficaSortings(mpontos, mediaMCMPi, desvioMCMPi):
    for i in range(len(mpontos)):
        plt.errorbar(percentages, mediaMCMPi[i], yerr=desvioMCMPi[i],label = sizes[i])
        plt.ylabel('Tempo')
        plt.xlabel("Porcentagem de embaralhamento")
        plt.legend()
        plt.savefig(f'./plots/percent_{i}.png')
        plt.plot




# sizes = [1000, 5000, 10000, 50000, 100000]
sizes = [10,20,30]
percentages = [0.01,0.03,0.05,0.1,0.5]
algorithms = [selection,bubble,counting,insertion]
algorithms_names = ['Selection','Bubble','Counting','Insertion']

def main():
    # algorithms = [selection,bubble,insertion,counting]
    for algorithm in algorithms:
        avg_result = []
        std_result = []
        for i in sizes:
            avg = []
            std = []
            V = [i for i in range(i)]
            for j in percentages:
                V_copy = embaralha(V,len(V),i)
                result = timeMe(algorithm,V,i,10,j)
                std.append(result[1])
                avg.append(result[0])     

            avg_result.append(avg)
            std_result.append(std)
        print(avg_result)
        GraficaSortings(sizes,avg_result,std_result)

        

main()