def my_sort(arr):
    n = len(arr)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr


numbers = [1, 4, 7, 3, 8, 3, 9, 8]
my_sort(numbers)
print(numbers)

