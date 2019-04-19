'''
Zachary Dulac, Trung Nguyen, Abby Tse
Dr. Zhang
CISC 4080
Adding to N
'''

'''
returns either and empty list or list of first possible combination of elements
in the vector/given list using brute force
@param vector: given list of values
@param val: value of the desired sum
'''
def brute_force(vector, val):
    # base case if the sum is 0, then no elements in the list is needed
    if val == 0:
        return []
    # base case if the length of the given list is empty and the value is not 0
    if len(vector) == 0 and val != 0:
        return []

    ans_set = [] # list for the answer set
    temp_set = [[]] # temporary list to hold the power set

    # calculates the power set or all possible subsets of the given set in list and appends to temp_set
    for elem in vector:
        for subset in temp_set:
            temp_set = temp_set + [list(subset) + [elem]]

    # iterates through the subsets and if the sum of the subset is equivalent to the val/sum then assign that subset to ans_set
    for subset in temp_set:
        if sum(subset) == val:
            ans_set = subset
            break

    return ans_set

'''
returns either and empty list or list of first possible combination of elements
in the vector/given list using memoization/dynamic programming
'''
def dynamic(vector, val):
    # base case if the sum is 0, then no elements in the list is needed
    if val == 0:
        return []
    # base case if the length of the given list is empty and the value is not 0
    if len(vector) == 0 and val != 0:
        return []


    ans_set = []  # list for the answer set
    # create 2D array initializing every value to False
    # row = values of list
    # col = 0 to sum+1
    subset = [[False for i in range(val + 1)] for j in range(len(vector))]

    # initializes column 0 to be True
    for i in range(len(vector)):
        subset[i][0] = True

    # algorithm to calculate the subset using the 2D array and assigning True to possible values
    for i in range(len(vector)):
        for j in range(1, (val + 1)):
            # assigns True if the column == row
            if j == vector[i]:
                subset[i][j] = True
            if i != 0:
                # assigns True if the previous row had True in the same column
                if subset[i-1][j]:
                    subset[i][j] = True
                    try:
                        # assigns True to the summation of the column index with True values and current row index
                        subset[i][vector[i] + j] = True
                        # logic to check if the desired val/sum is reached thus, beginning to scan through the 2D matrix for the subset values to get the val
                        if subset[i][val]:
                            ans_set.append(vector[i])  # appends the value of the current row to the answer set
                            val = val - vector[i]  # deducts the appended value from the val/sum
                            i = i-1 #  decrements i and goes to the previous row

                            # checks to see when the last true in the column with val is found
                            while(val != 0):
                                # decrements the row if the previous column is still true
                                if subset[i-1][val]:
                                    i = i-1
                                else:
                                    # appends the value to the answer set and deducts the appended value from val/sum
                                    ans_set.append(vector[i])
                                    val = val - vector[i]
                    # catch/except if index is out of bound
                    except:
                        continue

    # print_subset(subset, list, sum)

    return ans_set

'''
prints the 2D matrix of booleans
'''
def print_subset(subset, list, sum):
    for i in range(len(list)):
        for j in range(sum+1):
            print(subset[i][j], end=" ")
        print('\n')

def main():
    test_set = [[2,3,7,8,10], [3,34,4,12,5,2], [1,2,3,7,8], [100, 200, 300], [1,2,3]]
    test_sum = [11, 9, 11, 0, 10]

    i = 0
    for list in test_set:
        print("List: " + str(list))
        bf_subset = brute_force(list, test_sum[i])
        print("Subset of sum using brute force: " + str(bf_subset))

        dm_subset = dynamic(list, test_sum[i])
        print("Subset of sum using dynamic programming: " + str(dm_subset) + '\n')

        i = i + 1

if __name__ == "__main__":
    main()
