#EXERCICE 2
def edgeset(edges):
    "Convert a list of undirected edges to a set of directed edges."
    alledges = set()
    for (a,b) in edges:
        alledges.add((a,b))
        alledges.add((b,a))
    return alledges
    
def is_maximal_matching(n, edges, matching):
    alledges = edgeset(edges)
    matched = [False] * n
    for (a,b) in matching:
        if (a,b) not in alledges or matched[a] or matched[b]:
            return False
        matched[a] = True
        matched[b] = True
    return all(matched[a] or matched[b] for (a,b) in edges)
