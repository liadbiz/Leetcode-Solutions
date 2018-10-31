"""
The i-th person has weight people[i], and each boat can carry a maximum weight
of limit.

Each boat carries at most 2 people at the same time, provided the sum of the
weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is
guaranteed each person can be carried by a boat.)


Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
"""
class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        start, end = 0, len(people) - 1
        res = 0
        people.sort(reverse=True)
        while start <= end:
            if people[start] + people[end] <= limit:
                end -= 1
            res += 1
            start += 1
        return res

if __name__ == '__main__':
    people1 = [1,2]
    limit1 = 3
    people2 = [3, 2, 2, 1]
    limit2 = 3
    people3 = [3, 5 ,3 , 4]
    limit3 = 5
    people4 = [2, 2]
    limit4 = 6
    print(Solution().numRescueBoats(people1, limit1))
    print(Solution().numRescueBoats(people2, limit2))
    print(Solution().numRescueBoats(people3, limit3))
    print(Solution().numRescueBoats(people4, limit4))
