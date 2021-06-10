count = 0
while count < 2:
    h = input("Введите строку: ")
    subs_set = set()
    for i in range(len(h)):
        for j in range(len(h) - 1 if i == 0 else len(h), i, -1):
            subs_set.add(hash(h[i:j]))
    count += 1
    print(len(subs_set))
