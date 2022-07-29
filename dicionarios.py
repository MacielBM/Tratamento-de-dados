'''           keys:values
dicionario = {'a':'amor','b':'blue'}
dicionario2 = {1:20, 3:30, 4:40}
dicionario3 = {5.5:50.50, 30.1:30.25}
dicionario4 = {(10,20):['paython','linguagem',10]}
print(dicionario)
print(dicionario.get(input(),"Valor Não encontrado"))   '''


         #  keys:"values"
agenda = {40408021:"José",87541236:"heloise",78945612:"carlos",36925874:"claudio"}
#del(agenda[40408021])

print(agenda.keys())       #imprime apenas as chaves    (telefones)
print(agenda.values())      #imprime apenas os valores (nomes)
print(len(agenda))            #imprime quantos itens existem

print(agenda.popitem())      #remove o ultimo item da lista (.popitem)
print(agenda.pop(40408021))   #remove o item indicado (.pop)
