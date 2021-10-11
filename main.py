# graphing functions
import matplotlib.pyplot as plt
import numpy as np



a=np.linspace(0.5, 0.7, 50)
f_a = np.vectorize(lambda a: ((3/(a**2))-1/(1-a)**2)) 
y=f_a(a)
plt.plot(a, y, label='Force (arb units)')
plt.xlabel("a (x/d)")
plt.ylabel("Force (arb units")

plt.legend()
plt.show()