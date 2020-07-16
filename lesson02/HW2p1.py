# 1
test_list = list()
test_list.append(None)
test_list.append(1)
test_list.append(1.1)
test_list.append("test")
test_list.append([1, 2, 3, 4])
test_list.append(bytes("test string", "UTF-8"))
test_list.append((1, 2, 3, 4, 2, 3, 1, 4, 3))
test_list.append(set(test_list[6]))
test_list.append({"name": "Ivan", "lastname": "Ivanov"})
test_list.append(True)
test_list.append(bytearray(test_list[5]))
counter = 0
for varr in test_list:
    print(type(varr), varr)
