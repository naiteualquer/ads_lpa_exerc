#tipo de triângulo

ladoa = int(input('digite lado a: '))
ladob = int(input('digite lado b: '))
ladoc = int(input('digite lado c: '))

if (ladoa and ladob and ladoc) > 0:
    if ladob <= ladoc and ladoc <= ladob and ladoc <= ladoa:
        print("hello")

    else:
            print("um lado não pode ser maior que a soma dos outros dois lados")
else:
    print('lada não pode ser zero')
