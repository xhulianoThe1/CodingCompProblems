
var diStringMatch = function(S) {
    var arr = [], k = 0, z = S.length; 
    
    if(S[0] == 'I'){ 
        arr.push(k)
        k++
    }
    else{ 
        arr.push(z)
        z--
    }
    
for(var i = 0; i<S.length; i++){ 
    if(S[i + 1] == 'D'){ 
       arr.push(z)
        z--
       }
       else if(S[i + 1] =='I') { 
    arr.push(k)
           k++
       } 
}
    
if(arr[S.length -1] == 'I'){ 
    arr.push(k)
}

else { 
    arr.push(z)
}
 
    return arr
};
