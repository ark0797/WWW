x0=4.00
x1=4.25
i=2
for i in range (2,30):
    x=float(108-(815-1500/x1)/x0)
    (x1,x0)=(x,x1)
    i+=1
print(x)
