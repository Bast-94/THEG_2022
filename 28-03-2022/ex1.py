def scc(n, edges):
    # Convert to adjacency list
    succ = [[] for _ in range(n)]
    for (s,d) in edges:
        succ[s].append(d)
    # Dijkstra-based SCC enumeration, using a live stack as in Tarjan
    # 
    # Since only a single pass of the automaton is necessary, we will destroy
    # the adjacency list as the DFS processes the edges, this way we only need to
    # keep a stack of states.
    inscc = [None] * n  # the number of the SCC containing each state

    scc.n = 0 # the number of SCCs discovered so far 
 
    index = [0] * n  # discovery index of each vertex
    scc.next_index = 1
    
    def dfs(s):
        stack = [s]
        live = [s]
        index[s] = scc.next_index
        roots = [scc.next_index]
        scc.next_index += 1
        while stack:
            src = stack[-1]
            if len(succ[src]) == 0:  # all successors processed, backtrack
                stack.pop()
                if index[src] == roots[-1]:
                    # Unwind the live stack.  
                    # All vertices until src belong to the same SCC.
                    while True:
                        x = live.pop()
                        inscc[x] = scc.n
                        if x == src:
                            break
                    scc.n += 1
                    roots.pop()
            else: # we have one successor
                dst = succ[src].pop()
                idst = index[dst]
                if idst > 0:  # a previously visited vertex 
                    if inscc[dst] is None: # but not yet in a known SCC
                        # pop all roots greater that idst
                        while roots[-1] > idst:
                            roots.pop()
                else: # a new vertex
                    index[dst] = scc.next_index
                    roots.append(scc.next_index)
                    scc.next_index += 1
                    stack.append(dst)
                    live.append(dst)
    for s in range(n):
        if inscc[s] is None:
            dfs(s)
    return inscc
