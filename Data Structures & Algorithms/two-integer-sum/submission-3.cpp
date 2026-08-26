class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int key;
        for (int i = 0; i < nums.size()-1; i++){
            key = target - nums[i];
            for (int j = i+1; j < nums.size(); j++){
                if (nums[j] == key){
                    return {i, j};
                }
            }
        }
    }
};
