import bisect
class MyCalendarThree:

    def __init__(self):
        self.starts = []
        self.ends = []
        self.max_intersection = 0
        self.steps = 0

    def book(self, start_time: int, end_time: int) -> int:
        
        already_stoped = bisect.bisect(self.ends, start_time)
        already_started = bisect.bisect(self.starts, start_time)
        running = already_started - already_stoped + 1
        self.max_intersection = max(self.max_intersection, running)
        while (already_stoped < self.steps and already_started < self.steps and
                (end_time > self.ends[already_stoped] or
                 end_time > self.starts[already_started])):
            if self.ends[already_stoped] <= self.starts[already_started]:
                running -= 1
                already_stoped += 1
            else:
                running += 1
                self.max_intersection = max(self.max_intersection, running)
                already_started += 1

        bisect.insort(self.starts, start_time)
        bisect.insort(self.ends, end_time)
        self.steps += 1

        

        return self.max_intersection

m = MyCalendarThree()

steps = [10,20],[50,60],[10,40],[5,15],[5,10],[25,55]
# [24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]
for s, e in steps:
    print(m.book(s, e))