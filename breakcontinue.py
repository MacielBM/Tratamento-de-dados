import time

'''
print("entando no laço...")
for i in range(10):
    print(i)
    time.sleep(1)
    if (i==5):
        break
print("saindo do laço...")

'''

print("entando no laço...")
i = 0
while(i<10):
    i+=1
    if (i%2==0):
        continue
    print(i,end=' ') 
    print('É número impar')



    i+=1
    if (i%2==0):
        print(i,end=' ') 
        print('É número par')

print("saindo do laço...")