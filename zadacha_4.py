# Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. 
# Напишите программу, которая определит на какое место в шеренге Пете нужно встать,
# чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). 
# Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

import random

number=int(input('Введите число учеников->'))
massiv=([0]*number)
for i in range(number):
    massiv[i]=int(random.randint(150,200+1))
   # print(massiv[i], end=" ")
print()

for i in range(len(massiv)):
    for j in range(len(massiv)):
         if(massiv[i]>massiv[j]):
             temp=massiv[j]
             massiv[j]=massiv[i]
             massiv[i]=temp
for i in range(number):
    print(massiv[i], end=" ")
print()

rost=int(input('Введитет рост Пети ->'))
flag=False
i=0
while( i < len(massiv) and flag==False ):
    if(rost>massiv[i]):
        print(f'Номер Петра в шеренге по убыванию роста {i+1}')
        flag=True
    elif(i==len(massiv)-1):
         print(f' Стр 2 Номер Петра в шеренге по убыванию роста {i+2}')
         flag=True
    i+=1

massiv.append(rost)
for i in range(len(massiv)):
     for j in range(len(massiv)):
          if(massiv[i]>massiv[j]):
                temp=massiv[j]
                massiv[j]=massiv[i]
                massiv[i]=temp
for i in range(len(massiv)):
    print(massiv[i], end=" ")
print()

