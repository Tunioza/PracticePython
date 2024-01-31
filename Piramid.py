def build_piramid(height):
    for i in range(1, height + 1):
        for j in range(0, (height-i)):
            print(" ", end="")
        for x in range(0, (2*i-1)):
            print("*", end="")
        for y in range(0, (height-i)):
            print(" ", end="")
        print()

build_piramid(100)
