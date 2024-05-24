import scipy

def func1(y, x):
    return y + (1 + x) * y**2
  
t = scipy.integrate.odeint(func1, -1, [1, 1.5])

print(t)