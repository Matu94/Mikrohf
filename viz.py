import matplotlib.pyplot as plt
from math import cos, sin, radians
f = "mikro10.csv"
m = [line.strip().split("\t") for line in open(f)]
szog = []
tav = []
for meres in m[1]:
    a = meres.strip().split(",")
    szog.append(radians(float(a[1])))
    tav.append(float(a[2][:-1]) / 1000)
    
for i in range(len(tav)):
    '''
    plt.subplot(121)
    plt.plot(szog[i], tav[i], "b*")
    plt.subplot(122)
    '''
    plt.plot((0, sin(szog[i])*tav[i]), (0, cos(szog[i])*tav[i]), "r*-")
plt.axis("equal")
plt.grid(True)
plt.show()