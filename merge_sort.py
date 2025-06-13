def merge_sort(numbers):
    if len(numbers)>1:
        midpoint=len(numbers)//2
        left=numbers[:midpoint]
        right=numbers[midpoint:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                numbers[k]=left[i]
                k+=1
                i+=1
            else:
                numbers[k]=right[j]
                k+=1
                j+=1
        while i<len(left):
            numbers[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            numbers[k]=right[j]
            k+=1
            j+=1
    return numbers

print(merge_sort([1,3,5,6,56,3,2,899,7]))