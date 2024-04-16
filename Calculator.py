def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def sqrt(x):
    return x**0.5


# Main Program
print("Выберите действие.")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Квадратный корень")


while True:
    operation = input("Enter Choice (1/2/3/4/5): ")

    if operation in ('1', '2', '3', '4', '5'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if operation == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif operation == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif operation == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        elif operation == '5':
            print("Квадратный корень из", num1, "=", sqrt(num1))
            print("Квадратный корень из", num2, "=", sqrt(num2))


