// Given a set of distinct integers, nums, return all possible subsets (the power set).
// Note: The solution set must not contain duplicate subsets.

// function subsets(nums, cache={'': true}, result=[[]]) {
//   if (nums.length == 0) return result;

//   if (cache[nums]) return result;

//   cache[nums] = true;
//   result.push(nums);
//   subsets(nums.slice(1), cache, result)
//   subsets(nums.slice(0,-1), cache, result)

//   return result;
// }

function subsets(nums){
  let result = [];
  dfs([], 0);
  
  function dfs(current, index){
      result.push(current);
      for(let i = index; i < nums.length; i++) {
          dfs(current.concat(nums[i]), i + 1);
      }
  }
  
  return result;
}

console.log(subsets([1,2,3]))

// [1,2,3]
/**
  []
  [1] 1 = 2
  [2] 
  [1,2] 2 = 4
  [3]
  [1,3]
  [2,3]
  [1,2,3] 3 = 8
 */