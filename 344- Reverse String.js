/**
 * @param {string} s
 * @return {string}
 */
var reverseString = function(s) {
    var a = s.split(""); 
    var b =  a.reverse(); 
    var c = b.join(""); 
    return c; 
};