def merge(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2

    left = m[:mid]
    right = m[mid:]
    left = merge(left)
    right = merge(right)

    return merge_sort(left, right)

def merge_sort(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] >= right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    
    if len(left) != 0:
        result.extend(left)
    if len(right) != 0:
        result.extend(right)
    
    return result

a = [69, 10, 30, 2, 16, 8, 31, 22]
print(merge(a))

        
    
