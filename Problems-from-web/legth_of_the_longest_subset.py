import random
import time

from typing import Iterable
from collections import OrderedDict


# variants with memory o(1) with dictinary of indexes work for any numbers
#
#  with ordered dict and enumerate and trick 
# with addind last meet index to the dict.
# the is the fastest  variant

def lenght_of_longest_subset(input_objects: Iterable, k: int) -> int:
    """return the length of the subset of input_objects  which contain maximum 
       k different object"""
    length = 0
    right_most_indexes = OrderedDict()
    index_left = -1

    for index, obj in enumerate(input_objects):
        if obj in right_most_indexes:
            right_most_indexes.pop(obj)
        right_most_indexes[obj] = index
        if len(right_most_indexes) <= k:
            length = max(length, index - index_left)
        else:
            elem_to_delete = next(iter(right_most_indexes.keys()))
            index_left = right_most_indexes[elem_to_delete]
            right_most_indexes.pop(elem_to_delete)

    return length


# with standrt dict and finding min of the indexes of the number to cut
# min takes  o(n) *o(k) and if k is big it slow down the solition.
def lenght_of_longest_subset1(input_objects: Iterable, k: int) -> int:
    """return the length of the subset of input_objects  which contain maximum 
    k different object"""
    length = 0
    right_most_indexes = {}
    index_left = -1

    for index, obj in enumerate(input_objects):
        right_most_indexes[obj] = index
        if len(right_most_indexes) <= k:
            length = max(length, index - index_left)
        else:
            elem_to_delete = min(right_most_indexes,
                                 key=right_most_indexes.get)
            index_left = right_most_indexes[elem_to_delete]
            right_most_indexes.pop(elem_to_delete)
    return length

#  variant with additional set more memory O(n)


def lenght_of_longest_subset5(input_objects, k=1):
    """return the length of the subset of input_objects
       which contain maximum k different object"""
    length = 0
    current_set = []  # list - hold current subset
    current_set_unique = set()
    # set - hold current set of unique elements in current set

    for obj in input_objects:
        current_set.append(obj)
        if obj not in current_set_unique:
            current_set_unique.add(obj)
        if len(current_set_unique) <= k:
            length = max(length, len(current_set))

        else:
            """we have  k+1 different elements in current_set,
            so we need to eject elements from it.
            will do it from left side one by one until current_set will 
            conatain exaclty k different elements"""
            while len(set(current_set)) > k:
                current_set.pop(0)
            current_set_unique = set(current_set) 
            # replace current_set_unique with new set of unique elements

    return length

# debug staff

start = time.process_time()
print(lenght_of_longest_subset((random.randint(0,6) for i in range(100000)),5))

end = time.process_time()
print(end, )
#
# start = 0
# start = time.process_time()
# print(lenght_of_longest_subset2((random.randint(0, 40000) for i in range(1000000)),39999))
# print(lenght_of_longest_subset1('abcbcecbcbcbdddddde', 3))
# end=time.process_time()
# print(end, 'len() + Ordered dict')
#
# start = 0
# start = time.process_time()
# print(lenght_of_longest_subset3((random.randint(0, 40000) for i in range(10000000)),39999))
# print(lenght_of_longest_subset1('abcbcecbcbcbdddddde', 3))
# end=time.process_time()
# print(end, '2 count + standart dict')

# # #
# # #
assert lenght_of_longest_subset('', 3) == 0
assert lenght_of_longest_subset(['None','None','a','b'],2) == 3
assert lenght_of_longest_subset('abcbcecbcbcbdddddde', 3) == 12
assert lenght_of_longest_subset('abbabbcccbbcb', 2) == 9
assert lenght_of_longest_subset('abbabbcccbbcb', 4) == 13
assert lenght_of_longest_subset('aaaaaaaaaaaaaaaaaaa', 2) == 19
assert lenght_of_longest_subset('baaaaaaaaaaaaaaaaaaab', 2) == 21
assert lenght_of_longest_subset('cbbcbbdbc', 3) == 9
assert lenght_of_longest_subset('ababcacdaddbbdb', 2) == 6
assert lenght_of_longest_subset('abcdebcdecdedeea', 4) == 14
assert lenght_of_longest_subset('aaaabbbbbccccccdddddddaaaaaaaaa', 1) == 9
assert lenght_of_longest_subset('aaaabbbbbccccccdddddddaaaaaaaaa', 2) == 16
assert lenght_of_longest_subset('abbcbbdbc', 3) == 8
assert lenght_of_longest_subset('ababcacdaddbbdb', 3) == 8
assert lenght_of_longest_subset('cabcaccbbddbcbcdbcbdbcdd', 3) == 19
assert lenght_of_longest_subset('cabcaccbbaddabbabeabeabeabbbeeabcd', 3) == 20
assert lenght_of_longest_subset([i for i in range (100)], 100) == 100