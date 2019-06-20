var numJewelsInStones = function(J, S) {
    var total = 0; 
    //Loop through the J string and return the # of jewels 
    for(var i = 0; i < J.length; i++) { 
        for(var k = 0; k < S.length; k++){ 
            if(J[i] == S[k]){ 
                total += 1; 
            } 
        }
    } 
    return total; 
}; 

