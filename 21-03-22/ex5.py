#EXERCICE 5

# Normalize edges so that vertices are increasing    
def normedge(e):
    return e if e[0] < e[1] else (e[1], e[0])

def update_matching(matching, augpath):
    m = { normedge(e) for e in matching }
    p = { normedge(e) for e in zip(augpath, augpath[1:])}
    return list(m ^ p)
    
def find_maximum_matching(n, edges):
    matching = []
    p = find_augmenting_path(n, edges, matching)
    while p is not None:
        matching = update_matching(matching, p)
        p = find_augmenting_path(n, edges, matching)
    return matching
