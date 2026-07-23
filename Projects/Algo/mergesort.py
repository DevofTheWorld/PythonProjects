''' is an efficient, comparison-based, and stable sorting algorithm
that follows the divide-and-conquer computer science paradigm.
It works by recursively breaking an array down into single-element subarrays,
then merging those subarrays back together in the correct sorted order'''

def mergesort(arr):
        # determine the length of the int arr
        # length / 2
    length = len(arr) / 2

    if int(length) % 2 == 1:
        length += .5


    leftarr = arr[:int(length)]
    rightarr = arr[int(length):]





if __name__ == '__main__':
    mergesort([3, 4, 6, 7, 2, 18, 20])