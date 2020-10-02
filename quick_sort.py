# helper function conceptial partitioning
def partition(data):
    # takes in a single kist and partitions it into 3 lists left, pivot, right
    # create 2 empty lists (left, right)
    left = []
    right = []
    # create a pivot list containing the first element of the data
    pivot = data[0]
    
    # for each value in our data starting at index 1:
    for value in data[1:]:
        # check if value is less than or equal to the pivot
        if value <= pivot:
            # append value to the left list
            left.append(value)
        # otherwise ( the value must be greater than the pivot )
        else:
            # append our value to the right list
            right.append(value)
            
            
    # returns the tupple of (left, pivot, right)
    return left, pivot, right

# quick sort that uses the partitioned data
def quicksort(data):
    # base case if the data is an empty list return an empty list
    if data == []:
        return data
    
    # partition the data into 3 variables (left, pivot, right)
    left, pivot, right = partition(data)
    # recirsive call to quicksort using the left
    # recursive call to quicksort using the right
    
    # return the concatenation quicksort of lhs + pivot + rhs
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))



# def numberSigningSum(n):
#     new_n = [int(a) for a in str(n)]
#     value = 0
#     count = 0
#     steps = ""
#     for i in new_n:
#         if count % 2 == 0:
#             value += i
#             steps += " + " + str(i)
#         else:
#             value -= i
#             steps += " - " + str(i)
#         count += 1
#     print(f"{steps[3:]} = {value}")
#     return new_n


# # Test case
# n = 52134
# print(numberSigningSum(n))
# # should return 5 - 2 + 1 - 3 + 4 = 5


# # Test case 2
# n = 54481
# print(numberSigningSum(n))
# # should return 5 - 4 + 4 - 8 + 1 = -2
    
