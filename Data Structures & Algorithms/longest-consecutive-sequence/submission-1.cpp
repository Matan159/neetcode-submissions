class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Optimally initializes the set in one line, skipping the manual loop
        unordered_set<int> numset(nums.begin(), nums.end());
        int res = 0;
        
        for (int num : numset) {
            // If num-1 doesn't exist, 'num' is the start of a sequence
            if (!numset.count(num - 1)) {
                int count = 1;
                
                // Count upwards directly without a separate 'val' variable
                while (numset.count(num + count)) {
                    count++;
                }
                
                res = max(res, count);
            }
        }
        
        return res;
    }
};