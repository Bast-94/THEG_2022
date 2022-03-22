#EXERCICE 3

def is_matching(n,edges,pairs):
    # Note: This is a quadratic implementation of is_matching().  Can you see why?
    # Can you guess the complexity of the implementation given in the solution for the first question?
    seen = [False] * n
    for (a,b) in pairs:
        if ((a,b) not in edges) and ((b,a) not in edges):
            return False
        if seen[a] or seen[b]:
            return False
        seen[a] = seen[b] = True 
    return True

def is_perfect_matching(n,edges,matching):
    if (n % 2) or (n/2 != len(matching)):
        return False
    return is_matching(n,edges,matching)
    
