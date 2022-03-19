def init_mat(n, edges, op_plus, e_plus, op_times, e_times):
  M = [[e_plus for _ in range(n)] for _ in range(n)]
  for i in range(n):
    M[i][i] = e_times
  for (a,b,w) in edges:
    M[a][b] = w
  return M


def floyd_warshall(n, edges, op_plus, e_plus, op_times, e_times):
  # Generalised Floyd-Warshall algorithm

  M_last = init_mat(n, edges, op_plus, e_plus, op_times, e_times)

  # Floyd-Warshall triple loop
  for k in range(n):
    M_current = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
      for j in range(n):
        M_current[i][j] = op_plus(M_last[i][j], op_times(M_last[i][k], M_last[k][j]))
    M_last = M_current
