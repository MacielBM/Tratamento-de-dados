lista = ['a','x','s','w','d','a','n','a']
lista.reverse()                          
''' inverte todos os elementos da lista 
assim como:
             lista[0:0:-1]

'''
lista.sort()            
 #colocar em ordem alfabetica ou crescente 
for i in range(len(lista)):
    print(lista[i])

l = lista.count('a')                
#lista pode ser representada por 'l'

print("existem", l ,'letras')