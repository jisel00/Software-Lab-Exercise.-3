def BS(j, k, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if j[mid] == k:
            return mid
        elif j[mid] < k:

            low = mid + 1
        else:

            high = mid - 1
    return -1


j = [3, 1, 4, 2, 8]

k = 5
result = BS(j, k, 0, len(j) - 1)

if result != -1:

    print("Element is present at index: " + str(result))

else:

    print("Not found")


