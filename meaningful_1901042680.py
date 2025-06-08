def meaningful(a, left, right, k):
    if k > 0 and k <= (right-left+1):
        p = partition(a, left, right)
        
        if p-left == k-1:
            return a[p]
            
        if p-left > k-1:
            return meaningful(a, left, p-1, k)
            
        return meaningful(a, p+1, right, k-p+left-1)
        
def partition(a, left, right):
    i = a[right]
    j = left
    
    for k in range(left, right-1):
        if a[k] <= i:
            temp = a[j]
            a[j] = a[k]
            a[k] = temp
            
            j += 1
            
    temp = a[j]
    a[j] = a[right]
    a[right] = temp
    
    return j
    
a = [4,2,4,6,34,6]
print("kth smallest element: ", meaningful(a, 0, len(a)-1, 3))