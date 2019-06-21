var twoSum = function(nums, target) {   
    var arr = []; 
    var a; 
    for(var i = 0; i < nums.length; i++){
        for (var k = i + 1; k < nums.length; k++) {
            a = nums[i] + nums[k]; 
            if (target == a){ 
                arr.push(i, k);     
            }
        } 
    } 
    return arr; 
}; 