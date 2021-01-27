def word_count_engine(document):
  hash_map = {}
  res = []
  doc_list = document.split()

  for i in range(len(doc_list)):
    word = ''
    for char in doc_list[i]:
      if char.isalpha():
        word+=char
    if word.lower() not in hash_map:
      hash_map[word.lower()] = (0, i)
    
    hash_map[word.lower()] = (hash_map[word.lower()][0]+1, hash_map[word.lower()][1])

  for s in hash_map:
    res.append([s, hash_map[s]])
  
  res.sort(key=lambda x: (x[1][0], -x[1][1]), reverse=True)
  for i in range(len(res)):
    s, vals = res[i]
    res[i] = [s, str(vals[0])]
  return res