def isWall(map,v):
    if map[v[0]][v[1]] == 1:
        return True
    else:
        return False

def solution(map):
    h = len(map)
    w = len(map[0])
    dist1 = [[float('inf')]*w for _ in range(h)]
    dist2 = [[float('inf')]*w for _ in range(h)]
    visited1 = set()
    visited2 = set()
    queue1 = []
    queue2 = []
    walls = set()

    queue1.append((0,0))
    visited1.add((0,0))
    dist1[0][0] = 1
    while queue1:
        current = queue1.pop(0)
        x,y = current
        currentdist = dist1[current[0]][current[1]]
        for neighbour in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if neighbour[0] >= h or neighbour[0] < 0 or neighbour[1] >= w or neighbour[1] < 0:
                continue
            if neighbour not in visited1:
                if isWall(map,neighbour):
                    walls.add(neighbour)
                else:
                    queue1.append(neighbour)
                visited1.add(neighbour)
                dist1[neighbour[0]][neighbour[1]] = currentdist + 1

    queue2.append((h-1,w-1))
    visited2.add((h-1,w-1))
    dist2[h-1][w-1] = 1
    while queue2:
        current = queue2.pop(0)
        x,y = current
        currentdist = dist2[current[0]][current[1]]
        for neighbour in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if neighbour[0] >= h or neighbour[0] < 0 or neighbour[1] >= w or neighbour[1] < 0:
                continue
            if neighbour not in visited2:
                if isWall(map,neighbour):
                    walls.add(neighbour)
                else:
                    queue2.append(neighbour)
                visited2.add(neighbour)
                dist2[neighbour[0]][neighbour[1]] = currentdist + 1
    
    walldist = [dist1[x][y]+dist2[x][y]-1 for x,y in walls]
    walldist.append(dist1[h-1][w-1])
    return min(walldist)

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
