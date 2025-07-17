T = int(input())
 
for test_case in range(1,T+1):
    print('#{number}'.format(number = test_case))
    num = int(input())
    mat =[]
    for _ in range(num):
        row = list(map(int, input().split(' ')))
        mat.append(row)
 
    for n in range(num - 1, -1, -1):
        for i in range(num-1, -1, -1):
            print(mat[i][num - n-1], end='')
        print(' ', end='')
        for i in range(num-1, -1, -1):
            print(mat[n][i], end='')
        print(' ', end='')
        for i in range(0, num):
            print(mat[i][n], end='')
        print('')