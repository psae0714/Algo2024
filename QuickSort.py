def quickSort(arr,start,end):
    if start<end:
        pivot=arr[end]
        i=start-1
        
        for j in range(start,end):
            if arr[j]<=pivot:
                i+=1
                arr[j],arr[i]=arr[i],arr[j]
                
        arr[i+1],arr[end]=arr[end],arr[i+1]
        mid=i+1
        quickSort(arr,start,mid-1)
        quickSort(arr,mid+1,end)
    return arr
arr=[3, 5, 7, 8, 1, 2, 5, 4, 11, 35, 88, 412, 11, 66, 9, 5, 23, 1, 3, 5, 4, 9, 8, 4, 32, 1, 22, 0, 16]
print(quickSort(arr,0,len(arr)-1))