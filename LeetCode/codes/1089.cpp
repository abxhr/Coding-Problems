// Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        vector<int> res;
        for (int i = 0; res.size() < arr.size(); i++){
            if (arr[i] == 0){
                res.push_back(0);
                res.push_back(0);
            }
            else{
                res.push_back(arr[i]);
            }
        }
        if (res.size() != arr.size())
            res.pop_back();
        arr = res;
    }
};