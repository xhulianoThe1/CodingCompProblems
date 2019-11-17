var findOcurrences = function(text, first, second) {
    var res = text.split(" ")
    var arr = []; 
    for(var i =0; i < res.length; i++){
        if(res[i] == first && res[i + 1] ==second && res[i + 2] != undefined){ 
            arr.push(res[i + 2])
        }
    }
    return arr 

};
