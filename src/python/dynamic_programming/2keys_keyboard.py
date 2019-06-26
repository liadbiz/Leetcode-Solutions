"""
650. 2 Keys Keyboard
source: https://leetcode-cn.com/problems/2-keys-keyboard/

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

"""
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i // 2, 0, -1):
                if i % j == 0:
                    dp[i] = dp[j] + i // j
                    break
        return dp[-1]


if __name__ == "__main__":
    n= 6
    assert Solution().minSteps(n) == 5, "result is not correct"
