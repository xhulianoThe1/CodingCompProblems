var reverse = function (x) {
    if(x/-1 > 0){
        x = x/-1
        var y = x.toString();
        var z = y.split("").reverse().join("");
        var a = Number(z);
        a = a * -1; 
            if(a < -2147483648) { 
                return 0; 
            }
            else{ 
            return a; 
                }
    }
    
     else { 
        var y = x.toString();
        var z = y.split("").reverse().join("");
        var a = Number(z);

            if(a > 2147483648) { 
                return 0; 
            }
            else{ 
            return a; 
                }
     }          
         }; 