def floyd_warshall(n, edges, op_plus, e_plus, op_times, e_times):
    res = [[e_plus]*n for i in range(n)]
    parent = [[i]*n for i in range(n)]
    for i in range(0, n):
        res[i][i] = e_times
    for i, j, k in edges:
        res[i][j] = k

    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                tmp = res[y][z]
                res[y][z] = op_plus(op_times(res[y][x], res[x][z]), res[y][z])
                if (tmp != res[y][z]):
                    parent[y][z] = parent[x][z]

    for x in range(0, n):
        for y in range(0, n):
            if (res[x][y] == e_plus):
                parent[x][y] = -1
    return res, parent


def path(D, source, destination):
    res = []

    def path_rec(mat, i, j):
        if(i == j):
            res.append(i)
            return True
        elif (mat[i][j] == -1):
            return False
        else:
            tmp = path_rec(mat, i, mat[i][j])
            res.append(j)
            return tmp
    if not path_rec(D, source, destination):
        return []
    return res
