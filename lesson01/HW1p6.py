while True:
    startAmount = input("Введите количество километров которые пробежал спорстмен в первый день - А (0 для выхода) >>> ")
    try: #try to check incorrect inputs
        startAmount = float(startAmount)
    except ValueError as vr:
        print("вы не выполняете договоренности")
        startAmount = 0
    except Exception as ex:
        print("вы не выполняете договоренности")
        startAmount = 0

    goal = input("Введите количество километров которые спортсмен должен пробежать - B (0 для выхода) >>> ")
    try: #try to check incorrect inputs
        goal = float(goal)
    except ValueError as vr:
        print("вы не выполняете договоренности")
        goal = 0
    except Exception as ex:
        print("вы не выполняете договоренности")
        goal = 0

    days = 1
    currResult = startAmount
    if startAmount > 0 and goal > 0: #task doesn't have any sense in other ways
        while currResult < goal:
            currResult *= 1.1
            days += 1
            print(f"День {days} результат {currResult} км")
        print(f"Спортсмен достигнет результата на {days} день")
    elif goal == 0 or startAmount == 0:
        print("будьте здоровы, приходите еще")
        break
    else:
        print("попробуйте еще раз")
