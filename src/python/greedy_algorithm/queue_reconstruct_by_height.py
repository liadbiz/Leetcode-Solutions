"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
class Solution:
    # 先按照前面的人数升序，然后按照身高升序，
    # 然后依次插入`res`中，在满足每个人k的前提下，应该尽可能的插入到靠后的位置
    # 这样才不会影响之前插入的人的合理性
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        people.sort(key=lambda x: (x[1], x[0]))  
        res = [people[0]]
        for p in people[1:]:
            t = 0
            for i, r in enumerate(res):
                if r[0] >= p[0]:
                    t += 1
                if t > p[1]:
                    res = res[:i] + [p] + res[i:]
                    break
            else:
                res.append(p)
        return res
    # 每个人的位置只取决与比他高的人，所以可以将`people`先按照身高降序排序，然后
    # 按照`k`值升序排序。再依次插入的时候，每个人的位置就是其`k`值，因此已经插入的人
    # 都是比当前的身高要高。
    def reconstructQueue2(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        people.sort(key=lambda (h, k) : (-h, k))
        for p in people:
            res.insert(p[1], p)
        return res

if __name__ == "__main__":
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(Solution().reconstructQueue(people))
    print(Solution().reconstructQueue2(people))
