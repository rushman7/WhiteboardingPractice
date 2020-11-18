// You are given an integer array nums sorted in ascending order, and an integer target.
// Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
// If target is found in the array return its index, otherwise, return -1.

function search(nums, target) {
  let pivot = Math.floor((nums.length-1)/2),
      start = 0,
      end = nums.length-1;

  while (start < end) {
    if (nums[start] <= nums[end]) {
      pivot = start;
      break;
    }
    if (target == nums[pivot]) return pivot;
    if (nums[pivot] > nums[pivot+1]){
      pivot++
      break;
    }
    if (nums[pivot] > nums[start]) start = pivot, pivot = Math.floor((start+end)/2);
    else end = pivot, pivot = Math.floor((start+end)/2);
  }
  // console.log(pivot)
  if (target < nums[pivot]) return -1;
  if (pivot == 0) start = 0, end = nums.length-1;
  else if (target >= nums[0]) start = 0, end = pivot-1;
  else if (target <= nums[nums.length-1]) start = pivot, end = nums.length-1;

  // console.log(start,end,pivot)
  while (start < end) {
    let mid = Math.floor((start+end)/2);
    // console.log('B',start, mid, end)
    if (nums[mid] == target) return mid;
    if (target > nums[mid]) start = mid+1;
    else end = mid;
    // console.log('A', start, mid, end)
  }

  return nums[start] == target ? start : -1
};

console.log(search([4,5,6,7,0,1,2], 6)) // 2
console.log(search([4,5,6,7,8,0,1,2], 5)) // 1
console.log(search([4,5,6,7,0,1,2], 3)) // -1
console.log(search([1], 0)) // -1
console.log(search([1,3], 0)) // -1
console.log(search([1,3], 3)) // 1
console.log(search([1,3,5], 2)) // -1
console.log(search([1,3,5], 1)) // 0
console.log(search([1,2,3,4,5], 2)) // 1