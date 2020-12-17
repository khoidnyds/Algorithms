def RecursiveGCD(a, b):
    """
    GCD(a,b)=GCD(b,r) which a=bq+r (Euclidean Algorithm)
    """
    if b:
        return RecursiveGCD(b, a % b)
    else:
        return a

# lcm(a, b) × gcd(a, b) = ab


a, b = 28851538, 1183019
assert RecursiveGCD(a, b) == 17657
