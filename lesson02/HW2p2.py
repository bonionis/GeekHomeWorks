# 2

list = list()
user_data = None
while user_data != "":  # input nothing to stop filling
    user_data = input("Введите данные (ничего для остановки) >>> ")
    list.append(user_data)
list = list[:-1]  # removing empty item

print("Original list")
for element in list:
    print(element)

counter = 0
while counter < len(list) - 1:
    list[counter + 1], list[counter] = list[counter], list[counter + 1]
    counter += 2

print("Modified list")
for element in list:
    print(element)