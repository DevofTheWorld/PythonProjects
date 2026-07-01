def bubbleSort(arr):
    temporary = 0

    for i in range(len(arr)):
        current = arr[i]
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temporary = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temporary


    print(arr)

if __name__ == "__main__":
    bubbleSort([12, 5, 13, 21, 16])