// Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

// Notice that the solution set must not contain duplicate triplets.

 

// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Example 2:

// Input: nums = []
// Output: []
// Example 3:

// Input: nums = [0]
// Output: []

var threeSum = function(nums) {
  let result = [];
  nums.sort((a,b) => a-b);
  
  for (let i=0;i<nums.length && nums[i] <= 0;i++) {
      if (i == 0 || nums[i-1] != nums[i]) {
          twoSumII(nums, result, i)
      }
  }
  
  return result;
}

function twoSumII(nums, result, i) {
  let lo = i+1, hi = nums.length-1
  while (lo < hi) {
      let sum = nums[i] + nums[lo] + nums[hi]
      if (sum < 0) lo++;
      else if (sum > 0) hi--;
      else {
          result.push([nums[i],nums[lo],nums[hi]]);
          while (lo < hi && nums[lo] == nums[lo+1]) lo++;
          while (lo < hi && nums[hi] == nums[hi-1]) hi++;
          lo++;
          hi--;
      }
  }
}