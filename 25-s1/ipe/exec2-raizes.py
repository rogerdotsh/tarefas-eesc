# ax² + bx + c = 0
import math

a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4*a*c

if delta < 0:
    print("-1")
elif delta == 0:
    x = -b / (2*a)
    print(x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(x1)
    print(x2) # eu te odeio runcodes, eu te odeio.
