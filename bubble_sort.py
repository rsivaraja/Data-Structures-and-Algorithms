def bubble_sort(numbers):
    counter=0
    passes=0
    while counter==0:
        for i in range(len(numbers)-1):
            if numbers[i]>numbers[i+1]:
                temp=numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=temp
                counter+=1
        passes+=1
        if counter==0:
            break
        else:
            counter=0
    print(numbers)
    print(passes)

bubble_sort([1,6,5,7,8,9,4,3,3])

