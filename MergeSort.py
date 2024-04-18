def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        
        leftHalf=arr[:mid]
        rightHalf=arr[mid:]
        
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        
        k=i=j=0
        
        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i]<rightHalf[j]:
                arr[k]=leftHalf[i]
                i+=1
            else:
                arr[k]=rightHalf[j]
                j+=1
            k+=1
        
        while i<len(leftHalf):
            arr[k]=leftHalf[i]
            i+=1
            k+=1
        while j<len(rightHalf):
            arr[k]=rightHalf[j]
            j+=1
            k+=1
    return arr

arr=[3, 5, 7, 8, 1, 2, 5, 4, 11, 35, 88, 412, 11, 66, 9, 5, 23, 1, 3, 5, 4, 9, 8, 4, 32, 1, 22, 0, 16]
print(mergeSort(arr))