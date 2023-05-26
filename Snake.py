import random


random_x = random.randint(1, 60 - 2)
random_y = random.randint(1, 30 - 2)


def print_cube(szeles, magas):
    for i in range(magas):
        for j in range(szeles):
            if i == 0 or i == magas - 1 or j == 0 or j == szeles - 1:
                print("*", end="")
            elif i == random_y and j == random_x:
                print("@", end="")
            else:
                print(" ", end="")
        print()

szeles = 60
magas = 30
print_cube(szeles, magas)

irany = input("Merre? ")

def print_cube(szeles, magas):
    for i in range(magas):
        for j in range(szeles):
            if i == 0 or i == magas - 1 or j == 0 or j == szeles - 1:
                print("*", end="")
            elif irany == "Fel" and i == random_y-1 and j == random_x:
                print("@", end="")
            elif irany == "Le" and i == random_y+1 and j == random_x:
                print("@", end="")
            elif irany == "Jobbra" and i == random_y and j == random_x +1:
                print("@", end="")
            elif irany == "Balra" and i == random_y and j == random_x -1:
                print("@", end="")
            else:
                print(" ", end="")
        print()

szeles = 60
magas = 30
print_cube(szeles, magas)