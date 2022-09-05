if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    
    z = max(l)
    while max(l) == z:
        l.remove(z)
    
    print(max(l))

