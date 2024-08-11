import time

print('GERANDO TABUADAS',end=' ')
for t in range (3):
    time.sleep(1.5)
    print('.',end=' ')
time.sleep(3)
print('')

for tabuada in range (1,11):
    print('_'*20)
    for numero in range (1,11):
        total = str(tabuada * numero).zfill(2)
        if total != '100':
            print(f'|    {tabuada} x {str(numero).zfill(2)} = {total}    |')
        else:
            print(f'|    {tabuada} x {str(numero).zfill(2)} = {total}   |')
print('_'*20)
print('')