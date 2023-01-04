import random
def instrucciones():
    print("""
        Adivina el numero!!
    1 - Se genera un numero de 3 cifras aleatorio
    2 - Los 3 digitos son diferentes, es decir se generara ningun numero como: 111, 224, 232,etc.
    3 - Debes ingresar un numero de 3 cifras, y te mostrara numeros clave
    4 - Si tienes numeros correctos en la posicion correcta te dira la cantidad de correctos
    5 - Si tienes numeros correctos pero en la posicion incorrecta te lo mostrara como cantidad de bases
    """)
def correctos(numero,a,b,c):
    A = numero//100
    B = (numero - (A * (100))-(numero%10))/10
    C = numero%10
    correctos = 0
    if(a == A):
        correctos +=1
    if(B == b):
        correctos+=1
    if(C == c):
        correctos +=1
    return correctos
def base(numero,a,b,c):
    A = numero//100
    B = (numero - (A * (100))-(numero%10))/10
    C = numero%10
    base = 0
    if(a==B):
        base +=1
    if(a==C):
        base +=1
    if(b == A):
        base +=1
    if(b ==C):
        base +=1
    if(c==A):
        base +=1
    if(c==B):
        base +=1
    return base
def main():
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)
    while(a == b):
        b = random.randint(1,9)
    while(a == c or b == c):
        c = random.randint(1,9)
    numero = (a*100) + (b * 10) + c
    opcion = int(input("Ingrese un numero (de 3 cifras)-> "))
    intentos = 0
    correcto = 0
    bases = 0
    while(opcion != numero or intentos ==10):
        while(len(str(opcion))!= 3):
            opcion = int(input("El numero debe tener 3 cifras. intentalo de nuevo-> "))
        correcto = correctos(opcion,a,b,c)
        bases = base(opcion,a,b,c)
        intentos+=1
        print(f"Intento {intentos}. tienes correctos {correcto} y base {bases}")
        opcion = int(input("Ingrese un numero (de 3 cifras)-> "))
    if opcion == numero:
        print(f"Has encontrado el numero. Bien hecho!. El numero es {numero}")
    else:
        print(f"Se te acabaron los intentos, el numero era {numero}") 
if __name__ == '__main__':
    main()
    