# QuickSort implementation

def q_sort(L):
    a = [x for x in L if x < L[0]]
    b = [x for x in L if x == L[0]]
    c = [x for x in L if x > L[0]]
    if L: return q_sort(a) + b + q_sort(c)
    return []
    
list_q = [4,76,2,5554,13,2568,3,6,1,987,765,234,8]
print(q_sort(list_q))
    
