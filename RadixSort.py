def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # 각 자리수의 빈도수 카운팅
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # 누적 빈도수 계산
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # 정렬된 배열 구성
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # 원래 배열에 복사
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr):
    # 입력 배열의 최댓값 찾기
    max_num = max(arr)
    
    # 최댓값의 자리수 계산
    exp = 1
    while max_num // exp > 0:
        countingSort(arr, exp)
        exp *= 10

# 테스트용 배열
arr = [170, 45, 75, 90, 802, 24, 2, 66]
# Radix sort 수행
radixSort(arr)
# 결과 출력
print(arr)

#radix정렬은 반복문을 통해 다른 정렬 함수를 실행하여 그 정렬함수가 기수정렬을 해둔다
