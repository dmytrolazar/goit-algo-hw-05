def binary_float_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter = 0
 
    while low <= high:
        iter += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return (iter,mid)
    return (iter, high+1 if (high != len(arr) - 1) else -1)

arr = [2.2, 3.3, 4.4, 10.1, 40.4]
while True:
    x = float(input("Enter a float: "))
    iter, result = binary_float_search(arr, x)
    if result != -1:
        print(f"In {iter} iteration(s), the first element greater than or equal to {x} was found at index {result} of the array.")
    else:
        print(f"In {iter} iteration(s), {x} was found to be greater than every element of the array.")
