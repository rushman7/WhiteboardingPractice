def longestPeak(array):
    max_peak = 0
    for i in range(1, len(array)-1):
      if array[i-1] < array[i] and array[i] > array[i+1]:
        right, left = i, i
        while left > 0 and array[left] > array[left-1]:
          left-=1
        while right < len(array)-1 and array[right] > array[right+1]:
          right+=1
        if left != i and right != i:
          max_peak = max(max_peak, right-left+1)

    return max_peak