import math
x = float(input("Введіть значення х:"))

y = 0.0
if x > 7:
    y = (2.27 * math.exp(4 * x + 1) + 3)
elif x > 0.5:
    y = 0.64 * math.pow(x, x + 0.1)
else:
    y = math.log(math.fabs(x - math.exp(x)))
print("y=", y)

