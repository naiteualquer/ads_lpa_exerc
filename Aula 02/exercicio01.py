preco = float(input("digite o preço do produto: "))
p = float(input("digite o percentual de desconto: "))

desconto = preco * (p / 100)
final = preco - desconto

print ("o preço do produto é {}. Desconto de {}%." .format(preco,p))
print ("o valor calculaado do desconto: {}. Valor final do produto: {}" .format(desconto, final))