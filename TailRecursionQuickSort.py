def tailRecursiveQuickSort(arr,start,end):
    while start<end:#배열의 크기가 1이 되기 전까지 반복적 진행
        pivot=arr[end]#배열의 끝 피벗으로 선정
        i=start-1#왼쪽 배열의 인덱스
        
        #niaveQuickSort와 같이 진행
        for j in range(start,end):
            if arr[j]<=pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]

        arr[i+1],arr[end]=arr[end],arr[i+1]
        mid=i+1
        #재귀적 호출을 한번만 사용해 왼쪽 배열 정렬
        tailRecursiveQuickSort(arr,start,mid-1)
        #배열의 시작을 갱신
        start=mid+1
        #while문 반복 진행으로 초기 배열의 오른쪽 배열을 추가적인 재귀적 호출없이 정렬
        
    return arr

arr=[3, 5, 7, 8, 1, 2, 5, 4, 11, 35, 88, 412, 11, 66, 9, 5, 23, 1, 3, 5, 4, 9, 8, 4, 32, 1, 22, 0, 16]
print(tailRecursiveQuickSort(arr,0,len(arr)-1))