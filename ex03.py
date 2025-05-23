"""Implemente um programa em Python que:
• Receba uma lista de números inteiros positivos N = [5000, 10000, 15000, 20000].
• Para cada número n da lista, calcule o valor de log10(fatorial(n)) (pois o fatorial é grande
demais para ser exibido diretamente).
• Execute esses cálculos em paralelo, utilizando múltiplos núcleos.
• Ao final, exiba uma tabela com n e o valor de log10(n!).
Como o valor de n! cresce rapidamente, a dica é calcular: log10(𝑛𝑛!) = log10(1) +
log10(2) + ⋯ + log10 𝑛𝑛. Isso evita estouro de memória e permite comparação entre grandes
fatoriais.
Requisitos funcionais
• Utilize ProcessPoolExecutor para o paralelismo real
• Crie uma função log_fatorial(n) que retorna (n, log10(n!))
3
• Use math.log10.
• Exiba a saída com 4 casas decimais de precisão."""

import concurrent.futures
import math
from tabulate import tabulate

header = ["n", "log10(n!)"]
N = [5000, 10000, 15000, 20000]

def log_fatorial(n):
    x=0
    ENE = []
    for i in range(1, n+1):
        x += math.log10(i)
    return ([n, x])
    #return (n, log10(n!))

with concurrent.futures.ProcessPoolExecutor() as executor:
    a = list(map(log_fatorial, N))
    print(tabulate(a, headers=header, tablefmt='fancy_grid', numalign='center', stralign='center'))