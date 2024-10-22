def insertSort(list):
    for i in range(1,len(list)):
        temp = list[i]
        j = i-1
        while(list[j] > temp and j >= 0):
            list[j+1] = list[j]
            j-=1
        list[j+1] = temp

    return list



print(insertSort([1,34,5,6,1,4.6,56,1,3,5]))