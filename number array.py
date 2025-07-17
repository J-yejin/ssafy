T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split(' '))

    ls_a = list(map(int, input().split(' ')))
    ls_b = list(map(int, input().split(' ')))

    if a > b:
        M = a
        m = b
        ls_M = ls_a.copy()
        ls_m = ls_b.copy()
    else:
        M = b
        m = a
        ls_M = ls_b.copy()
        ls_m = ls_a.copy()

    case = M - m + 1
    ls_rs = list()
    for i in range(0, case):
        rs = 0
        for j in range(0, m):
            rs += ls_M[j+i]*ls_m[j]
        ls_rs.append(rs)

    print('#{number}'.format(number=test_case), end=' ')
    print(max(ls_rs))