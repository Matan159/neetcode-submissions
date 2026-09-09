class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Initialize arrays to false
        bool rows[9][9] = {false};
        bool cols[9][9] = {false};
        bool boxes[3][3][9] = {false};
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char temp = board[i][j];
                if (temp == '.') continue;
                
                // Map '1'-'9' to index 0-8
                int val = temp - '1'; 
                
                // Check if the digit has been seen
                if (rows[i][val] || cols[j][val] || boxes[i/3][j/3][val]) {
                    return false;
                }
                
                // Mark the digit as seen
                rows[i][val] = true;
                cols[j][val] = true;
                boxes[i/3][j/3][val] = true;
            }
        }
        return true;
    }
};