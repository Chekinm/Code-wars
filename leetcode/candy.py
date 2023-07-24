# arr = [1,2,3, 1]

# left = 0
# end = len(arr)


# def candy(left, end, total=0):
#     # if only 1 elem
#     if end - left == 1:
#         return total + 1
#     # we have at least 2
#     if arr[left + 1] > arr[left]:
#         direction = 1
#     elif arr[left + 1] < arr[left]:
#         direction =  -1
#     else:
#         return candy(left + 1, end, total + 1)
#     total += 2

#     count = 2
#     while left + count < end:
#         direction_new = arr[left + count] - arr[left + count -1]
#         if direction_new == 0:
#             return 

        
#         elif direction_new == 0

        
#         elif 
    










# def candy(ratings):
#     # if we have only 1 elem in substring
#     if len(ratings) < 2:
#         return len(ratings)
#     # we have at least 2 elem
#     N = len(ratings)
#     right = 1
#     left = 0
#     total = 1
#     direction = 0
      
#     while right < N:
#         # check current state

#         while (ratings[right] - ratings[right - 1]) * 


#         if ratings[right] == ratings[right - 1]:
#             # flat
#             direction_new = 0
#         elif ratings[right] < ratings[right - 1]:
#             # increasing
#             direction_new = - 1
#         else:
#             # decreasing
#             direction_new = 1

#         if direction_new == direction

#         if direction_new != direction:
#             # need to handle previouse right - left elements
#             print('changedir', right, left, direction, direction_new)
#             if direction_new != 0:
                
#                 direction = direction_new
                

#             elif direction_new == 1:

                



#         else:  # state rematin 
#             if direction: # flat
#                 total += 1
#                 left += 1
#                 right += 1



#         right += 1

#     n = right - left
#     if direction:
#         total = total + (n * (n + 1)) // 2
#     else:
#         total += n
#     return total


# print(candy([1, 2, 2, 2]))
def derivative (m1,m2):
    if m2 > m1:
        return 1
    elif m2 < m1:
        return -1
    return 0


def candy(arr):
    if len(arr) < 2:
        return len(arr)
    previouse_direction = derivative(arr[0],arr[1])    
    # create a dict with monotonic segments
    segments = []
    prev_ind = 0
    ind = 1
    while ind < len(arr) - 1:
        current_direction = derivative(arr[ind], arr[ind+1])          
        if current_direction != previouse_direction:
            segments.append((previouse_direction, prev_ind, ind))
            prev_ind = ind
            previouse_direction = current_direction
        ind += 1
    # append last segment
    segments.append((previouse_direction, prev_ind, ind))
    print(segments)
    # for segment in segments:
 
    
    

candy([1,2,10,9,8,7,6,5,4,4,4,4,3,2,1,1,1])




