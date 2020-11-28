// Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

// [4,5,6,7,0,1,2] if it was rotated 4 times.
// [0,1,2,4,5,6,7] if it was rotated 7 times.
// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

// Given the sorted rotated array nums, return the minimum element of this array.


var findMin = function(nums) {
  let m,
      s = 0,
      e = nums.length-1;
  
  if (nums.length == 1 || nums[e] > nums[0]) return nums[0]
  
  while (e >= s) {
      m = Math.floor((e+s)/2)   
      if (nums[m] > nums[m+1]) return nums[m+1];
      if (nums[m-1] > nums[m]) return nums[m];
      if (nums[m] > nums[0]) s = m+1;
      else e = m-1;
  }
  
  return nums[e]
};