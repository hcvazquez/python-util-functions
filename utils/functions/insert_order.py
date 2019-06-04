def insert(arr, n):
    # Searching for the position 
    for i in range(len(arr)):
        if arr[i] > n:
            index = i
            break

    # Inserting n in the list 
    arr = arr[:index] + [n] + arr[index:]
    return arr