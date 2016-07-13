a, j = [1], [0]

def john_(n):
    while len(j) <= n:
        m = len(j)
        t = j[-1]
        j.append(m - ann_(t))
    return j[n]
    
def ann_(n):
    while len(a) <= n:
        m = len(a)
        t = a[-1]
        a.append(m - john_(t))
    return a[n]

def john(n):
    john_(n - 1)
    return j[:n]

def ann(n):
    ann_(n - 1)
    return a[:n]
        
def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))
