class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        if s == "":
            return True
        ss = [s[0]]
        for i in range(1, len(s)):
            if len(ss) == 0:
                ss.append(s[i])
            else:
                if ss[-1] not in paren_map:
                    return False
                elif ss[-1] in paren_map and s[i] == paren_map[ss[-1]]:
                    ss.pop()
                else:
                    ss.append(s[i])
        return len(ss) == 0        
