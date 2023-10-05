from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(airport: str) -> None:
            while graph[airport]:
                dfs(graph[airport].pop(0))
            itinerary.append(airport)

        # Create a map from departure airport to arrival airport.
        graph = defaultdict(list)
        for start, end in sorted(tickets):
            graph[start].append(end)

        itinerary = []
        dfs("JFK")

        return itinerary[::-1]
