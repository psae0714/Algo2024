def countSort(inputArr, output, k):
    count = [0] * k#먼저 초기화 필요

    for j in range(0, len(inputArr)):
        count[inputArr[j]] += 1#입력 배열의 각 요소 카운트한다

    for i in range(1, k):
        count[i] += count[i - 1]#빈도수 누적 계산

    for j in range(len(inputArr) - 1, -1, -1):#입력 배열을 순회하며 정렬된 배열에 요소 배치
        output[count[inputArr[j]] - 1] = inputArr[j]
        count[inputArr[j]] -= 1

    return output

inputArr = [1, 2, 3, 3, 3, 4, 5, 5, 2, 6, 1, 1, 3, 4]
output = [0] * len(inputArr)
countSort(inputArr, output, 7)
print(output)
