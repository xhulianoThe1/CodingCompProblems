var findComplement = function(num) {
    var arr2 = []; 
    var arr = (num.toString(2))
    for(var i = 0; i < arr.length; i++){ 
        if(arr[i] == 0){ 
            arr2.push(1)
        }
        else if (arr[i] == 1){ 
            arr2.push(0)
        }
    }
    var digit = arr2.join("")
    var a = parseInt(digit, 2)
    return a
    console.log(a)
    };
