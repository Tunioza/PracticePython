ludzie = [("Jan","Kowalski"), ("Grzegorz", "Brzęczyszczykiewicz"),("Jacek", "Placek")]

print(ludzie)

def get_second_element(pair):
    return pair[1]

sorted_people_def = sorted(ludzie, key=get_second_element)
print("Posortowane za pomocą funkcji zdefiniowanej przez def:")
print(sorted_people_def)

# Sortowanie za pomocą wyrażenia lambda
sorted_people_lambda = sorted(ludzie, key=lambda x: x[1])
print("\nPosortowane za pomocą wyrażenia lambda:")
print(sorted_people_lambda)