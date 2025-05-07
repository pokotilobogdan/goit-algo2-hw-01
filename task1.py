import random
import sys
import os
from colorama import Fore


# ФУНКЦІЇ ДЛЯ ГАРНОГО ВИВОДУ ТЕКСТУ
def yellow(string: str):
    return Fore.YELLOW + string + Fore.RESET

def red(string: str):
    return Fore.RED + string + Fore.RESET


# ОСНОВНІ ФУНКЦІЇ
def find_min_and_max(arr: list):
    # Базові випадки
    if len(arr) == 0:
        return None, None
    if len(arr) == 1:
        return arr[0], arr[0]
    
    # Ділимо список на дві частини
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Порівнюємо min та max цих частин. Відповідні результати йдуть у відповідь
    min_left, max_left = find_min_and_max(left_arr)
    min_right, max_right = find_min_and_max(right_arr)

    result_min = min(min_left, min_right)
    result_max = max(max_left, max_right)

    return result_min, result_max


# Згенеруємо список, на якому і протестуємо функцію
def create_arr():
    arr = []
    for _ in range(random.randint(1, 15)):
        arr.append(round(random.uniform(-20, 20), 2))
    return arr
    
if __name__ == "__main__":

    while True:
        # Очищаємо термінал
        os.system('cls' if os.name == 'nt' else 'clear')

        arr = create_arr()
        print()
        print(yellow("Список:"), arr)
        
        min_num, max_num = find_min_and_max(arr)
        print(yellow("min:"), min_num, yellow("max:"), max_num)
        print()

        answer = input("generate a new one? y/n\n")

        if answer.lower() in ['y', 'yes']:
            continue
        elif answer.lower() in ['n', 'no']:
            sys.exit()
        else:
            print(red("You should type y or n"))
