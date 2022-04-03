var judgeCircle = function(moves) {
    var x = 0, y = 0, i; 
    var a = moves.split(""); 
    for(i = 0; i < moves.length; i++){ 
        if(a[i] == 'U'){
            y += 1
        } 
        
        else if(a[i] == 'D'){
            y -= 1 
        } 
        
        else if(a[i] == 'R'){
            x += 1
        } 
        
        else if(a[i] == 'L'){
            x -= 1
        } 
    } 

    if (x == 0 && y == 0) {
        return true; 
    }
    else { 
        return false; 
    }

};
