def quicksort(a):
    if len(a) <= 1: return a
    pivot = a[len(a) / 2]
    lower = [x for x in a if x < pivot]
    upper = [x for x in a if x > pivot]
    mid = [x for x in a if x == pivot]
    return quicksort(lower) + mid + quicksort(upper)

def superquicksort(a, llb, uub):
#     print ('llb = %d, uub = %d' % (llb, uub))
    if llb == uub: return
    pivot_index = (llb + uub) / 2 
    ulb = pivot_index - 1
    lub = pivot_index + 1
    pivot = a[pivot_index]
    i = ulb
    j = lub
    # for all k: i < k <= ulb => a[k] < pivot
    # for all k: lub <= k < j => a[k] > pivot
    # for all k: ulb < k < lub => a[k] == pivot
    while i >= llb and j <= uub:
        if a[i] < pivot:
            i -= 1
        elif a[i] == pivot:
            a[i], a[ulb] = a[ulb], a[i]
            ulb -= 1
            i -= 1
        elif a[j] > pivot:
            j += 1
        elif a[j] == pivot:
            a[j], a[lub] = a[lub], a[j]
            lub += 1
            j += 1
        else:  # a[j] < pivot and a[i] > pivot
            a[i], a[j] = a[j], a[i]
            i -= 1
            j += 1
            
    if i < llb:
        while j <= uub:
            if a[j] > pivot: j += 1
            elif a[j] == pivot:
                a[j], a[lub] = a[lub], a[j]
                lub += 1
                j += 1
            else:
                ulb += 1
                a[ulb], a[j], a[lub] = a[j], a[lub], a[ulb]
                lub += 1
                j += 1
    elif j > uub:
        while i >= llb:
            if a[i] < pivot: i -= 1
            elif a[i] == pivot:
                a[i], a[ulb] = a[ulb], a[i]
                ulb -= 1
                i -= 1
            else:
                lub -= 1
                a[lub], a[i], a[ulb] = a[i], a[ulb], a[lub]
                ulb -= 1
                i -= 1
    if ulb > llb: superquicksort(a, llb, ulb)
    if lub < uub: superquicksort(a, lub, uub)
