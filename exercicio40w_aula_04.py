#40. Exibir os vinte primeiros valores da série de Bergamaschi. A série: ,
# 1, 1, 1, 3, 5, 9, 17
a=1
b=1
c=1
i=1

#  a  b  c  d 
#  1  0  0  1
#  0  1  0  1
#  0  0  1  1
#  1  1  1  3 
#  0  0  0  5
#  0  0  0  9

while(i<=20):
    print(a)
    d=a+b+c
    a=b
    b=c
    c=d
      
    i=i+1