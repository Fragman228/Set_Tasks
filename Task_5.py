a = int(input())
f = ''

while True:
    b = int(input())
    h = []
    if b > a:
        print("Error")
        break
    else:
        for i in range(b):
            language = input()
            h.append(language)
    amounth = a - b
    c = int(input(f"Максимальное число ввода {amounth} ученик(а)(ов)\n"))
    h1 = []
    if c + b > a:
        print("Error")
        break
    else:
        for o in range(c):
            language1 = input()
            h1.append(language1)
    amounth = a - b - c
    d = int(input(f"Максимальное число ввода {amounth} ученик(а)(ов)\n"))
    h2 = []
    for o1 in range(d):
        language = input()
        h2.append(language)
    print(h, "\n", h1, '\n', h2)
    for x1 in h:
        for x2 in h1:
            for x3 in h2:
                if x1 == x2 == x3:
                    print(x3)
    break





