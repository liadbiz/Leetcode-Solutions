"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution:
    # 思路： 其实很简单，找出出现次数最多的task，那么我们应该把其他task插入到
    # 该task之间，将插入适当的idle保证每个该task之间的task的数是等于n的，那么
    # 被该task隔开的task之间的距离也是大于或者等于n的。然后将这种方案求的的
    # interval的数目和输入的长度取最大值即可，为什么要取这两者的最大值呢？因为
    # 会出现n的值小于出现次数最多的task的数量，那么用以上方法求出的就会小于
    # tasks的长度，但是实际上每个task都要一个interval，因此取两者最大值即可。
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        task_count = collections.Counter(tasks)
        max_count = max(task_count.values())
        print(max_count)
        return max((max_count  - 1) * (n + 1) + sum(1 for i in task_count.values() if i == max_count ), len(tasks))


if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(Solution().leastInterval(tasks, n))
