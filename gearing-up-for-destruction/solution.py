def verify(pegs,r0):
    if r0 < 2:
        return False
    rj = r0
    for i in range(1,len(pegs)):
        ri = pegs[i] - pegs[i-1] - rj
        if ri < 1:
            return False
        rj = ri
    return True

def solution(pegs):
    sum1 = pegs[-1]
    sign = 1

    for peg in pegs[-2:0:-1]:
        sign *= -1
        sum1 += sign*2*peg

    if len(pegs)&1:
        #if length is odd
        sum1 += pegs[0]
        a = -2*sum1
        if not verify(pegs,a):
            return [-1,-1]
        else:
            return [a,1]
    else:
        sum1 -= pegs[0]
        a = 2*sum1
        if not verify(pegs,float(a)/3):
            return [-1,-1]
        elif a%3 == 0:
            a /= 3
            return [a,1]
        else:
            return [a,3]
            


print(solution([4,30,50]))