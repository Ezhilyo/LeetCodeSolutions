class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        int n= arr.size();
        int i,j;
        vector<bool> is_present(n,0);
        for(auto piece: pieces){
            bool is_piece_present = false;
            for(i=0;i<n;i++){
                for(j=i;j<i+piece.size();j++){
                    if(piece[j-i]!=arr[j]){
                        break;
                    }
                }
                if(j==i+piece.size()){
                    is_piece_present = true;
                    for(j=i;j<i+piece.size();j++){
                        is_present[j]=true;
                    }
                }
            }
            if(!is_piece_present){
                return false;
            }
        }
        return true;
    }
};