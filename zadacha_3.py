#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n=int(input('Введите число  N ->'))
i=1
flag=False
while(flag==False):
    i+=1
    if(int(n%i)==0):
        flag=True
print(f"НОД числа N={n}, не равный 1, -> {i}")
print()