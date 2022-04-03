var hammingDistance = function(x, y) {
    var x = x.toString(2).split(""), y = y.toString(2).split(""), total = 0
    
    if(x.length > y.length){ 
        while(x.length > y.length){
        y.unshift('0')
       } 
    }
    
    else if(y.length > x.length){ 
       while(y.length > x.length){
        x.unshift('0')
       } 
    }

    for(var i = 0; i < x.length; i++){ 
            if(x[i] != y[i]){ 
                total += 1
            }
    }
     return total
};
