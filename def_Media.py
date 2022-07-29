import math
from msilib.schema import Media
from statistics import median, median_grouped

lista = [1,2,3,54,5,7,8]
def media(lista):
    soma = 0.0
    for r in lista:
        soma += r
    return soma / len(lista)

media_lista = media(lista)
print(f'{media_lista:,.2f}')