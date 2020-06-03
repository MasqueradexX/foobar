from itertools import permutations

def solution(times, times_limit):
    v = len(times)
    dist = list(times)

    # Floyd Warshall
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] +dist[k][j]
    
    # check for negative cycles
    for i in range(v):
        if dist[i][i] < 0:
            return range(v-2)
    
    #enumerate all paths        
    for path_len in range(v-2, 0, -1):
        for path in permutations(range(1,v-1), path_len):
            cost = 0
            for i in range(1,len(path)):
                cost += dist[path[i-1]][path[i]]
            cost += dist[0][path[0]] + dist[path[-1]][v-1]
            
            if cost <= times_limit:
                return [id - 1 for id in sorted(path)]
  
    return []

print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))