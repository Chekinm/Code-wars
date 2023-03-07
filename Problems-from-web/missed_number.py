from random import randint


def generate_problem(n=100, k=1):
    ls = [i for i in range(1, n + 1)]
    lst_to_solve = []
    while len(ls) > k:
        lst_to_solve.append(ls.pop(randint(0, len(ls) - 1)))  # get random element from ls list and append in to the
                                                              # list. i the end we wil have shuffled array and
                                                              # residual elements in the ls list.
    return lst_to_solve, ls

def find_missed_numbers_in_array(arr, k):
    """Function receives a shuffled array (arr) of numbers from 1 to n, with k numbers deleted.
    It finds and returns a list of k missed numbers as a list
    """
    for i in range(k):
        arr.append(0)
    for i in range(len(arr)):
        while arr[i] != 0 and arr[i] != i + 1:   # generally we made a cunt sort like procedure.
                                                 # it will be zeros on the place where should stay missed numbers
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
    return [i + 1 for i in range(len(arr)) if arr[i] == 0]   # we just return indexes of zero element


n = 1000
k = 2
a = generate_problem(n, k)

list_to_solve = a[0]
missed = a[1]

print(find_missed_numbers_in_array(list_to_solve, k))

print(find_missed_numbers_in_array(list_to_solve, k) == missed)
