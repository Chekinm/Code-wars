from collections import deque

# In mathematics, the symbols Δ and d are often used to denote the difference between two values.
# Similarly, differentiation takes the ratio of changes (ie. dy/dx) for a linear relationship.
# This method can be applied multiple times to create multiple 'levels' of rates of change.
# (A common example is x (position) -> v (velocity) -> a (acceleration)).
# Today we will be creating a similar concept.
# Our function delta will take a sequence of values and a positive integer level,
# and return a sequence with the 'differences' of the original values.
# (Differences here means strictly b - a, eg. [1, 3, 2] => [2, -1])
# The argument level is the 'level' of difference, for example
# acceleration is the 2nd 'level' of difference from position.
# The specific encoding of input and output lists is specified below.
# The example below shows three different 'levels' of the same input.
# input = [1, 2, 4, 7, 11, 16, 22]
# list(delta(input, 1)) # [1, 2, 3, 4, 5, 6]
# list(delta(input, 2)) # [1, 1, 1, 1, 1]
# list(delta(input, 3)) # [0, 0, 0, 0]


# variant with 'for' Delta Generators

def delta_with_for(values, n):
    deq = deque()
    for val in values:
        if len(deq) > n:
            yield deq.popleft()
        deq.append(val)
        for i in range(len(deq)-2, -1, -1):
            deq[i] = deq[i+1] - deq[i]
    yield deq.popleft()

# variant with 'while'


def delta_with_while(values, n):

    values_iter = iter(values)
    deq = deque()
    flag = True
    while flag:
        try:
            while len(deq) < n + 1:
                deq.append(next(values_iter))
                i = len(deq) - 2
                while i >= 0:
                    deq[i] = deq[i+1] - deq[i]
                    i -= 1
            yield deq.popleft()
        except StopIteration:
            flag = False


print(list(delta_with_for([1, 2, 3, 4, 5, 6], 1)))
print(list(delta_with_while([1, 2, 3, 4, 5, 6], 1)))
