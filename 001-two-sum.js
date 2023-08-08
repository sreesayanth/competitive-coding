function twoSum(nums, target) {
    let numObj = {};
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        console.log(numObj[complement], complement);
        if (numObj[complement] !== undefined) {
            return [numObj[complement], i];
        }
        numObj[nums[i]] = i;
    }
}
nums = [2, 7, 11, 15]
target = 9
console.log(twoSum(nums, target));
