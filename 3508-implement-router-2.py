from typing import List
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right


class Router:
    '''
    We can use an array/deque to implement the FIFO queue of packets
    We can also use a set to allow us to check for duplicate packet in the current queue
    We can use a hashmap to store the destination and list of timestamps which would be in increasing order.
        - We might need to use binary search to get the qualified range of timestamp

    __init__:
        - Set the max_size constant

    addPacket:
        - concat the fields and use as key to match against the set to check for duplicates
            - if exist, return false
            - else
                - Check if the size exceeds the queue size. If yes, pop the earliest entry
                - Remove the earliest entry from the set
                - Remove the entry from the destination_timestamps
                - Add the packet as an array into the queue
                - Add the key into the set
                - Also, using the destination, append the timestamp into the hashmap of destination_timestamps
                - return true
    forwardPacket:
        - if queue is empty, return empty
        - else
            - pop the earliest entry
            - remove the entry from the set
            - using the destination, search in the destination_timestamps hashmap, then while timestamp in hashmap < entry in the queue, popleft

    getCount:
        - search in the destination_timestamps hashmap, get the list of timestamps.
        - Then we use binary search to search for the startTime as well as endTime and then get the length in between

    '''

    def __init__(self, memoryLimit: int):
        self.max_size = memoryLimit
        self.packets = deque()
        self.curr_packets = set()
        self.destination_timestamps = defaultdict(list)

    def _remove_packet(self) -> List[int]:
        old_source, old_destination, old_timestamp = self.packets.popleft()
        old_key = (old_source, old_destination, old_timestamp)
        self.curr_packets.remove(old_key)
        old_destination_timestamps = self.destination_timestamps[old_destination]
        if old_destination_timestamps and old_destination_timestamps[0] <= old_timestamp:
            old_destination_timestamps.pop(0)

        return [old_source, old_destination, old_timestamp]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.curr_packets:
            return False

        if len(self.packets) == self.max_size:
            self._remove_packet()

        self.packets.append((source, destination, timestamp))
        self.curr_packets.add(key)
        self.destination_timestamps[destination].append(timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []
        return self._remove_packet()

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        curr_destination_timestamps = self.destination_timestamps[destination]
        start_idx = bisect_left(curr_destination_timestamps, startTime)
        end_idx = bisect_right(curr_destination_timestamps, endTime)

        return end_idx - start_idx


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


router = Router(3)
print(f'output: {router.addPacket(1, 4, 90)}, expected: True')
print(f'output: {router.addPacket(2, 5, 90)}, expected: True')
print(f'output: {router.addPacket(1, 4, 90)}, expected: False')
print(f'output: {router.addPacket(3, 5, 95)}, expected: True')
print(f'output: {router.addPacket(4, 5, 105)}, expected: True')
print(f'output: {router.forwardPacket()}, expected: [2,5,90]')
router.addPacket(5, 2, 110)
print(f'output: {router.getCount(5, 100, 110)}, expected: 1')

router = Router(3)
print(f'output: {router.addPacket(1, 4, 6)}, expected: True')
print(f'output: {router.getCount(4, 1, 4)}, expected: 0')

router = Router(2)
print(f'output: {router.addPacket(5, 2, 4)}, expected: True')
print(f'output: {router.addPacket(4, 2, 4)}, expected: True')
print(f'output: {router.getCount(4, 1, 4)}, expected: 0')
