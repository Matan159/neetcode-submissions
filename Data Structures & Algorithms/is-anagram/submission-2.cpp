using namespace std;
class Solution {
    #include <unordered_map>
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }
        unordered_map<char, int> sChars;
        unordered_map<char, int> tChars;
        for (auto cs:s){
            if (sChars.count(cs)){
                sChars[cs]++;
            } else {
                sChars[cs] = 1;
            }
        }
        for (auto ct:t){
            if (tChars.count(ct)){
                tChars[ct]++;
            } else {
                tChars[ct] = 1;
            }
        }
        for (auto& [c,n]:sChars){
            if (n != tChars[c]){
                return false;
            }
        }
        return true;
    }
};
