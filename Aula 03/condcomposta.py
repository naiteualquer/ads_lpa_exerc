print ("questão a")
ano = int(input("qual o ano: "))

if ano % 4 == 0:
    print("pode ser um ano bissexto")
else:
    print("definitivamente não é um ano bissexto")

print ("questão b")
lado = input("qual o lado: ")

if lado == "cima" or "baixo":
    print ("decida-se")
else:
    print("você escolheu um caminho")