def solution(x,y):
    x = int(x)
    y = int(y)
    count = 0
    while (x,y) != (1,1):
        if x == 0 or y == 0:
            return 'impossible'
        if x > y:
            step = max([x/y-1,1])
            x -= step*y
            count += step
        else:
            step = max([y/x-1,1])
            y -= step*x
            count += step
    return str(count)

print(solution('4', '7'))