import random

print("\n---- Pedra, Papel, Tesoura ----")
options = ["pedra", "papel", "tesoura"]

player = input("Escolha (pedra/papel/tesoura): ").lower()
computer = random.choice(options)

print(f"Você: {player}")
print(f"Computador: {computer}")

if player not in options:
    print("Opção Inválida!")
elif player == computer:
    print("Empate!!!")
elif (player == "pedra" and computer == "tesoura" or
      player == "tesoura" and computer == "papel" or
      player == "papel" and computer == "pedra"):
    print("Você ganhou")
else:
    print("Computador ganhou")