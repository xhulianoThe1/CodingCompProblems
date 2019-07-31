var mostCommonWord = function(p, b) {    
    p = p.toLowerCase().match(/[^_\W]+/g).join(' ').split(" "); 
    for(var i = 0; i < p.length; i++){ 
        for(var k = 0; k < b.length; k++){ 
            while(p[i] == b[k]){ 
                    p.splice(i, 1); 
            }
        }
    } 
    
    if (b == 0) {
        return p.join(""); 
    }
     
    var temp = 0, max = 0, mostCommon = 0, i;
    for (i = 0; i < p.length - 1; i++) {
      var temp1 = 1;
      var j = void 0;
      for (j = i + 1; j < p.length; j++) {
        if (p[i] == p[j]) {
          temp1++;
        }
      }
      if (temp1 > max) {
        max = temp1;
        mostCommon = p[i];
      }
    }

    if(mostCommon == 0){ 
        return p[i]; 
    }
    else { 
        return mostCommon; 
    }
};