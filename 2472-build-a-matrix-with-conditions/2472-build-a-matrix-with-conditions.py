class Solution:

    def buildGraph(self, k, condition):
        graph = {}
        indeg = [0]*k
        for root, child in condition:
            if root not in graph:
                graph[root] = []
            graph[root].append(child)
            indeg[child-1] += 1
        return indeg, graph

    def traverseGraph(self, k, graph, indeg):
        q = deque([i+1 for i in range(k) if indeg[i] == 0])
        index = {}
        level = 0
        while q:
            node = q.popleft()
            index[node] = level
            for child in graph.get(node, []):
                indeg[child-1] -= 1
                if indeg[child-1] == 0:
                    q.append(child)
            level += 1
        return -1 if level != k else index

    def formMatrix(self, k, row_index, col_index):
        matrix = [[0]*k for _ in range(k)]
        for i in range(1, k+1):
            row, col = row_index[i], col_index[i]
            matrix[row][col] = i
        return matrix

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        row_indeg, row_graph = self.buildGraph(k, rowConditions)
        col_indeg, col_graph = self.buildGraph(k, colConditions)
        row_index = self.traverseGraph(k, row_graph, row_indeg)
        if row_index == -1:
            return []
        col_index = self.traverseGraph(k, col_graph, col_indeg)
        if col_index == -1:
            return []
        return self.formMatrix(k, row_index, col_index)
        