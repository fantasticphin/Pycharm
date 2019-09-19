def power1(k):
    i = 0;
    power = 1
    while i < k:
        power *= 2
        i += 1
    return power

def power2(k):
    if k == 0:
        return 1
    else:
        return 2 * power2(k-1)

n = 10
print(power1(n))
print(power2(n))


