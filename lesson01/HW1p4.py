while True:
    source = input("Введите целое положительное число (0 для выхода) >>> ")
    try:  # try to check incorrect inputs
        source = int(source)
    except ValueError as vr:
        print("вы не выполняете договоренности")
        source = 0
    except Exception as ex:
        print("вы не выполняете договоренности")
        source = 0
    if source > 0:  # task doesn't describe another behavior
        power = 1
        maxNumber = 0
        while source >= 1:
            temp = source % 10 ** power
            candidate = temp / 10 ** (power - 1)
            if candidate > maxNumber:
                maxNumber = candidate
            power += 1
            source = source - temp
        print(f"Максимальная цифра в числе {int(maxNumber)}")
    elif source <= 0:
        print("Число не удовлетворяет условиям, будьте здоровы, приходите еще")
        break
    else:
        print("попробуйте еще раз")
