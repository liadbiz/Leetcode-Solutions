class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1] <= target:
            for i in letters:
                if i < target:
                    return i
        else:
            for i in letters:
                if i > target:
                    return i
         
            
if __name__ == "__main__":
    letters = ["c", "f", 'j']
    target1 = "a"
    target2 = "c"
    target3 = "d"
    target4 = "g"
    target5 = "j"
    target6 = "k"
    print(Solution().nextGreatestLetter(letters, target1))
    print(Solution().nextGreatestLetter(letters, target2))
    print(Solution().nextGreatestLetter(letters, target3))
    print(Solution().nextGreatestLetter(letters, target4))
    print(Solution().nextGreatestLetter(letters, target5))
    print(Solution().nextGreatestLetter(letters, target6))
