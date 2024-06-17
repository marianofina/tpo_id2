import random


def id_generator(cod: str):
    number = random.randint(0, 99999999)
    caracteres = len(str(number))
    restantes = 8 - caracteres
    ceros = '0' * restantes
    return cod + ceros + str(number)
