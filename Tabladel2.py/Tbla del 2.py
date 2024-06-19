a=2
b=1
while b<11:
    c = a*b 
    print(f"{b}*{a}={c}")
    b+=1

a=1
while a!=0 :
    a=int(input("Dame el valor y te devuelvo la tabla de multiplicar"))
    for i in range(1,11):
        print(f"{i}X{a}=")
        print(i*a)
print ("programa finalizado")


a=1
while a!=0 :
    a=int(input("Dame el valor y te devuelvo la tabla de multiplicar"))
    if a == 0: 
        break 
    else: 
        for i in range(1,11):
            print(f"{i}X{a}=")
            print(i*a)
print ("programa finalizado")


a=2
b=1
while b<11:
    c = a*b 
    print(f"{b}*{a}={c}")
    b+=1