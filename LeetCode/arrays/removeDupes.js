// Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

// Clarification:

// Confused why the returned value is an integer but your answer is an array?

// Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

// Internally you can think of this:

var removeDuplicates = function(nums) {
  let dupes = 0,
      anchor = 0;
  
  for (let i=1;i<nums.length;i++) {
      if (nums[anchor] != nums[i]) {
          let temp = nums[anchor+1]
          nums[anchor+1] = nums[i]
          nums[i] = temp
          anchor++;
      } else dupes++
  }
  
  for (let i=0;i<dupes;i++) nums.pop();
};