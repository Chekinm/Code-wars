from collections import deque

# variant with 'for' 

def delta_with_for(values, n):
    deq = deque()
    for val in values:
        if len(deq) > n:
            yield deq.popleft()
        deq.append(val)
        for i in range(len(deq)-2,-1,-1):
            deq[i]=deq[i+1] - deq[i]
    yield deq.popleft()
            
def delta_with_while(values, n):

    values_iter = iter(values)
    deq = deque()
    flag = True
    while flag:
        try:
            while len(deq) < n + 1:
                deq.append(next(values_iter))
                i = len(deq) - 2
                while i >=0:
                    deq[i] = deq[i+1] - deq[i] 
                    i -= 1
            yield deq.popleft()
        except StopIteration as e:
            flag = False

print(list(delta_with_for([1,2,3,4,5,6], 1)))
print(list(delta_with_while([1,2,3,4,5,6], 1)))