def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

q, w = map(int, input().split())

if q > w:
    x = range(w, q + 1)
else:
    x = range(q, w + 1)

e = [num for num in x if is_prime(num)]

if w >= q:
    print("main order - amount:", len(e))
else:
    print("reverse order - amount:", len(e))
