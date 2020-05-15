def solution(l):
    n = len(l)
    divisors = [[] for _ in l]
    for i in range(n):
        for j in range(i+1,n):
            if (l[j]%l[i] == 0):
                divisors[j].append(i)
    
    sum1 = 0
    for num in divisors:
        for i in num:
            sum1 += len(divisors[i])
    
    return sum1

print(solution([1,2,3,4,5,6]))