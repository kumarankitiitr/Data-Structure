    n,d = map(int, input().split())
    arr = list(map(int, input().split()))
    # Reverse array from beginning till d
    # Reverse array from d till n
    
    l = arr[(d%n):] + arr[:(d%n)]
    for i in l:
        print(i , end = ' ')
    print()
