enru=open('en-ru.txt', 'r')
A=enru.read()
A=A.split()
B=[]
C=[]
i=0
while i<=len(A)-3:
    B.append(A[i])
    i+=3
j=2
while j<=len(A):
    C.append(A[j])
    j+=3 
E=dict(zip(B, C))  

input=open('input.txt','r')
d=input.read()
d=d.lower()
d=d.replace(',', ' ')
d=d.replace('!', ' ')
d=d.replace('?', ' ')
d=d.replace('.', ' ')
d=d.split()
F=[]
k=0
while k<=len(d)-1:
    if d[k] in E:
        F.append(E[d[k]])
    k+=1
f=' '.join(F)
output=open('output.txt', 'w')
output.write(f)

