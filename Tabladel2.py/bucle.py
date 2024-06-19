want_greet = "S"
valid_options=0

while want_greet == "S" :
    print("Hola que tal!")
    want_greet = input ("¿quiere otro saludo?")
    if want_greet not in "SN" : 
        print("No le he entendido pero le saludo igual")
        want_greet="S"
        continue
valid_options += 1
print(f"{valid_options} respuestas validas")
print("que tenga un buen dia")