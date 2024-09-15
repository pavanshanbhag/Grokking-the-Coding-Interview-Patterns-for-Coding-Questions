"""
Problem Statement
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""


# answer
def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        # we will take all existing subsets and insert the current number in them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and insert the current element to it
            set = subsets[i].copy()
            set.append(currentNumber)
            subsets.append(set)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()


"""
Time complexity 
Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, the time complexity of the above algorithm is O(2^N), 
where ‘N’ is the total number of elements in the input set. This also means that, in the end, we will have a total of O(2^N) subsets.

Space complexity 
All the additional space used by our algorithm is for the output list. Since we will have a total of O(2^N) subsets, 
the space complexity of our algorithm is also O(2^N).

"""


# power set implementation
def get_bit(num, bit):
    temp = 1 << bit
    temp = temp & num
    if temp == 0:
        return 0
    return 1


def find_all_subsets(nums):
    subsets = []

    if not nums:
        return [[]]
    else:
        subsets_count = 2 ** len(nums)
        for i in range(0, subsets_count):
            subset = set()
            for j in range(0, len(nums)):
                if get_bit(i, j) == 1 and nums[j] not in subset:
                    subset.add(nums[j])

            if i == 0:
                subsets.append([])
            else:
                subsets.append(list(subset))
    return subsets
