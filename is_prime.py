import math

def check_prime(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        num = int(input())
        print(check_prime(num))
