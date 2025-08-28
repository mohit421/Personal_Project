'''
8. String to Integer (atoi)
'''


class Solution:
    def myAtoi(self, s: str) -> int:

        def whitespaces(i:int)->int:
            if i<len(s) and s[i] == " ":
                return whitespaces(i+1)
            return i

        def get_sign(i:int):
            sign = 1
            if i<len(s) and (s[i] == '-' or s[i]=='+'):
                if s[i] == '-':
                    sign = -1
                i += 1
            return sign, i

        def build_int(i:int, value: int)->int:
            if i >= len(s) or not s[i].isdigit():
                return value
            digit = int(s[i])

            new_val = value*10 + digit
            return build_int(i+1, new_val)




        i = whitespaces(0)
        sign, i = get_sign(i)
        num = build_int(i,0)

        num = sign*num
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        return max(min(num,INT_MAX),INT_MIN) 