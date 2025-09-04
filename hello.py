import random

random_int = random.randint(1, 10)

while int(input("Adivinhe meu numero: ")) != random_int:
    print("Errou")

print("Acertou!")
