"""
Solution Review: Problem Challenge 1 - Minimum Meeting Rooms (hard)
Given a list of intervals representing the start and end time of ‘N’ meetings,
find the minimum number of rooms required to hold all the meetings.

Example 1:

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
occur in any of the two rooms later.

Example 2:

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

Example 3:

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
hold all the meetings.

Example 4:

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

Here is a visual representation of Example 4:
"""

# mycode
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)
    conflict = []
    min_rooms = 0
    for meeting in meetings:
        while len(conflict) > 0 and meeting.start >= conflict[0].end:
            heappop(conflict)
        heappush(conflict, meeting)
        min_rooms = max(len(conflict), min_rooms)
    return min_rooms


def main():
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))
    )
    print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))
    )


main()


# answer
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)

    minRooms = 0
    minHeap = []
    for meeting in meetings:
        # remove all the meetings that have ended
        while len(minHeap) > 0 and meeting.start >= minHeap[0].end:
            heappop(minHeap)
        # add the current meeting into min_heap
        heappush(minHeap, meeting)
        # all active meetings are in the min_heap, so we need rooms for all of them.
        minRooms = max(minRooms, len(minHeap))
    return minRooms


def main():
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))
    )
    print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))
    )


main()


"""
Time complexity 
The time complexity of the above algorithm is O(N*logN), where ‘N’ is the total number of meetings. T
his is due to the sorting that we did in the beginning. 
Also, while iterating the meetings we might need to poll/offer meeting to the priority queue.
Each of these operations can take O(logN). 
Overall our algorithm will take O(NlogN).

Space complexity 
The space complexity of the above algorithm will be O(N) which is required for sorting. 
Also, in the worst case scenario, we’ll have to insert all the meetings into the Min Heap (when all meetings overlap) which will also take O(N) space. 
The overall space complexity of our algorithm is O(N).
"""


# ps
from heapq import *


def minMeetingRooms(meetings):
    meetings.sort(key=lambda x: x[0])  # Sort meetings by start time
    min_rooms = 0
    min_heap = []
    for meeting in meetings:
        if (
            min_heap and meeting[0] >= min_heap[0]
        ):  # Current meeting overlaps with the earliest ending meeting in the queue
            heappop(min_heap)
        heappush(min_heap, meeting[1])  # Add current meeting's ending time to the queue
        min_rooms = max(min_rooms, len(min_heap))  # Update the minimum number of meeting rooms required
    return min_rooms


"""
Approach:

Sort the meetings by their start time.
Create a priority queue to keep track of the meetings that are currently ongoing.
Iterate through the sorted meetings:
  - If the current meeting overlaps with the earliest ending meeting in the priority queue,
  we need to allocate a new meeting room.
  - Otherwise, we can reuse the meeting room of the earliest ending meeting in the priority queue.
Return the number of meeting rooms required


Complexity:

The time complexity of the above algorithm is O(NlogN), where N is the number of meetings. The sorting of meetings takes O(NlogN) time, and 
iterating through the sorted meetings takes O(N) time. Adding and removing elements from the priority queue takes O(logN) time, and we do this operation N times.
The space complexity of the algorithm is O(N) as we use a priority queue to store the ending times of the meetings. In the worst case, all meetings can overlap, 
and we would need N meeting rooms, hence N elements in the priority queue.
Overall, the algorithm has a reasonable time and space complexity, and it can efficiently solve the problem for large input sizes.
"""
