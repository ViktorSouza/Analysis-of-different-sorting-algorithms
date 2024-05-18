import matplotlib.pyplot as plt
from random import random
from random import randint
from sys import platform
import time

mytime = time.perf_counter
plt.style.use("seaborn-v0_8")
results = []
sizes = [100,200,500]
percentages = [0,0.1,0.5,1]
std = []

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
    """ 
    media [1,2,3,4,5]

    mpontos = [    x% y% z% w%
        n = 1000  [1, 2, 3, 4]
        n = 5000  [1, 2, 3, 4]
        n =...    [1, 2, 3, 4]
        n =...    [1, 2, 3, 4]
        n =...    [1, 2, 3, 4]
    ]
     """
    for size in mpontos:
        # plt.label()
        plt.xlabel("Porcentagem")
        plt.ylabel('Tempo')
        plt.errorbar(size, mediaMCMPi, yerr=desvioMCMPi, fmt="o",)
        plt.savefig(f'./plot_{size}numbers.png')
        # for percentage in size:


# Just my code :D l
# def plot(func, label, m, p): 
#     x = [i/m for i in range(m)]
#     y = [0 for _ in range(m)]
#     std = [0 for _ in range(m)]
#     V = [randint(0,9999) for _ in range(m)]
#     for i in range(m):
#         copy_V = list(V)
#         embaralha(copy_V, len(copy_V), i/m)
#         y[i], std[i] = timeMe(func, copy_V, len(copy_V), 10, i/100)
#     plt.plot(x, [i for i in y])
#     # plt.errorbar(x, [i/1000 for i in y], yerr=std, fmt="o")
#     # print(x)
#     plt.xlabel('Embaralhamento')
#     plt.ylabel('Tempo (ms)')

def main():
    for i in sizes:
        iti = []
        V = [i for i in range(i)]
        for j in percentages:
            V_copy = embaralha(V,len(V),i)
            result = timeMe(insertion,V,i,10,j)
            std.append(result[1])
            iti.append(result[0])     
        results.append(iti)
    GraficaSortings(results,[],std)
        

main()