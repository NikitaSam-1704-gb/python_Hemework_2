#Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно

n=int(input('Введите число элементов натурального ряда чисел N ->'))
res=0
if n<=0:
    res=-int(((abs(n)+1))/2)*abs(n)+1
    print(f"Сумма значений элементов натурального ряда N={n} равна {res}")
if n>0:
    res=int(((n+1))/2)*n
    print(f"Сумма значений элементов натурального ряда N={n} равна {res}")
print()