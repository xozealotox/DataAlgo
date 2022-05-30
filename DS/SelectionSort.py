def selection_sort(arr: list, n):
    for i in range(0, n - 2):
        min = i
        for j in range(i + 1, n - 1):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr


if __name__ == '__main__':
    arr = [0, 3, 0, 1, 7, 4, 1, 2, 5]
    x = selection_sort(arr, len(arr))
    print(x)
