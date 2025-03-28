escada = []

while len(escada) < 10:
    escada.append(len(escada) + 1)
    print(" ".join(map(str, escada)))
