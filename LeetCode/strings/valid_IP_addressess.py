def validIPAddresses(string):
    result = []
    def helper(curr_str, strIdx, dots):
      if not dots:
        remain = string[strIdx:]
        if len(string) - strIdx > 3 or strIdx >= len(string) or int(remain) > 255 or len(remain) >= 2 and remain[0] == '0':
          return
        result.append(curr_str+remain)
        return
      if strIdx >= len(string):
        return
      one_slice_str = curr_str + string[strIdx] + '.'
      helper(one_slice_str, strIdx+1, dots-1)
      
      if string[strIdx] != '0':
        two_slice_str = curr_str + string[strIdx:strIdx+2] + '.'
        helper(two_slice_str, strIdx+2, dots-1)

        thr_slice_str = string[strIdx:strIdx+3]
        if int(thr_slice_str) <= 255:
          helper(curr_str + thr_slice_str + '.', strIdx+3, dots-1)
    
    helper("", 0, 3)
    return result