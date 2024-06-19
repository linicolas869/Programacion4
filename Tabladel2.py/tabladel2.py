want_greet ="5"
valid_options=0

while want_greet == "s" :
    print("Hola que tal!")
    want_greet = input ("¿quiere otro saludo?")
    if want_greet not in "sn" : 
        print("No le he entendido pero le saludo igual")
        want_greet="s"
        continue
valid_options += 1
print(f"{valid_options} respuestas validas")
print("que tenga un buen dia")