var selfDividingNumbers = function(left, right) {
    var arr = [];
    var arr2 = [];
    var y, z; 
    while (left <= right){ 
        if(left % 10 != 0){
            y = left.toString();
            z = y.split("")
            arr.push(left)
            for(k = 0; k < z.length; k++){ 
                if(((left/z[k]) % 1) != 0){ 
                   //console.log("left", left)
                    //console.log(arr2)
                    arr2.push(left)
                    break;
                    
                    
                }
                
            } 
            
        }
            left++; 
    } 
 
    
       var a = [], diff = [];

    for (var i = 0; i < arr.length; i++) {
        a[arr[i]] = true;
    }

    for (var i = 0; i < arr2.length; i++) {
        if (a[arr2[i]]) {
            delete a[arr2[i]];
        } else {
            a[arr2[i]] = true;
        }
    }

    for (var k in a) {
        diff.push(k);
    }

    return diff;
    
    
    
}; 
