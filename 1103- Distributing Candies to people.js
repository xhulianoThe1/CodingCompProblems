var distributeCandies = function(candies, num_people) {
    var arr = []
    while(num_people!= 0){ 
        arr.push(0)
        num_people--;
    }    
    

var total = 1;  
restartLoop: 
while (true){ 
for(var i = 0; i < arr.length; i++){ 
    if(total > candies){ 
        arr[i] += candies
        break;
    }
    arr[i] += total
    candies = candies - total 
    total++
     
    //signify that there are no more candies 
    if (candies <= 0){ 
        break;
    }
    //signify that the loop finished 
    else if (i + 1 == arr.length){ 
        continue restartLoop; 
    }
   
}
    break; 
} 
return arr
};