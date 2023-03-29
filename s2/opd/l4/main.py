def f(x):
   if x >= 0 or x < -1238: return 3*x + 247
   return -1238
 
def r(x, y, z): return f(x) - f(y) - f(z+1) + 2

print(f(-10840))
print(f(10840))
print(r(40, 40, 40))