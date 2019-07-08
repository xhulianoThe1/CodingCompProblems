var removeDuplicates = function(S) {
   var arr = [], k = 0; 
   while(k < S.length){ 
        arr.push(S[k]); 
        k++; 
   }
  
for(var i = 0; i < arr.length; i++){
    while(arr[i] == arr[i  + 1]){ 
        arr.splice(i, 2);
        i = 0;
        if(arr.length == 0){ 
            break;
        }
    }
}
var t = arr.join("")
return t
};