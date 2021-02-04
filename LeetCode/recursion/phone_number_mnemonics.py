def phoneNumberMnemonics(phoneNumber):
    char_map = {
      '1': ['1'],
      '2': ['a','b','c'],
      '3': ['d','e','f'],
      '4': ['g','h','i'],
      '5': ['j','k','l'],
      '6': ['m','n','o'],
      '7': ['p','q','r','s'],
      '8': ['t','u','v'],
      '9': ['w','x','y','z'],
      '0': ['0']
    }
    N, result = len(phoneNumber), []
    def helper(s='', index=0):
      if len(s) == N:
        return result.append(s)
      
      for char in char_map[phoneNumber[index]]:
        helper(s+char, index+1)
    helper()
    return result