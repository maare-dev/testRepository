import sympy

num_to_check = 359334085968622831041960188598043661065388726959079837
is_prime_res = sympy.isprime(num_to_check)
print(f"1. num {num_to_check} is prime? -> {is_prime_res}")

base_num = 1000
next_p = sympy.nextprime(base_num)
print(f"2. nearest prime number bigger than {base_num} -> {next_p}")

start, end = 10, 50
primes_in_range = list(sympy.primerange(start, end))
print(f"3. prime nums in range from {start} to {end}: {primes_in_range}")

composite_num = 561
factors = sympy.factorint(composite_num)
print(f"4. prime factorization of {composite_num} (factor: exponent): {factors}")
