def main(arr):

    for i in range(len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    print(arr)



if __name__ == "__main__":
    main([5, 9, 3, 20, 22, 24])