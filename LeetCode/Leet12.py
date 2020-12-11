import math
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        num_roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        map_roman = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        r = num
        i = 12
        while r > 0:
            if r >= map_roman[i]:
                for j in range(math.trunc(r / map_roman[i])):
                    roman += num_roman[i]
                r = r % map_roman[i]
            else:
                i -= 1
        return roman