import numpy as np
import matplotlib.pyplot as plt
inp = open("input.txt","r")
s = inp.read().split()
s_len=[len(x) for x in s]
max_len=max(s_len)
ms=[0]*max_len
for x in s_len: 
    ms[x-1]+=1
y_pos=[1+i for i in range(max_len)]
plt.bar(y_pos, ms, align='center', alpha=0.8)
plt.xticks(y_pos, y_pos)
plt.xlabel('длины слов')
plt.ylabel('сколько раз')
plt.ylabel('Value')
plt.title('Bar title')
plt.show()
