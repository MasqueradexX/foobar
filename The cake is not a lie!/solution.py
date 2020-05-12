def verify(s,samplelen,cut):
    sample = s[:samplelen] 
    # print(sample)
    for n in range(1,cut):
        if sample != s[n*samplelen:(n+1)*samplelen]:
        #   print(sample + '!=' + s[n*samplelen:(n+1)*samplelen])
          return False
    return True

def solution(s):
    # Your code here
    strlen = len(s)
    for samplelen in range(1,strlen+1):
        if strlen%samplelen != 0:
            continue
        cut = strlen/samplelen
        for offset in range(samplelen):
            if offset != 0:
                s = s[offset:]+s[0:offset]
            # sample = s[:samplelen+1]
            if verify(s,samplelen,cut):
                return cut
            
print(solution('abcabcabcabc'))