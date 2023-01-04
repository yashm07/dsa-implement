from collections import defaultdict, deque
from typing import List

class Graph:
    def __init__(self):
        """
        Using adjacency list implementation (without linked list, just dict and list to simplify implementation)

        For matrix implementation, create nxn matrix, 1 represents edge, 0 represents no edge (unweighted graph)
        """
        self.graph = defaultdict(list)
        
    def add_edge(self, u: int, v: int) -> None:
        """
        Add edge to adjacency list

        O(1) time complexity, O(1) memory

        Args:
            u (int): first vertice
            v (int): second vertice
        """
        self.graph[u].append(v)

        # takes care of situation where 5->6 occurs, but 6 has degree of 0
        if not v in self.graph:
            self.graph[v]
    
    def bfs(self, start: int) -> None:
        """
        BFS, O(n+m) time complexity in adjacency list, O(n^2) in matrix

        Args:
            start (int): starting node
        """
        visited = []
        q = []

        visited.append(start)
        q.append(start)

        while q:
            node = q.pop(0)

            for neighbour in self.graph[node]:
                # check if node already visited
                if not neighbour in visited:
                    visited.append(neighbour)
                    q.append(neighbour)

    def dfs_recursive(self, start: int) -> None:
        """
        DFS, O(n+m) time complexity in adjacency list, O(n^2) in matrix

        Args:
            start (int): starting node
        """
        visited = []
        self.__dfs(start, visited)
        print(visited)
    
    def __dfs(self, start: int, visited: List[int]) -> None:
        """
        Private method for recursive dfs

        Args:
            start (int): starting node
            visited (list): visited nodes list
        """
        visited.append(start)
        for neighbour in self.graph[start]:
            if not neighbour in visited:
                self.__dfs(neighbour, visited)
    
    def dfs_iterative(self, start: int) -> None:
        """
        Iterative dfs

        Args:
            start (int): starting node
        """
        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            node = stack.pop()
            print(node)
            for neighbour in self.graph[node]:
                if not neighbour in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)
        
    def __dfs_top_sort(self, start: int, visited: List[int], s: List[int]) -> None:
        """
        Private method for recursive topological sort. Same as regular dfs, accept track reverse order of dfs

        Args:
            start (int): starting node
            visited (List[int]): visited nodes
            s (List[int]): output of sort, stack
        """
        visited.append(start)
        for neighbour in self.graph[start]:
            if not neighbour in visited:
                self.__dfs_top_sort(neighbour, visited, s)
        
        s.appendleft(start)
    
    def top_sort(self) -> List[int]:
        """
        Topological sort, runtime same as dfs

        Returns:
            List[int]: output of sort, stack
        """
        visited = []
        s = deque()
        
        for key, _ in self.graph.items():
            if not key in visited:
                self.__dfs_top_sort(key, visited, s)
        
        return s        