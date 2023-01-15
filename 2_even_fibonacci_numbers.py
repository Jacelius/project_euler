
def fibUntil(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
listOfFib = list(fibUntil(4000000))
print(sum(filter(lambda x: x % 2 == 0, listOfFib)))
