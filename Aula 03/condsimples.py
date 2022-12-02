print("questão a")
idade = int(input("qual sua idade: "))

if idade > 60:
    print("você tem direitos aos benefícios")

print("questão b")
dano = int(input("qual o dano: "))
escudo = int(input("qual o escudo: "))

if dano > 10 and escudo == 0:
    print("você está morto")

print("questão c")
direcao = input("qual a direção: ")

if direcao == "norte" or "sul" or "leste" or "oeste":
    print("você escapou, parabéns")

