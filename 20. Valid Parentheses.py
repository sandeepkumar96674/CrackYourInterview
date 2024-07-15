class Solution:
    def isValid(self, s: str) -> bool:
        sample = []                        
        lookforthese = {")": "(", "}": "{", "]": "["}  
        for no in s:
            if no in lookforthese:                      
                if sample and sample[-1] == lookforthese[no]:
                    sample.pop()              
                else:
                    return False
            else:
                sample.append(no)
        return not sample