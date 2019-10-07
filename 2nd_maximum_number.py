if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    l_arr = list(arr)
    max_score = max(l_arr)
    
    while max(l_arr) == max_score:
        l_arr.remove(max_score)
    
    print(max(l_arr))


    
