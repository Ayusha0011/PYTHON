def is_prime(num):
    if num <= 1:
        print(f"{num} is not prime")
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is divisible by {i}, so it's not prime.")
            return False
    print(f"{num} is prime!")
    return True
is_prime(11)