import random
szamok = []
darab = int(input("Add meg hogy mennyi elem van egy kártyán: "))

for i in range(darab):
    veletlen = random.randint(1,100)
    szamok.append(veletlen)
    print(veletlen, end=" ")
print("\n")

for j in range(darab-1):
    veletlen2 = random.randint(1,100)
    print(veletlen2, end=" ")
közös = random.choice(szamok)
print(közös)

print(f"A két pakli közös eleme: {közös}")