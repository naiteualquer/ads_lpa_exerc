frase = input("digite uma frase: ")
tam = len(frase)

frase2 = frase[:int(tam/2)] #pega somente metade dos strings
frase3 = frase2[-2:] #pega somente os dois últimos caracteres

print (frase2)
print (frase3)
