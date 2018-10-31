"""
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate
wants to make a decision about a change in the Dota2 game. The voting for this
change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right:
A senator can make another senator lose all his rights in this and all the
following rounds.
Announce the victory:
If this senator found the senators who still have rights to vote are all from
the same party, he can announce the victory and make the decision about the
change in the game.
Given a string representing each senator's party belonging. The character 'R'
and 'D' represent the Radiant party and the Dire party respectively. Then if
there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in
the given order. This procedure will last until the end of voting. All the
senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his
own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

Example 1:
Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next
senator's right in the round 1.
And the second senator can't exercise any rights any more since his right has
been banned.
And in the round 2, the first senator can just announce the victory since he
is the only guy in the senate who can vote.
Example 2:
Input: "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in the round 1. 
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
Note:
    The length of the given string will in the range [1, 10,000].
"""
class Solution:
    # 思路：
    # 对于每一次投票过程(round)，遍历senate，维护一个变量dn，表示需要被ban吊的
    # 字母的数量，对于每一个被遍历到的字母，如果需要被ban掉，那么就ban掉它，dn-1.
    # 知道某一投票过程没有ban掉一个字母，说明投票结束。
    # 第一个函数是我的实现，第二个函数是简化实现，思路是一致的。
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        ban = [0 for  i in range(len(senate))]
        dn = 0
        crt = ''
        flag = True
        while flag:
            i = 0
            flag = False
            while i < len(senate):
                if not ban[i]:
                    if dn == 0:
                        crt = senate[i]
                        dn += 1
                    elif crt == senate[i]:
                        dn += 1
                    elif crt != senate[i]:
                        flag = True
                        ban[i] = 1
                        dn -=1
                i += 1
        return ['Radiant' if senate[i] == 'R' else 'Dire' for i in range(len(ban)) if ban[i] == 0][0]
        # for i in range(len(ban)):
        #     if ban[i] == 0:
        #         return 'Radiant' if senate[i] == 'R' else 'Dire'

    def predictPartyVictory2(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        delta = 0
        while len(set(senate)) > 1:
            nsenate = ''
            for s in senate:
                if s == 'R':
                    if delta >= 0: nsenate += 'R'
                    delta += 1
                else:
                    if delta <= 0: nsenate += 'D'
                    delta -= 1
            senate = nsenate
        return {'D' : 'Dire', 'R' : 'Radiant'}[senate[0]]

if __name__ == '__main__':
    senate1 = "RD"
    senate2 = "RDD"
    senate3 = "DDRRR"
    senate4 = "RRR"
    print(Solution().predictPartyVictory(senate1))
    print(Solution().predictPartyVictory(senate2))
    print(Solution().predictPartyVictory(senate3))
    print(Solution().predictPartyVictory(senate4))

