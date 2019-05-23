import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("datos.dat")
x = data[:,0]
y = data[:,1]
plt.figure()
plt.plot(x,y)
plt.savefig("GonzalezMauricio_final_15.pdf")
