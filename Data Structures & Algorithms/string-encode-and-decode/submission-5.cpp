class Solution {
public:
    
    string encode(vector<string>& strs) {
        string res = "";
        string temp = "";
        for (auto& str : strs){
            res += ',';
            res += to_string(str.length());
            temp += str;
        }
        res = res+':'+temp;
        return res;

    }

    vector<string> decode(string s) {
        vector<std::string> res = {};
        vector<int> lens = {};
        string temp = "";
        while (s[0] == ','){
            s.erase(0, 1);
            temp = "";
            while (s[0] != ',' && s[0] != ':'){
                temp += s[0];
                s.erase(0, 1);
            }
            lens.push_back(stoi(temp));
        }
        s.erase(0, 1);
        
        for (int i=0; i<lens.size(); i++){
            temp = s.substr(0, lens[i]);
            res.push_back(temp);
            s = s.substr(lens[i], s.length()-lens[i]);
        }
        return res;
    }
};
