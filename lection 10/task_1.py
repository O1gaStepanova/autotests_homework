# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    while True:
        yield f"{create_word()} {create_word()}"


def create_word():
    letters = string.ascii_lowercase
    return "".join(random.choices(letters, k=random.randint(1, 16)))


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))