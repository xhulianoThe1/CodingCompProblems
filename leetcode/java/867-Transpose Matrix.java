class Solution {
    public int[][] transpose(int[][] A) { 
        int I = A.length, J = A[0].length; 
        int[][] a = new int[J][I]; 
        for(int i = 0; i< I; i++){ 
            for(int j = 0; j < J; j++){ 
                a[j][i] = A[i][j]; 
            } 
        }
        return a; 
    }
}
