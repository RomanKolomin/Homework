numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for n in numbers:
    is_prime = True
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)

if 1 in primes:
    primes.remove(1)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
