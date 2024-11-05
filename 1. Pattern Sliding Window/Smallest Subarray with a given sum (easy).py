"""
Problem Statement
Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray whose
sum is greater than or equal to 'S'. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Example 2:

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""
# answer


def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = float("inf")
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]  # add the next element
        # shrink the window as small as possible until the 'window_sum' is smaller than 's'
        while window_sum >= s:
            # Edge case when all the values are > target
            # if window_end - window_start == 0:
            # return 1
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    # Edge case
    if min_length == float("inf"):
        return 0
    return min_length


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()


"""
Time Complexity
The time complexity of the above algorithm will be O(N). 
The outer for loop runs for all elements and the inner while loop processes each element only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).

Space Complexity
The algorithm runs in constant space O(1).

Edge Cases
1. If the input array is empty, the function should return 0.
2. If all the elements in the array are larger than or equal to the target sum 'S',
the function should return 1.
3. If no contiguous subarray with a sum greater than or equal to 'S' exists, the funcction should return 0.
"""


# ps
def smallest_subarray_with_given_sum_ps(arr, S):
    window_start, window_sum = 0, 0
    min_length = float("inf")
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element
        # Shrink the window as small as possible until the 'window_sum' is smaller than 'S'
        while window_sum >= S:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    return min_length if min_length != float("inf") else 0
