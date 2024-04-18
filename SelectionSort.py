def selectionSort(arr):
    length=len(arr)
    for i in range(length):
        min = i
        for j in range(min+1,length):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
       
arr=[3, 5, 7, 8, 1, 2, 5, 4, 11, 35, 88, 412, 11, 66, 9, 5, 23, 1, 3, 5, 4, 9, 8, 4, 32, 1, 22, 0, 16]
print(selectionSort(arr))        
            
                