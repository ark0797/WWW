import math
def function(x):
    y=math.log(math.exp(1/(math.sin(x) + 1))/(1.25 + (1/(x**15))), 1 + x**2)
    return y
print(function(1), function(10), function(1000))
