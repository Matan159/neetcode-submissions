class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows (9);
        vector<unordered_set<char>> cols (9);
        unordered_set<char> boxes [3][3];
        char temp;
        for (int i=0; i<9; i++){
            for (int j=0; j<9; j++){
                temp = board[i][j];
                if (temp == '.'){ continue; }
                if (rows[i].count(temp) || cols[j].count(temp) || boxes[i/3][j/3].count(temp)){
                    return false;
                }
                rows[i].insert(temp);
                cols[j].insert(temp);
                boxes[i/3][j/3].insert(temp);
            }
        }
        return true;
        
    }
};
