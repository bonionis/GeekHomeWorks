while True:
    secAmount = input("Введите количество секунд от 1 до 9 (0 для выхода) >>> ")
    try: #try to check incorrect inputs
        secAmount = int(secAmount)
    except ValueError as vr:
        print("вы не выполняете договоренности")
        secAmount = 0
    except Exception as ex:
        print("вы не выполняете договоренности")
        secAmount = 0
    if secAmount > 0 and secAmount < 10: #task doesn't describe another behavior
        # counter = secAmount
        # while secAmount > 0:
        #     print(secAmount)
        #     secAmount -= 1
        # i think it's a simplist way to get a result
        result = secAmount * 100 + secAmount * 10 + secAmount + secAmount * 10 + secAmount + secAmount
        print(f"{secAmount * 100 + secAmount * 10 + secAmount}+{secAmount * 10 + secAmount}+{secAmount} = {result}")
    elif secAmount == 0:
        print("будьте здоровы, приходите еще")
        break
    else:
        print("попробуйте еще раз")
