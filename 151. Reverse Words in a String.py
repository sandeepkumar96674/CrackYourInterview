class Solution(object):
    def reverseWords(self, s):
        length = len(s)
        word_positions = [] 
        i = 0
        while i < length:
            while i < length and s[i] == ' ':
                i += 1
            if i == length:
                break
            start = i  
            while i < length and s[i] != ' ':
                i += 1
            end = i - 1  
            word_positions.append((start, end))
        
        result = []
        for start, end in reversed(word_positions):
            word = s[start:end + 1]
            result.append(word)
        
        return ' '.join(result)