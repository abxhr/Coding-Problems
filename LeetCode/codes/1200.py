# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr = sorted(arr)
        minimum = arr[-1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]<minimum:
                minimum=arr[i]-arr[i-1]
        for j in range(0,len(arr)-1):
            if arr[j+1] - arr[j] == minimum:
                ans.append([arr[j],arr[j+1]])
        return ans
