# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
    

def prime_factorization_all(n):
    prime_lit = []
    i = 2 
    while i<=n:
        if n%i ==0:
            prime_lit.append(i)
            n//=i
        else:
            i+=1

    if n > 1:
        prime_lit.append(n)

    return prime_lit
number = int(input('Enter number: '))
print(prime_factorization_all(number))
