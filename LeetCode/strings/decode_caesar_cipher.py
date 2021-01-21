def caesarCipherEncryptor(string, key):
  string = [s for s in string]

  for i in range(len(string)):
    val = ord(string[i])+key
    while val > 122:
      val-=26
    string[i] = chr(val)

  return "".join(string)