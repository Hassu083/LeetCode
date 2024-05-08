class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        toi = {}
        n = len(score) 
        for i in range(n):
            toi[score[i]] = i
        score.sort(reverse=True) 
        ans = [""]*n
        for i in range(n):
            if i==0:
                ans[toi[score[i]]]="Gold Medal"
            elif i==1:
                ans[toi[score[i]]]="Silver Medal"
            elif i==2:
                ans[toi[score[i]]]="Bronze Medal"
            else:
                ans[toi[score[i]]]=str(i+1) 
        return ans