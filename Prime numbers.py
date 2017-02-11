def prime(n):
    i = 2
    while i < n :
        if n % i == 0:
            return False
        i += 1
    return True

i = 2
while i <= 100 :
    if prime(i):
        print(i, "is a Prime Number")
    i= i+1

print("end")
