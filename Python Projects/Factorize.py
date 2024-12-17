def Factorize(n):
    prime = []  # List to store prime factors
    divisor = 2  # The smallest prime number

    while n > 1:
        while n % divisor == 0:  # While n is divisible by divisor
            prime.append(divisor)  # Add divisor to the list of prime factors
            n = n / divisor  # Divide n by divisor
        divisor += 1  # Move to the next number

    print(prime) # Show the list of prime factors

n = int(input("Enter a number: "))
Factorize(n)
