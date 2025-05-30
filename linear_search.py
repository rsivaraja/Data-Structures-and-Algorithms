def linearsearch(n):
    numbers=[1,4,6,36,7,57,46,8,59,64]
    for i in range(len(numbers)):
        if numbers[i]==n:
            print(f'Number is found in {i} position')
            break
    else:
        print('not found')
linearsearch(17) 