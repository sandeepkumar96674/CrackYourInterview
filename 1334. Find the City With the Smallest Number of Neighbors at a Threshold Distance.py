class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for src, dst, weight in edges:
            graph[src].append((weight, dst))
            graph[dst].append((weight, src))
        min_idx = -1
        min_count = float('inf')
        for i in range(n):
            dist = [float('inf')] * n
            dist[i] = 0
            q = [(0, i)]
            while q:
                weight, idx = heapq.heappop(q)
                for nb_weight, nb_idx in graph[idx]:
                    new_weight = weight + nb_weight
                    if new_weight < dist[nb_idx] and new_weight <= distanceThreshold:
                        dist[nb_idx] = new_weight
                        heapq.heappush(q, (new_weight, nb_idx))
            count = sum(d < float('inf') for d in dist)
            if count <= min_count:
                min_count = count
                min_idx = i

        return min_idx