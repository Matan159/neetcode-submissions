class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numset;
        vector<int> candidates;
        int res = 0;
        for (int num:nums){
            if (numset.count(num)){ continue; }
            else {
                numset.insert(num);
            }
        }
        for (int num:numset){
            if (numset.count(num-1)){ continue; }
            candidates.push_back(num);
        }
        int count=0;
        int val;
        for (int num:candidates){
            val = num;
            count = 1;
            while (numset.count(val+1)){
                val +=1;
                count +=1;
            }
            res = max(res, count);
        }
        return res;
    }
};
