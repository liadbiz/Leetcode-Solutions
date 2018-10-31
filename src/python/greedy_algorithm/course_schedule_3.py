"""
There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
"""
class Solution:
    # 思路：按照结束时间排序，依次遍历courses，维护一个变量start，表示当前学习的课程
    # 花费的总时间，也是下一个课程的开始时间，如果不能学习当前遍历课程，说明之前某个
    # 课程花费时间太长了，因此去掉该课程，进而学习当前遍历课程，这样只会让start变小
    # 因此不会降低课程安排的最优性。这也证明了贪心法能得到最优解。
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        import heapq
        courses.sort(key=lambda x:x[1])
        hq = []
        start = 0
        for t, e in courses:
            start += t
            heapq.heappush(hq, -t)
            while start > e:
                start += heapq.heappop(hq)
        return len(hq)


if __name__ == "__main__":
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    print(Solution().scheduleCourse(courses))
