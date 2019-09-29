def prime(n):
    if n==2:
        return True
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True    
    for j in range(1,20):
    print(j,"is prime")