class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        right = len(s)-1
        left = 0
        while right>left:
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        return True