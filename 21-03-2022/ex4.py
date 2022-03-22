#EXERCICE 4

def edgeset(edges):
    "build a set of edges with both directions"
    alledges = set()
    for (a,b) in edges:
        alledges.add((a,b))
        alledges.add((b,a))
    return alledges

def adjlists(n, edges, matchingedges):
    succ_matching = [[] for i in range(n)]
    succ_nonmatching = [[] for i in range(n)]
    for (a,b) in edges:
        s = succ_matching if (a,b) in matchingedges else succ_nonmatching
        s[a].append(b)
        s[b].append(a)
    return succ_matching, succ_nonmatching

def find_augmenting_path(n, edges, matching):
    freevertices = [True] * n
    for (a,b) in matching:
        freevertices[a] = freevertices[b] = False
    succ_matching, succ_nonmatching = adjlists(n, edges, edgeset(matching))

    # DFS-based exploration of all possible alternating paths starting from start.
    seen = [False] * n    
    def rec(start):
        seen[start] = True
        # start should be followed by a non-matching edge
        for y in succ_nonmatching[start]:
            if seen[y]:
                continue
            if freevertices[y]:
                return [start, y]
            seen[y] = True
            # and then a matching edge
            for z in succ_matching[y]:
                if seen[z]:
                    continue
                # and then again non-matching edge...
                res = rec(z)
                if res is not None:
                    return [start, y] + res
            # Erase "seen" on backtrack
            # This unfortunately causes the algorithm to become exponential 
            # in the worst case since it explores all possibles alternating paths.
            # For a polynomial implementation lookup Edmonds' Blossom algorithm.
            seen[y] = False
        seen[start] = False
        return None
        
    for start,isfree in enumerate(freevertices):
        if isfree:
            res = rec(start)
            if res:
                return res;
    return None
