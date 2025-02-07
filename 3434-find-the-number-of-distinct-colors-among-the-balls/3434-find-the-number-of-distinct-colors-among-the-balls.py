class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:


        res = []
        ball_to_color = {}
        color_to_ball = defaultdict(set)
        ans = 0
        for ball, color in queries:
            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                color_to_ball[old_color].remove(ball)
                if not color_to_ball[old_color]:
                    del(color_to_ball[old_color])
                    ans -= 1
            if color not in color_to_ball:
                ans += 1
            color_to_ball[color].add(ball)
            ball_to_color[ball] = color
            res.append(ans)

        return res        