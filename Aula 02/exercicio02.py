km = int(input("quantos km rodados: "))
dias = int(input("dias de aluguel: "))

diaria = 60 * dias
custokm = 0.15 * km


print("você percorreu {} km com {} diárias" .format(km,dias))
print('você deve pagar {} pela diária e {} pelos km rodados, totalizando {}' .format(diaria, custokm, (diaria+custokm)))