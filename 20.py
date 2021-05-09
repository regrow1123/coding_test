class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        my_stack = []
        my_table = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        for char in s:
            if not char in my_table:
                my_stack.append(char)
            elif not my_stack or my_table[char] != my_stack.pop():
                return False
        return len(my_stack) == 0