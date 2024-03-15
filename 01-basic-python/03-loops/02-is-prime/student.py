# Write your code here
def is_prime(n):
    if n == 1 or n == 0:
        return False
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True