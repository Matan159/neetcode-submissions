using namespace std;
class Solution {
    #include <unordered_set>
    #include <iostream>
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> mySet;
        for (auto itr = nums.begin(); itr != nums.end(); itr++){
            cout << *itr << endl;
            if (mySet.count(*itr)) {
                return true;
            }
            mySet.insert(*itr);
        }
        return false;
    }
};