def check_input():
    while True:
        try:
            num = input("Введите число: ")
            if num.isdigit():
                return num
        except Exception:
            print('Это не число')
num1 = check_input()
num2 = check_input()
print(num2,num1)