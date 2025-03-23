class Solution:
    def isValid(self, s: str) -> bool:
        closingDict = {'(': ")", "{": "}", "[": "]"}
        stack = []

        for x in s:
            if x not in closingDict:
                if stack and x == closingDict[stack[-1]]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(x)
        if len(s) < 2 or stack:
            return False
        return True

        