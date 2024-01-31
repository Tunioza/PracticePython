# 20_Element_Search


def find(ordered_list, element_to_find):
    start_index = 1
    end_index = len(ordered_list) - 1

    while True:
        middle_index = int((end_index - start_index) / 2)

        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False

        middle_element = ordered_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index


def binary_search_recursion(ordered_list, element_to_search, *indeksy):
    if len(indeksy) == 0:
        start_index = 0
        end_index = len(ordered_list) - 1
    elif len(indeksy) == 2:
        start_index = indeksy[0]
        end_index = indeksy[1]
    else:
        return False

    middle_index = (start_index + end_index) // 2

    if middle_index < start_index or middle_index > end_index or middle_index < 0:
        return False

    middle_element = ordered_list[middle_index]

    if middle_element == element_to_search:
        return True
    elif middle_element < element_to_search:
        return binary_search_recursion(ordered_list, element_to_search, middle_index + 1, end_index)
    else:
        return binary_search_recursion(ordered_list, element_to_search, start_index, middle_index - 1)



if __name__ == "__main__":
    l = [2, 4, 6, 8, 10]

    print(binary_search_recursion(l, 6))  # prints False
    print(binary_search_recursion(l, 5))  # prints False
    print(binary_search_recursion(l, 8))  # prints False
    print(binary_search_recursion(l, 1))  # prints False
