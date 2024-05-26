def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

arr = [int(x) for x in input("Enter the array of integers separated by spaces: ").split()]
n = len(arr)
quick_sort(arr, 0, n-1)

print("Sorted array:", arr)

target = int(input("Enter the target element to replace: "))
replacement = int(input("Enter the replacement element: "))

for i in range(n):
    if arr[i] == target:
        arr[i] = replacement

print("Array after replacing elements:", arr)
