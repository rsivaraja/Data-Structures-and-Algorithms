def insertion_sort(numbers):
    for i in range(1,len(numbers)):
        temp=numbers[i]
        j=i-1
        while j>=0 and temp>numbers[j]:
            numbers[j+1]=numbers[j]
            j-=1
        numbers[j+1]=temp
    return numbers
print(insertion_sort([1,3,4,6,7,8,99,123,3,4,56,7,7,7]))
