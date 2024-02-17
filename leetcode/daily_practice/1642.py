from heapq import heapify, heappop, heappush, nlargest
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        ladders_gap = []
        gap_count = 0
        for i in range(1, len(heights)):
            gap = heights[i] - heights[i - 1]
            if gap > 0:
                gap_count += 1
                if gap_count <= ladders:
                    heappush(ladders_gap, gap)
                elif gap > ladders_gap[0]:
                    bricks -= heappop(ladders_gap)
                    heappush(ladders_gap, gap)
                else:
                    bricks -= gap

                if bricks < 0:
                    return i - 1
                
        return len(heights) - 1



        
        return last

                


s = Solution()
print(s.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))
# assert s.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) == 7, "should be equal 7" 