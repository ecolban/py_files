def give_max_h(n, h_max):
    sieve = prime_sieve(n + 2 * h_max)
    twins = [i for i in xrange(len(sieve) - h_max) if sieve[i] and sieve[i + 1]]

    max_count = 0
    res = []
    for h in xrange(2, h_max + 1, 2):
        count = sum(1 for i in twins if sieve[i + h/2] and sieve[i + h])
        if count == max_count: 
            res.append([h, count])
        elif count > max_count:
            res = [[h, count]]
            max_count = count
        
    return res

def prime_sieve(n):
    '''Returns a sieve such that, for any 3 <= p < n,
       sieve[(p - 3) / 2] == True if and only if p is a prime'''
    sieve = [True for p in range(3, n, 2)]
    for i in range(len(sieve)):
        p = 2 * i + 3
        if p * p > n: return sieve
        elif sieve[i]:
            for j in xrange((p * p - 3)/2, len(sieve), p):
                sieve[j] = False
    return sieve

import re

def is_possible(expression):
    predicate = re.compile(r'[a-z]+')
    clause = re.compile('\(.+?\)')
    neg = re.compile(r'!')
    preds = list(set(re.findall(predicate, expression)))
    clauses = set(re.findall(clause, expression))
    return any(all(eval_clause(c, a) for c in clauses) for a in assignments(preds))
    

def assignments(preds):
    '''returns a list of dicts'''
    if not preds: return [{}]
    p1 = preds[0]
    f = assignments(preds[1:])
    t = [d.copy() for d in f]
    for d in t: d[p1] = True
    for d in f: d[p1] = False
    return t + f

def eval_clause(clause, assignment):
    term = re.compile(r'!?[a-z]+')
    terms = re.findall(term, clause)
    def eval_term(t):
        if t[0] == '!':
            return not assignment[t[1:]]
        else:
            return assignment[t]
    return any(eval_term(t) for t in terms)


expression = "(!aORb)AND(aORc)"

print(is_possible(expression))


