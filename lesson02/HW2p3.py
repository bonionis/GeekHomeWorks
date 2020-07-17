# 3

month_list = list() #getting initial data
month_list.append("")
month_list.append("Зима")
month_list.append("Зима")
month_list.append("Весна")
month_list.append("Весна")
month_list.append("Весна")
month_list.append("Лето")
month_list.append("Лето")
month_list.append("Лето")
month_list.append("Осень")
month_list.append("Осень")
month_list.append("Осень")
month_list.append("Зима")

month_tuple = tuple(month_list) #creating tuple for fun

month_dict = dict(list(enumerate(month_list))) #creating dictionary

while True:
    month_num = input("Введите номер месяца от 1 до 12 (или любой символ для выхода) >>> ")
    try: #try to check incorrect inputs
        month_num = int(month_num)
    except ValueError as vr:
        month_num = 0
    except Exception as ex:
        month_num = 0

    if month_num >= 1 and month_num <=12:
        print("Сезон из списка: ", month_list[month_num])
        print("Сезон из картежа: ", month_tuple[month_num])
        print("Сезон из словаря: ", month_dict.get(month_num))
    else:
        print("приходите еще")
        exit()

#test comment