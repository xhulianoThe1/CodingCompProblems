var fib = function(N) {
  var start = 1, total = 0, temp; 

  while(N > 0){ 
    temp = start; 
    start = total + start; 
    total = temp;  
    N--; 
 }
return total; 

};