'''
구현문제.  처음 call을 어떻게 처리할지 고민했었는데
굳이 call을 2차원 배열로 만들 필요가 없이 그냥 1차원 배열로 만든 뒤 for문을 한번만 돌려주면 되었다.
가로와 세로는 인덱스를 서로 바꿔주는것으로 해결

처음 check를 전역변수로 설정했다가 값이 누적되는것을 간과했음.
그 뒤로 깨닫고 함수 내에서 return 값으로 전달해주는것으로 바꾸었다.

'''

def garosero():
    check = 0
    for i in range(5):
        garo = True
        sero = True
        for j in range(5):
            if bingo[i][j] != False:
                garo = False
            if bingo[j][i] != False:
                sero = False

        if garo:
            check += 1
        if sero:
            check += 1
    return check

def daegak():
    check = 0
    daegak1 = True
    daegak2 = True
    for i in range(5):
        if bingo[i][i] != False:
            daegak1 = False
        if bingo[i][4-i] != False:
            daegak2 = False

    if daegak2:
        check += 1
    if daegak1:
        check += 1
    return check

bingo = [list(map(int, input().split()))for _ in range(5)]
call = []
for _ in range(5):
    call += list(map(int, input().split()))

cnt = 0
# check = 0
flag = True
for i in call:
    if flag:
        for r in range(5):
            for c in range(5):
                if bingo[r][c] == i:
                    bingo[r][c] = False
                    cnt += 1
                    if cnt >= 5:
                        if (garosero()+daegak()) >= 3:
                            print(cnt)
                            flag = False
