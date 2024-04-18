def mergeInsertionSort(arr):
    if len(arr)>5:#배열의 길이가 5보다 클때 실행될 수 있도록 하였습니다.
        mid=len(arr)//2
        leftHalf=arr[:mid]
        rightHalf=arr[mid:]
#merge sort와 같은 방식으로 진행됩니다.
        
        mergeInsertionSort(leftHalf)
        mergeInsertionSort(rightHalf)
        
        i=j=k=0
        while i<len(leftHalf) and j<len(rightHalf):
            #나뉘어진 부분 배열들을 insertion sort를 진행하여 먼저 정렬합니다.
            insertionSort(leftHalf)
            insertionSort(rightHalf)
            #이후 각 배열들의 같은 인덱스를 갖고 있는 원소들의 값들을 비교하여 병합합니다.
            while i<len(leftHalf) and j<len(rightHalf):
                if leftHalf[i]<rightHalf[j]:
                    arr[k]=leftHalf[i]
                    i+=1
                else:
                    arr[k]=rightHalf[j]
                    j+=1
                k+=1
            #병합 후 남은 것들을 마저 병합합니다.    
            while i<len(leftHalf):
                arr[k]=leftHalf[i]
                i+=1
                k+=1
            while j< len(rightHalf):
                arr[k]=rightHalf[j]
                j+=1
                k+=1
    return arr   

def insertionSort(arr):
    length=len(arr)

    for i in range(1,length):
        key=arr[i]
        
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr


arr=[3, 5, 7, 8, 1, 2, 5, 4, 11, 35, 88, 412, 11, 66, 9, 5, 23, 1, 3, 5, 4, 9, 8, 4, 32, 1, 22, 0, 16]
print(mergeInsertionSort(arr))