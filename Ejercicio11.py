#Escribir un programa que almacene las matrices:
A =[[1,2,3],[4,5,6]]
B = [[-1,0,1],[0,1,1]]
list= [] 
list1=[]
list2=[]
list3=[]
product= []
product1=[]
d=0
d1=0
d2=0
d3=0
while d<3:
    a=A[0][d]
    b=B[0][d]
    x=a*b
    list.append(x)
    d=d+1
pr=sum(list)
product.append(pr)
while d1<3:
    a=A[0][d1]
    b=B[1][d1]
    x=a*b
    list1.append(x)
    d1=d1+1
seg=sum(list1)
product.append(seg)
while d2<3:
    a=A[1][d2]
    b=B[0][d2]
    x=a*b
    list2.append(x)
    d2=d2+1
ter=sum(list2)
product1.append(ter)
while d3<3:
    a=A[1][d3]
    b=B[1][d3]
    x=a*b
    list3.append(x)
    d3=d3+1
cua=sum(list3)
product1.append(cua)
print(product)
print(product1)