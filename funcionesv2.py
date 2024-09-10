print("Mas sobre funciones")
#Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s
#LLamadas a funciones
print("Calculando suma")
n1=int(input("Ingrese el primer numero"))
n2=int(input("Ingrese el segundo numero")) 
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es {suma}")

print("")
def resta(c,d):
    r=c-d
    return r
print("Calculando resta")
n3=int(input("Ingrese el primer numero"))
n4=int(input("Ingrese el segundo numero")) 
res=resta(n3,n4)
print(f"La resta de {n3} - {n4} es {res}")

print("")
def mul(e,f):
    m=e*f
    return m
print("Calculando multiplicacion")
n5=int(input("Ingrese el primer numero"))
n6=int(input("Ingrese el segundo numero")) 
mult=mul(n5,n6)
print(f"La multiplicacion de {n5} x {n6} es {mult}")

print("")
def div(g,h):
    d=g/h
    return d
print("Calculando division")
n7=int(input("Ingrese el primer numero"))
n8=int(input("Ingrese el segundo numero")) 
divi=div(n7,n8)
print(f"La division de {n7} / {n8} es {divi}")
