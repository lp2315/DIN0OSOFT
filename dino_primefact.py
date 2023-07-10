# BRUTE FORCE ALGORITHM
# TO GENERATE PRIME DIVISORS

#

# GENERATE PRIME NUMBERS UP TO 10^5
primes = [open("D:/primebase.txt", "w")]

print(primes)


def prime_fact(n):
    n_primes = []  # LIST OF PRIME DIVISORS

    if n in primes:
        return print(str(n) + " is a prime number!")


    if n > 1:
        for i in primes:  # ITERATE OVER PRIMES

            while n % i == 0:  # WHILE n IS DIVISIBLE BY NEXT PRIME i
                n_primes.append(i)  # ADD i TO LIST
                n = n / i  # MOVE ON TO NEXT PRIME i

        n_primes.append(int(n))  # IF n IS A POSITIVE INTEGER, ADD TO PRIME LIST
        return n_primes.remove(1), print(n_primes)

    else:
        return print("Integer must be higher than 1!")


#

# USER INPUT

while True:
    x = input("Number?\n")
    try:
        x = int(x)
        prime_fact(x)
    except ValueError:
        print("Number must be an integer!")
