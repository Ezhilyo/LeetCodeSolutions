class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int n=A.size();
        if(n<3){
            return 0;
        }
        int diff=A[1]-A[0];
        int i=2;
        int total=0;
        int temp=1;
        while(i<n){
            if(A[i]-A[i-1]==diff){
                temp++;
            }else{
                total+=temp*(temp-1)/2;
                diff=A[i]-A[i-1];
                temp=1;
            }
            if(i==n-1){
                total+=temp*(temp-1)/2;
            }
            i++;
        }
        return total;
    }
};

