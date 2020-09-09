function validAnagram(an1, an2) {
  if (an1.length !== an2.length) return false;
  let freq1 = {};
  let freq2 = {};
  for (let i=0;i<an1.length;i++) {
    if (freq1[an1.charAt(i)]) freq1[an1.charAt(i)] = freq1[an1.charAt(i)]+1
    else freq1[an1.charAt(i)] = 1
  }
  for (let i=0;i<an2.length;i++) {
    if (freq2[an2.charAt(i)]) freq2[an2.charAt(i)] = freq2[an2.charAt(i)]+1
    else freq2[an2.charAt(i)] = 1
  }
  for (let key in freq1) {
    if (freq1[key] !== freq2[key]) return false;
  }
  return true;
}

console.log(validAnagram('',''))
console.log(validAnagram('aaz','zza'))
console.log(validAnagram('anagram','nagaram'))
console.log(validAnagram('rat','car'))
console.log(validAnagram('awesome','awesom'))
console.log(validAnagram('qwerty','qeywrt'))