"""O objetivo do exercício é implementar um programa em Python que simule a geração de séries
temporais para diferentes regiões do país. Para cada região identifique o maior intervalo contínuo
de dias com temperatura acima de 40°C. A análise de todas as regiões deve ser executada em
paralelo, distribuindo o trabalho entre os núcleos da CPU. Exiba, ao final, a região e o seu maior
período de onda de calor.
Por exemplo: considere que a sequência de dias para a região "Norte" é [38, 41, 42, 39, 44, 45,
46, 30, 41], portanto, o maior período contínuo acima de 40°C é de 3 dias consecutivos (dias 5 a
7: 44, 45, 46). Exibir, ao final, uma tabela com os nomes das regiões e seus respectivos maiores
períodos de calor extremo. Observação: gere os valores de temperatura para 10 dias. 
"""
from tabulate import tabulate
import concurrent.futures

regioes = {
    "Norte":[38, 41, 42, 39, 44, 45, 46, 30, 41, 42],
    "Nordeste":[39, 35, 47, 47, 33, 30, 40, 40, 37, 31],
    "Centro-Oeste":[44, 34, 36, 38, 49, 50, 45, 50, 33, 41],
    "Sudeste":[40, 35, 31, 39, 40, 49, 31, 30, 39, 43],
    "Sul":[33, 41, 45, 42, 30, 42, 41, 30, 33, 41]
}

header = ["Região", "Maior período de calor extremo (> 40°C)"]

def mais_40(temperaturas):
    max_periodo = 0
    periodo_atual = 0

    for temp in temperaturas:
        if temp > 40:
            periodo_atual += 1
            if periodo_atual > max_periodo:
                max_periodo = periodo_atual
        else:
            periodo_atual = 0

    return max_periodo

def gerar_tabela(regioes):
    tabela = []
    scrufles = list(map(mais_40, regioes.values()))
    for i, regiao in enumerate(regioes.keys()):
        tabela.append([regiao, scrufles[i]])
    return tabela

def gerar_tabela(regioes):
    tabela = []
    scrufles = list(map(mais_40, regioes.values()))
    for i, regiao in enumerate(regioes.keys()):
        tabela.append([regiao, scrufles[i]])
    return tabela

with concurrent.futures.ProcessPoolExecutor() as executor:
    tab = gerar_tabela(regioes)
    print(tabulate(tab, headers=header, tablefmt='fancy_grid', numalign='center', stralign='center'))