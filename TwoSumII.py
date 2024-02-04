def twoSum(numbers, target):
    checked = []
    for i in range(0, len(numbers)):
        if numbers[i] not in checked:
            l = numbers[i]
            for j in range(i, len(numbers)):
                r = numbers[j]
                if r + l == target:
                    return [i+1, j+1]
            checked.append(numbers[i])
        else:
            continue


print(twoSum([2, 7, 11, 15], 9))
