pi = 3.141592
raio = float(input())
circunferencia = 2 * pi * raio
area_c = pi * raio ** 2
area_esfera = 4 * pi * raio ** 2
volume_e = 4 / 3 * pi * raio ** 3 
print(f'{circunferencia:.6f}')
print(f'{area_c:.6f}')
print(f'{area_esfera:.6f}')
print(f'{volume_e :6f}')