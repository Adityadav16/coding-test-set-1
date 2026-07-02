def reverse_subarray(arr, left, right):

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1


def perform_operations(arr, operations):

    for left, right in operations:
        reverse_subarray(arr, left, right)

    return arr


arr = [9,8,7,6,5,4,3,2,1,0]

operations = [
    (0,9),
    (4,5),
    (3,6),
    (2,7),
    (1,8),
    (0,9)
]

result = perform_operations(arr, operations)

print(result)
