# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:40:13 2023

@author: Lenovo
"""

def bfs(start, target):
    head = 0
    nodes.append((start, -1, -1))
    visited.add(str(start))
    while head < len(nodes):
        state, _, _ = nodes[head]
        if state == target:
            return head
        z = state.index(0)
        x, y = z // 3, z % 3 
        for i in range(4): 
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                state_next = state.copy()
                state_next[z], state_next[3*nx+ny] = state_next[3*nx+ny], state_next[z]
                if str(state_next) not in visited:
                    visited.add(str(state_next))
                    nodes.append((state_next, head, i))
        head += 1
    return -1

start_n = input().replace("x","0")
start = [int(_) for _ in start_n.split()]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dir = ['r', 'l', 'u', 'd']
nodes = []
visited = set()
end = list(range(1, 9)) + [0]
end_node = bfs(start, end)
if end_node != -1:
    path = []
    while end_node != -1:
        path.append(dir[nodes[end_node][2]])
        end_node = nodes[end_node][1]
    print(''.join(path[::-1]))
else:
    print("unsolvable")