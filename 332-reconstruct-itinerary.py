from typing import List
from collections import defaultdict

class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    '''
    first we need to build the graph for this using adjacency list
    we also need to return the itinerary that has the smallest lexical order if there are multiple itineraries
    We can sort the adj list's values so that when we run the DFS, we go through based on lexical order
    Another way is to sort the tickets' 2nd value first so when we add the tickets into the list, they are already sorted
    '''
    graph = defaultdict(list)

    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    itinerary = []

    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        itinerary.append(airport)

    dfs("JFK")

    return itinerary[::-1]

sol = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
output = sol.findItinerary(tickets)
print(f'tickets: {tickets}\noutput: {output}')