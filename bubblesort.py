

#program to sort a list of items


array1 = [2,4,3,1]
array2 = [5,1,8,4,2,8,4,8,5,7]
def bubbleSort(array):
    tally = 0
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            tally +=1
            print(array[j], "compared to", array[j+1])

            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubbleSort(array2))
