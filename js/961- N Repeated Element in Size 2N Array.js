var repeatedNTimes = function(A) {
  var total = 0, i, k; 
  for (i = 0; i < A.length; i++){ 
        for(k = i + 1; k < A.length; k++) {
            if(A[i]-A[k]==0){ 
                total = A[i]
            }
        }
  }  
    return total; 
};
