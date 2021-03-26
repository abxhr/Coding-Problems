// Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution {
public:
    int scoreOfParentheses(string S) {
        stack<int> st;
        int score = 0;
        for (auto c : S) {
            if (c == '(') {
                st.push(score);
                score = 0;
            }
            else {
                int prev = st.top();
                st.pop();
                score += prev + max(score, 1);
            }
        }
        return score;
    }
};