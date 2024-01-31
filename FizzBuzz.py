def FizzBuzz(l):
    fb = []
    for i in range(1, l):
        if i % 3 == 0 and i % 5 == 0:
            fb.append("FizzBuzz")
        elif i % 3 == 0:
            fb.append("Fizz")
        elif i % 5 == 0:
            fb.append("Buzz")
        else:
            fb.append(i)
    return fb

print(FizzBuzz(40))