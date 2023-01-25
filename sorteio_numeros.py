import random
import time
print("\n             SORTEIO DA MARIUCHA\n\n")


max = input("Digite o número máximo de valores para o sorteio.\nEx.: um sorteio entre 10 pessoas, o número máximo é '10'\n\n\nValor: ")

time.sleep(2)

print("\n\n          O número ganhador é...\n")

time.sleep(1)

print("___________________________________________\n")
print("                 Sorteando...")
print("___________________________________________")

time.sleep(3)
num = random.randint(1, int(max))
print("\n" + str(num))
