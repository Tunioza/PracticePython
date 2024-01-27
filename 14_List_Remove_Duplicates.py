# 14_List_Remove_Duplicates

a = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]


def unique(lista):
    result = []
    for number in lista:
        if number not in result:
            result.append(number)
        else:
            continue
    return result


print(unique(a))
