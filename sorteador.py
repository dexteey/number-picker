import random
import time

print("==SORTEIO DE NÚMEROS==\n")
print("""Neste software, você irá escolher
um número mínimo para X e um número 
máximo para Y. Além disso, você também 
pode escolher um número Z para a 
quantidade de números a serem sortidos.\n""")

contador = 0

while(True):
    try:
        x = int(input("Digite um número mínimo para X: "))
        y = int(input("Digite um número máximo para Y: "))
        z = int(input("Escolha a quantidade Z de números que irão ser sorteados: "))
        if(z > 0 and x > 0 and x < y):
            break
        else:
            print("\nOrdem errada! Lembrando que valor mínimo deve\nser maior do que zero e menor que o valor máximo\nenquanto a quantidade deve ser maior que 0.\n")
    except ValueError:
        print("\nDados inválidos! Tente novamente com números inteiros.\n")

while(True):
    print("\nSorteando...\n")
    time.sleep(1)
    while(contador!=z):
        print(random.randint(x, y))
        contador = contador+1
    print("\nSorteio Concluído!")
    contador = 0
    repetir = 0
    while(repetir == 0):
        try:
            repetir = int(input("\nDeseja repetir com os mesmos números? Digite 1 para SIM ou 2 para NÃO: "))
        except ValueError:
            print("\nDigite somente 1 ou 2!")
    if(repetir!=1):
        print("\nObrigado por utilizar meu software! :D")
        break