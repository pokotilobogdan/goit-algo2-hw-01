import random
from colorama import Fore


# ФУНКЦІЇ ДЛЯ ГАРНОГО ВИВОДУ ТЕКСТУ
def yellow(elem):
    if isinstance(elem, str) is False:
        elem = str(elem)
    return Fore.YELLOW + elem + Fore.RESET

def blue(elem):
    if isinstance(elem, str) is False:
        elem = str(elem)
    return Fore.BLUE + elem + Fore.RESET

def red(elem):
    if isinstance(elem, str) is False:
        elem = str(elem)
    return Fore.RED + elem + Fore.RESET

def green(elem):
    if isinstance(elem, str) is False:
        elem = str(elem)
    return Fore.GREEN + elem + Fore.RESET

def highlighted_print(arr: list, k):
    '''
    Пишемо k-й елемент списку іншим кольором.
    Функція для перевірки правильності виконання завдання
    '''

    if k == 1 and len(arr) == 1:
        print("[" + green(arr[0]) + "]")
    elif k == 1 and len(arr) > 1:
        print("[" + green(arr[0]) + ", " + str(arr[1:])[1:])       # приписуємо праворуч ', 7, 8, 9]'
    elif k == len(arr):
        print(str(arr[:-1])[:-1] + ", " + green(arr[-1]) + "]")    # приписуємо ліворуч '[1, 2, 3, ' і праворуч ']'
    else:
        str_left = str(arr[:k-1])[:-1] + ", "     # приписуємо ліворуч '[1, 2, 3, '
        str_right = ", " + str(arr[k:])[1:]          # приписуємо праворуч ', 7, 8, 9]'
        print(str_left + green(arr[k-1]) + str_right)


# ОСНОВНІ ФУНКЦІЇ
def create_arr():
    arr = []
    for _ in range(random.randint(1, 15)):
        arr.append(round(random.uniform(-20, 20), 2))
    return arr

def pivot_func(arr: list):
    # опорний елемент може бути будь-яким, тому для зручності це буде перший елемент списку
    # зробимо його списком, в разі якщо є числа, що рівні pivot
    pivot = [arr[0]]

    # списки чисел, що менші та більші за pivot відповідно
    left_arr = []
    right_arr = []

    for num in arr[1:]:
        if num < pivot[0]:
            left_arr.append(num)
        elif num > pivot[0]:
            right_arr.append(num)
        else:
            pivot.append(num)

    return left_arr, pivot, right_arr


def my_func(arr: list, k: int):
    '''
    Повертає k-й найменший елемент списку
    '''
    if k < 1:
        print(red("k should be a natural number"))
        return None
    if k > len(arr):
        print(red("k should be less or equal of the list size"))
        return None
    
    left_arr, pivot, right_arr = pivot_func(arr)

    if k <= len(left_arr):
        result = my_func(left_arr, k)
    elif k > len(left_arr) + len(pivot):
        result = my_func(right_arr, k - len(left_arr) - len(pivot))
    else:
        result = pivot[0]

    return result


if __name__ == "__main__":

    arr = create_arr()
    k = random.randint(1, len(arr))

    print()
    print("Список:", blue(arr))
    print("Знайти " + blue(k) + "-й найменший елемент")
    print(green(my_func(arr, k)))

    print()
    print(yellow("Перевіримо з відсортованим списком:"))
    highlighted_print(sorted(arr), k)
    print()
