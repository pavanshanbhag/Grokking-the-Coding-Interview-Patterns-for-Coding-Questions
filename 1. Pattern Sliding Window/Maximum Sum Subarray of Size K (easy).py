"""
Problem Statement #
Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size 'k'.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""


# answer
def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0  # alternatively max_sum = float("-inf") to handle negative numbers
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()


"""
Time Complexity
The time complexity of the above algorithm will be O(N).

Space Complexity
The algorithm runs in constant space O(1).

# Edge Case 1: empty array
print(max_sum_subarray([], 3))  # Output: None

# Edge Case 2: k is larger than the array length
print(max_sum_subarray([2, 3, 4, 1, 5], 7))  # Output: None

# Edge Case 3: all elements are negative
print(max_sum_subarray([-2, -3, -4, -1, -5], 2))  # Output: -1

# Edge Case 4: one element in the array
print(max_sum_subarray([3], 1))  # Output: 3

# Edge Case 5: array has multiple subarrays with the same maximum sum
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 2))  # Output: 6

# Edge Case 6: array has only one subarray of size k
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 6))  # Output: 15

# Edge Case 7: array has all elements equal
print(max_sum_subarray([5, 5, 5, 5], 3))  # Output: 15
"""


def max_sum_subarray(arr, k):
    max_sum = float("-inf")
    window_start, window_sum = 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element
        # Shrink the window if we've reached the window size 'k'
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum
