# BRUTE FORCE ALGORITHM
# TO GENERATE PRIME DIVISORS

#

# GENERATE PRIME NUMBERS UP TO 10^5
primes = [x for x in range(2, 10000) if all(x % y != 0 for y in range(3, x))]


def prime_fact(n):
    n_primes = []  # LIST OF PRIME DIVISORS

    for i in primes:  # ITERATE OVER PRIMES

        while n % i == 0:  # WHILE n IS DIVISIBLE BY NEXT PRIME i
            n_primes.append(i)  # ADD i TO LIST
            n = n / i  # MOVE ON TO NEXT PRIME i

    if n > 1:
        n_primes.append(int(n))  # IF n IS A POSITIVE INTEGER, ADD TO PRIME LIST

    return print(n_primes)  # PRINT LIST


#

# USER INPUT

x = True

while x:  # REPEAT PROMPT INDEFINITELY
    x = input("Number?\n")
    prime_fact(int(x))
