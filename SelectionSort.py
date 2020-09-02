def selectionSort(arr):
    for i in range(len(arr)):
    
      minimum = i
      for j in range(i+1, len(arr)):
        if arr[minimum] > arr[j]:
          minimum = j
      arr[minimum], arr[i] = arr[i], arr[minimum]

    return(arr)
