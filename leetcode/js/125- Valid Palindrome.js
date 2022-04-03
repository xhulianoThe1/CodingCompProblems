var isPalindrome = function(s) {
    var a = [], b = [], x; 
    x = /[a-z^0-9]/g;
    s= s.toLowerCase().match(x)
    
    if (s != null){ 
        for (var i = s.length - 1;i >= 0; i--){ 
            a.push(s[i])
        } 
        for(var k = 0; k < s.length; k++){ 
              b.push(s[k])
        } 
        for(var i = 0; i < a.length; i++){ 
            if(a[i] != b[i]){ 
                var a = false;
                return a; 
                break; 
            }
        }
        if(a != false){ 
            return true
        }
    } 
    
    else{ 
        return true
    }
};
