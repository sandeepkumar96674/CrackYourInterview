class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        max_length = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(max_freq, char_count[s[right]])

            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length       