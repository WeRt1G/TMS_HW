def infinite_cycle(numbers):
    while True:
        for number in numbers:
            yield number

def main():
    try:
        count = int(input("Введите количество чисел для вывода: "))
        if count <= 0:
            print("Введите положительное число.")
            return
    except ValueError:
        print("Введите целое число.")
        return

    numbers_input = input("Введите числа через пробел: ")
    numbers = numbers_input.split()

    generator = infinite_cycle(numbers)

    for _ in range(count):
        print(next(generator), end=" ")


main()

