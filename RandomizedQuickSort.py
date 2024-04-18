import random
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

def randomizedQuickSort(arr, start, end):
    if end-start<1:#예외처리 1
        return
    if end-start==1:#배열의 길이가 2인경우 naiveQuickSort로 정렬 랜덤하게 3개의 원소를 뽑을 수 없기 때문
        quickSort(arr,start,end)
        return
        
    
    # 랜덤하게 피벗을 선택
    if start<end:
        randomIndex = random.sample(range(start,end+1),3)#3개의 index를 범위내에서 랜덤하게 선정
        randomValue=[arr[randomIndex[0]],arr[randomIndex[1]],arr[randomIndex[2]]]#선정된 랜덤 인덱스들이 가리키는 값을 가져옴
        quickSort(randomValue,0,2)#선정된 값들을 정렬
        for i in randomIndex:
            if arr[i]==randomValue[1]:#정렬된 랜덤값들의 중간값을 피벗으로 선정
                medianIndex=i#피벗의 위치를 medianIndex에 할당
                
                
        arr[medianIndex], arr[end] = arr[end], arr[medianIndex]#피벗을 끝으로 옮김
        #다음은 naiveQuickSort와 같이 진행
        pivot = arr[end]
        k = start - 1
        
        for j in range(start, end):
            if arr[j] <= pivot:
                k += 1
                arr[k], arr[j] = arr[j], arr[k]
        
        arr[k + 1], arr[end] = arr[end], arr[k + 1]
        pivotIndex = k + 1

        randomizedQuickSort(arr, start, pivotIndex - 1)#재귀적 호출로 왼쪽 배열 정렬
        randomizedQuickSort(arr, pivotIndex + 1, end)#재귀적 호출로 오른쪽 배열 정렬
    return arr

arr=[3, 5, 7, 8, 1, 2, 5, 4, 11, 35, 88, 412, 11, 66, 9, 5, 23, 1, 3, 5, 4, 9, 8, 4, 32, 1, 22, 0, 16]
print(randomizedQuickSort(arr,0,len(arr)-1))