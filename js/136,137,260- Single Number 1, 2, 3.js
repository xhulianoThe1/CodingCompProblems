var singleNumber = function(nums) {
   var arr = [], i, k, x, j; 
   for(i = 0; i < nums.length; i++){ 
       for(k = i + 1; k < nums.length; k++){ 
            if(nums[i] == nums[k]){ 
                arr.push(nums[k]); 
            }
       }
   }
    for (x = nums.length - 1; x >= 0; x--) {
        for (j = 0; j < arr.length; j++) {
          if (nums[x] === arr[j]) {
            nums.splice(x, 1);
          }
        }
    }
        return nums;
}; 
