def square_generator(n):
    # Yield squares from 0 to n
    for i in range(n + 1):
        yield i * i


def even_numbers_generator(n):
    # Yield even numbers from 0 to n
    for i in range(0, n + 1, 2):
        yield i


def divisible_by_3_and_4(n):
    # Yield numbers divisible by both 3 and 4 (i.e., by 12)
    for i in range(n + 1):
        if i % 12 == 0:
            yield i


def squares(a, b):
    # Yield squares from a to b
    for i in range(a, b + 1):
        yield i * i


def countdown(n):
    # Yield numbers from n down to 0
    for i in range(n, -1, -1):
        yield i


if __name__ == "__main__":
    n = int(input("Enter n: "))

    print("1) Squares up to n:")
    print(list(square_generator(n)))

    print("2) Even numbers (comma-separated):")
    print(",".join(str(x) for x in even_numbers_generator(n)))

    print("3) Numbers divisible by 3 and 4:")
    print(list(divisible_by_3_and_4(n)))

    a = int(input("Enter a for squares(a, b): "))
    b = int(input("Enter b for squares(a, b): "))
    print("4) squares(a, b):")
    print(list(squares(a, b)))

    print("5) Countdown from n to 0:")
    print(list(countdown(n)))