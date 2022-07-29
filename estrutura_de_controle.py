


Titulo = 'Programa de Aposentadoria'

print(f'{Titulo: ^50}')

Idade = int(input('Qual a sua idade? '))
sexo = input('Qual seu sexo?  ')

if sexo.casefold() == "feminino" or sexo.casefold() == "mulher":
    if Idade >= 60:
        print('Sua aposentadoria está liberada')
    else:
        print(f'Você ainda não tem idade suficiante para aposentar. Aguarde mais {60 - Idade} anos!')

elif sexo.casefold() == "masculino" or sexo.casefold() == "homem" \
    or sexo.casefold() == "homosexual":
    if Idade >= 65:
         print('Sua aposentadoria está liberada')
    else:
        print(f'Você ainda não tem idade suficiante para aposentar.  Aguarde mais {65 - Idade} anos! ')

else:
    print('Voce não digitou o sexo corretamente')
