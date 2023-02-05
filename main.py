import random

print("Bine ai venit la Guessing Game!")

print("Ma gandesc la un numar intre 1 si 100")
numar = int(random.randint(1, 100))


def play(mod):
    if mod == "greu":
        vieti = 5
    else:
        vieti = 10
    alegere = int(input(f"Ai {vieti} incercari sa ghicesti numarul."))
    if alegere > numar:
        print("Prea mare.")
        vieti -= 1
    elif alegere < numar:
        print("Prea mic.")
        vieti -= 1
    else:
        return print("Ai ghicit.")
    while vieti > 0:
        alegere = int(input(f"Mai ai {vieti} incercari sa ghicesti numarul."))
        if alegere > numar:
            print("Prea mare.")
            vieti -= 1
        elif alegere < numar:
            print("Prea mic.")
            vieti -= 1
        else:
            return print("Ai ghicit.")
    return print("Ai pierdut.")

dif = input("Alege o dificultate. Scrie 'usor' sau 'greu'").lower()
play(dif)
