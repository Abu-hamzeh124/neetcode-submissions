class Solution:
    def isPalindrome(self, s: str) -> bool:
        sFinal = "".join(c.lower() for c in s if c.isalnum())
        return sFinal == sFinal[::-1]
