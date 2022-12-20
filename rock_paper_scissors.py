import random

user_points = 0
computer_points = 0

while True:
    user_choice = input ("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()

    if user_choice == 'q':
        break

    computer_choice = random.randint(0, 2)
    # 0 : R, 1 : T, 2 : P

print ("Goodbye!")