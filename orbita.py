pi=3.1416
G=6.67e-11
M=5.9736e24
R=6.378e0
T=float(input("ingrese en valor del periodo T: "))
h=(((G*M)*((T/2*pi)**2))**1/3)-R
print(h)
