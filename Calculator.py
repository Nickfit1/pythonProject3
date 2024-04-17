def add(x, y):
    return float(x) + float(y)


def sub(x, y):
    return float(x) - float(y)


def mul(x, y):
    return float(x) * float(y)


def div(x, y):
    return float(x) / float(y)


def sqrt(x):
    return float(x)**0.5


# Main Program
print("Выберите действие.")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Квадратный корень")

def check_input():
    while True:
        try:
            num = input("Введите число: ")
            if num.isdigit():
                return num
        except ValueError:
            print('Это не число')
while True:
    operation = input("Enter Choice (1/2/3/4/5): ")

    if operation in ('1', '2', '3', '4', '5'):
        num1 = check_input()
        num2 = check_input()

    if operation == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif operation == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

    elif operation == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

    elif operation == '4':
        try:
            print(num1, "/", num2, "=", div(num1, num2))
        except ZeroDivisionError:
                print("Ошибка: На ноль делить нельзя!")
    elif operation == '5':
        print("Квадратный корень из", num1, "=", sqrt(num1))
        print("Квадратный корень из", num2, "=", sqrt(num2))


