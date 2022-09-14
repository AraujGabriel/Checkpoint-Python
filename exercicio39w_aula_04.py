#39. Exibir os trinta primeiros valores da série de Fibonacci. A série: 1, 1, 2, 3, 5, 8, ...
a=1
b=0
f=0
i=1

while(i<=30):
    f=a+b
    print(f)
    a=b
    b=f
    f=a
    i=i+1


