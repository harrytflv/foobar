all_primes, num = "", 1

while len(all_primes) < 10005:
    num += 1
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        all_primes += str(num)

print(all_primes)
