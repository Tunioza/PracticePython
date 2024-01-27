with open("nazwy.txt", 'r') as f:
    grzyb = f.read()

grzyb = grzyb.replace(":", "")
grzyb = grzyb.strip(" ")
grzyb = grzyb.replace(" ", "_")
grzyb = grzyb.split("\n")

print(grzyb)
result = []
for nazwa in grzyb:
    while nazwa.endswith("_"):
        nazwa = nazwa[:-1]
    result.append(nazwa)

for i in range(0, 40):
    with open(f"{result[i]}.py", 'w') as g:
        g.write(f"# {result[i]}")