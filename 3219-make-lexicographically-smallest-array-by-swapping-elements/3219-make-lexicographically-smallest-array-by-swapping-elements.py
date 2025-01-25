class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        

        n = len(nums)
        sorted_nums = sorted(nums)

        # form windows
        i = 0
        windows = []
        while i < n:
            j = i
            while j+1 < n and sorted_nums[j+1]-sorted_nums[j] <= limit:
                j += 1
            windows.append([sorted_nums[i],sorted_nums[j],i])
            i = j + 1
        
        # search within windows
        def searchInWindows(num):
            left, right = 0, len(windows)-1
            while left <= right:
                mid = (left+right)>>1
                window = windows[mid]
                if window[0] <= num <= window[1]:
                    return mid
                elif window[0] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            # if code returns -1 means some error need to be resolved
            return -1
        
        # form result to return 
        ans = []
        for num in nums:
            idx = searchInWindows(num)
            index_sorted_nums = windows[idx][2]
            windows[idx][2] = index_sorted_nums + 1
            ans.append(sorted_nums[index_sorted_nums])

        return ans