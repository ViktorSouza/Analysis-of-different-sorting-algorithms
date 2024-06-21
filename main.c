#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

void selectionC(int *V, int n)
{
    for (int i = 0; i < n; i++)
    {
        int smallestElementIndex = i;
        for (int j = i + 1; j < n; j++)
        {
            if (V[j] < V[smallestElementIndex])
            {
                smallestElementIndex = j;
            }
        }
        int temp = V[i];
        V[i] = V[smallestElementIndex];
        V[smallestElementIndex] = temp;
    }
};

void bubbleC(int *V, int n)
{

    int lim = n - 1;
    while (lim >= 0)
    {
        int isIncreasing = true;
        for (int j = 0; j < lim; j++)
        {
            if (V[j] > V[j + 1])
            {
                isIncreasing = false;
                int temp = V[j];
                V[j] = V[j + 1];
                V[j + 1] = temp;
            }
        }
        if (isIncreasing == true)
            break;
        lim -= 1;
    }
};
void insertionC(int *V, int n)
{
    int last_index = 0;
    for (int i = last_index; i < n - 1; i++)
    {
        if (V[i] > V[i + 1])
        {
            int j = i;

            // Nesta parte, caso V[i + 1] seja menor do que V[i], então o elemento V[i] será colocado uma posição à esquerda quantas vezes forem necessárias até que esteja no lugar correto
            while (V[j] > V[j + 1])
            {
                int temp = V[j];
                V[j] = V[j + 1];
                V[j + 1] = temp;
                if (j <= 0)
                    break;
                j -= 1;
            }
        }
    }
};
int count_element_in_array(int n, int V[], int size)
{

    int result = 0;
    for (int i = 0; i < size; i++)
    {

        if (V[i] == n)
            result += 1;
    }
    return (result);
}
int max(int V[], int n)
{
    int largest = V[0];
    for (int i = 1; i < n; i++)
    {
        if (V[i] > largest)
            largest = V[i];
    }
    return largest;
}
void countingC(int *V, int n)
{
    int max_element = max(V, n);
    int *hist_list = malloc(sizeof(int) * (max_element + 1));
    for (int i = 0; i < max_element + 1; i++)
        hist_list[i] = count_element_in_array(i, V, n);
    int index = 0;

    for (int i = 0; i < max_element + 1; i++)
    {
        for (int j = 0; j < hist_list[i]; j++)
        {
            V[index] = i;
            index += 1;
        }
    }
};
