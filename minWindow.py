from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        target_freq = Counter(t)
        window_freq = {}

        have, need = 0, len(target_freq)
        res, res_len = [-1, -1], float("infinity")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1

            if char in target_freq and window_freq[char] == target_freq[char]:
                have += 1

            while have == need:
                # Update result if current window is smaller
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Contract window from left
                left_char = s[left]
                window_freq[left_char] -= 1
                if left_char in target_freq and window_freq[left_char] < target_freq[left_char]:
                    have -= 1
                left += 1
        
        start_index, end_index = res
        return s[start_index : end_index + 1] if res_len != float("infinity") else ""
