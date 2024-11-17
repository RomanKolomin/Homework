def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        is_prime = True
        for div in range(2, result // 2 + 1):
            if result % div == 0:
                is_prime = False
                break
        if is_prime:
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
