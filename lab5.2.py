import math

Ax = float(input("Введіть координати точки A x:"))
Ay = float(input("Введіть координати точки A y:"))

Bx = float(input("Введіть координати точки B x:"))
By = float(input("Введіть координати точки B y:"))

Cx = float(input("Введіть координати точки C x:"))
Cy = float(input("Введіть координати точки C y:"))

M = (5, -6)

M_A = math.sqrt((M[0] - Ax)**2 + (M[1] - Ay)**2)
M_B = math.sqrt((M[0] - Bx)**2 + (M[1] - By)**2)
M_C = math.sqrt((M[0] - Cx)**2 + (M[1] - Cy)**2)

dist_min = min(M_A, M_B, M_C)

if dist_min == M_A:
    closest_p = "A"
elif dist_min == M_B:
    closest_p = "B"
else:
    closest_p = "C"
print(f"Найближча точка до точки M: {closest_p}")

