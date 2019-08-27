

    for k in range(0, len(a)-1, 2):
        b[a[k]] = a[k+1]

    for j in range(len(b)):
        for key, value in b.items():
            if not key in b.values():
                c.append(key)
                c.append(value)
        del(b(c[-2]))
