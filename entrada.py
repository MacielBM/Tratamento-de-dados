import math
from multiprocessing.connection import wait

nome = input("digite seu nome: ")#str
idade = int(input("digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("digite sua altura: "))
ICM = peso/altura**2

print("Seu nome é",nome, "Voce tem",idade,"anos e pesa",peso, "seu ICM é",ICM)

