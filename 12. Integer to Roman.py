class Solution:
    def intToRoman(self, num: int) -> str:
        
# Here I created a list named as "Val" which contain the integer valued and associate them with other list named as "Roman Symbols"  

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_numeral = []
        for i in range(len(val)):
            while num >= val[i]:
                num -= val[i]
                roman_numeral.append(syms[i])
        return "".join(roman_numeral)