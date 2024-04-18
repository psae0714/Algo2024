def heapify(arr, n, i):
    largest = i  # 가장 큰 값을 부모로 설정
    left = 2 * i + 1
    right = 2 * i + 2
  
    # 왼쪽 자식과 비교
    if left < n and arr[i] < arr[left]:
        largest = left
  
    # 오른쪽 자식과 비교
    if right < n and arr[largest] < arr[right]:
        largest = right
  
    # 최대값이 루트가 아니면 교환
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
  
        # 재귀적으로 하위 트리에 대해 heapify 호출
        heapify(arr, n, largest)
  
  
def heapSort(arr):
    n = len(arr)
  
    # Max 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # Max 힙에서 원소 추출하여 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 루트(최대값)와 마지막 노드 교환
        heapify(arr, i, 0)  # root를 heapify
  
  
# 예시 배열
arr = [3, 5, 7, 8, 1, 2, 5, 4, 11, 35, 88, 412, 11, 66, 9, 5, 23, 1, 3, 5, 4, 9, 8, 4, 32, 1, 22, 0, 16]

# heapSort 수행
heapSort(arr)
print("정렬된 배열:", arr)
