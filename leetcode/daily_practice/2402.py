from collections import defaultdict, deque
from heapq import heapify, heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:


        start = min(meetings)[0]
        

        occupied = defaultdict(list) # endtime, room numbers list, 
        occupied_heap = []
        heapify(occupied_heap)
        heapify(meetings)
        free_room = list(range(n))
        
        heapify(free_room)
        count_booking = defaultdict(int)
        
        while True:
            try:
                next_meeting = heappop(meetings)
                start = next_meeting[0]
                duration = next_meeting[1] - next_meeting[0]
            except IndexError:
                break

            while occupied_heap and occupied_heap[0][0] <= start:
                room = heappop(occupied_heap)
                heappush(free_room, room[1])

            if not free_room:
                room = heappop(occupied_heap)
                start = room[0]
                heappush(free_room, room[1])
            
            room = heappop(free_room)
            print(next_meeting, duration)
            heappush(occupied_heap, (start + duration, room))
            count_booking[room] += 1
            
        

        return max(count_booking.items(), key=lambda x:x[1])[0]