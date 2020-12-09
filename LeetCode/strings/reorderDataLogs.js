// You have an array of logs.  Each log is a space delimited string of words.

// For each log, the first word in each log is an alphanumeric identifier.  Then, either:

// Each word after the identifier will consist only of lowercase letters, or;
// Each word after the identifier will consist only of digits.
// We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

// Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

// Return the final order of the logs.



var reorderLogFiles = function(logs) {
  let digits = [];
  let letters = [];
  
  for (i in logs) {
      let temp = logs[i].split(" ");
      if (isNaN(temp[1])) letters.push(logs[i]);
      else digits.push(logs[i]);
  }
  
  letters.sort(function(a, b) {
      let subA = a.substring(a.indexOf(" "));
      let subB = b.substring(b.indexOf(" "))
      return subA.localeCompare(subB) == 0 ? a.localeCompare(b) : subA.localeCompare(subB)
  })
  
  return [...letters, ...digits]
};