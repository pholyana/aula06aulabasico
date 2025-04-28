A=[0,0,0,0,0]
x=0
m=[0,0,0,0,0]
for c in range(len(A)):
    A[c]=int(input("digite um numero:"))
x = int (input("digite um valor multiplicador:"))
for i in range(len(m)):
    m[i]=x*A[i]
print(A)
print(x)
print(m)