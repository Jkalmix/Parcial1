#Cree un algoritmo que lea 5 números enteros uno por uno 
# e identifique cuáles son positivos y pares. 
# Al final, debe mostrar la suma total de esos números.


# ingresar los 5 nùmero y convertirlos ene entero

primer_entero = input("Por favor, ingresa el primer número entero: ")
a = int(primer_entero) 
seg_entero = input("Por favor, ingresa el segundo número entero: ")
b = int(seg_entero) 
ter_entero = input("Por favor, ingresa el tercero número entero: ")
c = int(ter_entero) 
cuar_entero = input("Por favor, ingresa el cuarto número entero: ")
d = int(cuar_entero) 
qui_entero = input("Por favor, ingresa el quinto número entero: ")
e = int(qui_entero)


#Creo una variable para la suma de positivos
suma_positivos = 0
#creo condicuiones para identificar si el numero es positivo o negativo y si es par o impar y si es positivo y par voy sumando
if a >= 0:
        print( f"{a} es un numero positivo")
else: print( f"{a} es un numero negativo")

if a % 2 == 0:
        print( f"{a} es par")
else: print( f"{a} es impar")

if a > 0 and a % 2 == 0:   
            suma_positivos += a

if b >= 0:
        print( f"{b} es un numero positivo")
else: print( f"{b} es un numero negativo")
if b % 2 == 0:
        print( f"{b} es par")
else: print( f"{b} es impar")
if b > 0 and b % 2 == 0:   
            suma_positivos += b


if c >= 0:
        print( f"{c} es un numero positivo")
else: print( f"{c} es un numero negativo")
if c % 2 == 0:
        print( f"{c} es par")
else: print( f"{c} es impar")
if c > 0 and c % 2 == 0:   
            suma_positivos += c

if d >= 0:
        print( f"{d} es un numero positivo")
else: print( f"{d} es un numero negativo")
if d % 2 == 0:
        print( f"{d} es par")

if d > 0 and d % 2 == 0:   
            suma_positivos += d

else: print( f"{d} es impar")
if e >= 0:
        print( f"{e} es un numero positivoa")
else: print( f"{e} es un numero negativo")
if e % 2 == 0:
        print( f"{e} es par")
else: print( f"{e} es impar")
if e > 0 and e % 2 == 0:  
            suma_positivos += e
#imprimo la suma de los positivos
print(f"la Sùma de los pares positivos es {suma_positivos}")  
#variable para la suma total de los 5 numeros
sum_total= a + b + c + d + e
#imprimo las uma total de los 5 numeros
print(f"la Sùma total es {sum_total}")

print("----------------------------------")
print("")
print("----------------------------------")

#Diseñe un programa que lea la edad de una persona y muestre un mensaje según el siguiente criterio:
# •Menor de 13 años → “Niño”
# Entre 13 y 17 años → “Adolescente”
# •	Entre 18 y 59 años → “Adulto”
# •	60 años o más → “Adulto mayor”
# Restricción: El programa debe validar que la edad sea un número entero positivo. En caso contrario, debe mostrar un mensaje de error.
# ingresar la edad y convertirla en entero
edad = input("Por favor, ingresa su edad: ")
a = int(edad)
#validar que la edad sea un numero entero positivo
if a > 0:
    #valirdar las condiciones de la edad
    if a < 13 : print("Niño")
    if 13 <= a <= 17 : print("Adolecente")
    if 18<= a <= 59 : print("Adulto")
    if 60 <= a : print("Adulto Mayor")
else: print ("No puede ser un numero negativo negativo.")

print("----------------------------------")
print("")
print("----------------------------------")

#Solicite al usuario que escriba una palabra (sin espacios) y
# cuente cuántas vocales tiene. 
# El programa debe ser sensible a mayúsculas y minúsculas (es decir, contar tanto a como A).
#Nota: No use listas. Utilice un contador por cada vocal.

# ingresar la palabra y convertirla en minuscula
palabra = input("Por favor, escribe una palabra (sin espacios): ")

a = 0
e = 0
i = 0
o = 0
u = 0
#contar las vocales y hacer que sea indistinto si es mayuscula o minuscula
for letra in palabra:
    if letra == 'a' or letra == 'A':
        a += 1
    elif letra == 'e' or letra == 'E':
        e += 1
    elif letra == 'i' or letra == 'I':
        i += 1
    elif letra == 'o' or letra == 'O':
        o += 1
    elif letra == 'u' or letra == 'U':
        u += 1

total_vocales = a + e + i + o + u 
print(f"La palabra '{palabra}' tiene:")

print(f"  {a} vocal(es) 'a'")
print(f"  {e} vocal(es) 'e'")
print(f"  {i} vocal(es) 'i'")
print(f"  {o} vocal(es) 'o'")
print(f"  {u} vocal(es) 'u'")
print(f"En total, tiene {total_vocales} vocales.")

print("----------------------------------")
print("")
print("----------------------------------")