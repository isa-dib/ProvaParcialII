"""Implemente um programa em Python que:
• Receba uma lista com diferentes tamanhos de plantação (pares (m, n)), por exemplo: [(3, 3),
(4, 5), (6, 6), (10, 8), (12, 12)].
• Para cada grade m × n, calcule quantos caminhos distintos existem do ponto (0, 0) ao ponto
(m−1, n−1) com movimentos apenas para direita ou para baixo.
• Execute todos os cálculos em paralelo, utilizando múltiplos núcleos da CPU.
• Exiba, ao final, uma tabela com o tamanho da grade e o número de caminhos possíveis.
Requisitos funcionais:
• Utilize ProcessPoolExecutor para realizar o processamento em paralelo
• O cálculo de cada grid deve ser feito em uma função separada, paralelizável
• A resposta para cada grade (m, n) deve ser o número de caminhos distintos"""
import concurrent.futures
from tabulate import tabulate

pares =  [(3, 3),(4, 5), (6, 6), (10, 8), (12, 12)]
a = []
header = ["Grade (m x n)", "Número de caminhos distintos"]

def contar_caminhos(inicio, fim, m, n):
    if inicio == m-1 and fim == n-1:
        return 1
    if inicio >= m or fim >= n:
        return 0
    return contar_caminhos(inicio+1, fim, m, n) + contar_caminhos(inicio, fim+1, m, n)

with concurrent.futures.ProcessPoolExecutor() as executor:
    for i in pares:
        m = i[0]
        n = i[1]
        resultado = contar_caminhos(0, 0, m, n)
        a.append([f"{m} x {n}", resultado])
    print(tabulate(a, headers=header, tablefmt='fancy_grid', numalign='center', stralign='center'))