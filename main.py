import math

def fermat_test(n, a):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    return pow(a, n - 1, n) == 1

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


assert is_prime(2)
assert is_prime(3)
assert is_prime(7)
assert is_prime(13)

assert not is_prime(1)
assert not is_prime(4)
assert not is_prime(9)
assert not is_prime(15)


assert fermat_test(45625472856425645485717390, 2) == False
assert fermat_test(1298074214633706835075030044377087, 2) == True
assert fermat_test(359334085968622831041960188598043661065388726959079837, 2) == True

assert fermat_test(561, 2) == True


print("All tests passed!")
