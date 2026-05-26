class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            t = ord(c)
            if t<48 or 57<t<65 or 90<t<97 or 122<t:
                continue
            if 97 <= t <= 122:
                arr.append(t-32)
            else:
                arr.append(t)
        left, right = 0, len(arr)-1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True
        