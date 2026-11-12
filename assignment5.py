# 1. Find the second-largest unique element in an array without using sort() or max().
# arr = [10, 20, 40, 30, 40]

# largest = arr[0]
# second = 0

# for i in arr:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i

# print("Second largest:", second)

# 2.Find all pairs in an array whose sum equals a given target.
# arr = [2, 4, 3, 5, 7, 8, 1]
# target = 9

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(arr[i], arr[j])

# 3. Move all zeros to the end of an array without changing the order of other elements.
# arr = [0, 1, 0, 3, 12]

# new = []

# for i in arr:
#     if i != 0:
#         new.append(i)

# for i in arr:
#     if i == 0:
#         new.append(i)

# print(new)

# 4. Find the missing number from an array containing numbers from 1 to N.
# arr = [1, 2, 4, 5, 6]

# n = 6

# total = n * (n + 1) // 2

# for i in arr:
#     total = total - i

# print("Missing number:", total)

# 5.Find all duplicate elements in a list without using nested loops.
# arr = [1, 2, 3, 2, 4, 5, 3, 6]

# duplicates = []

# for i in arr:
#     if arr.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)

# print("Duplicate elements:", duplicates)

# 6.Find the first non-repeating character in a string.
# s = "aabbcde"

# for i in s:
#     if s.count(i) == 1:
#         print("First non-repeating character:", i)
#         break

# 7.. Check whether two strings are anagrams without using sorted().
# s1 = "listen"
# s2 = "silent"

# if len(s1) == len(s2):
#     for i in s1:
#         if s1.count(i) != s2.count(i):
#             print("Not Anagram")
#             break
#     else:
#         print("Anagram")
# else:
#     print("Not Anagram")

# 8. Merge two sorted arrays without using sort().
# a = [1, 3, 5, 7]
# b = [2, 4, 6, 8]

# c = []

# i = 0
# j = 0

# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
#     else:
#         c.append(b[j])
#         j += 1

# c.extend(a[i:])
# c.extend(b[j:])
# print(c)

# 9.Rotate an array to the right by K positions.
# arr = [1, 2, 3, 4, 5]
# k = 2

# k = k % len(arr)

# new = arr[-k:] + arr[:-k]

# print(new)

# 10. Find the intersection of two arrays, including duplicate occurrences.
# a = [1, 2, 2, 3, 4]
# b = [2, 2, 3, 5]

# c = []

# for i in a:
#     if i in b:
#         c.append(i)
#         b.remove(i)

# print("Intersection:", c)

# 11.Find the maximum sum of a contiguous subarray.

# arr = [1, 1, 2, 4, 0, 2, 1, 7, 4]

# current = arr[0]
# maximum = arr[0]

# for i in arr[1:]:
#     current = max(i, current + i)

#     if current > maximum:
#         maximum = current

# print("Maximum sum:", maximum)

# 12. Find the longest substring without repeating characters.
# s = "abcabcbb"

# longest = ""

# for i in range(len(s)):
#     temp = ""

#     for j in range(i, len(s)):
#         if s[j] not in temp:
#             temp = temp + s[j]
#         else:
#             break

#     if len(temp) > len(longest):
#         longest = temp

# print("Longest substring:", longest)
# print("Length:", len(longest))

# 13.. Find the longest common prefix among multiple strings.
# arr = ["flower", "flow", "flight"]

# prefix = arr[0]

# for i in arr:
#     while not i.startswith(prefix):
#         prefix = prefix[:-1]

# print("Longest common prefix:", prefix)

# 14.Group a list of strings into anagram groups.
# arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

# groups = []

# for i in arr:
#     found = False

#     for j in groups:
#         if len(i) == len(j[0]):
#             if all(i.count(ch) == j[0].count(ch) for ch in i):
#                 j.append(i)
#                 found = True
#                 break

#     if not found:
#         groups.append([i])

# print(groups)

# 15.Find the Kth largest element in an unsorted array.
# arr = [3, 2, 1, 5, 6, 4]
# k = 2

# arr.sort(reverse=True)

# print("Kth largest element:", arr[k-1])

# 16.Check whether a given string contains balanced parentheses using a stack
# s = "{[()]}"

# stack = []

# for i in s:
#     if i in "({[":
#         stack.append(i)

#     elif i in ")}]":
#         if len(stack) == 0:
#             print("Not Balanced")
#             break

#         stack.pop()

# else:
#     if len(stack) == 0:
#         print("Balanced")
#     else:
#         print("Not Balanced")

# 17. Find all subarrays whose sum equals a given target.
# arr = [1, 2, 3, 4, 2]
# target = 5

# for i in range(len(arr)):
#     total = 0

#     for j in range(i, len(arr)):
#         total = total + arr[j]

#         if total == target:
            # print(arr[i:j+1])

# 18. Merge overlapping intervals in a list.
# arr = [[1, 3], [2, 6], [8, 10], [9, 12]]

# arr.sort()

# new = [arr[0]]

# for i in arr[1:]:
#     if i[0] <= new[-1][1]:
#         new[-1][1] = max(new[-1][1], i[1])
#     else:
#         new.append(i)

# print(new)

# 19. Search for an element in a rotated sorted array.
# arr = [4, 5, 6, 7, 0, 1, 2]

# target = 0

# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Element found at index:", i)
#         break
# else:
#     print("Element not found")

# 20. Find the longest consecutive sequence in an unsorted array.
# arr = [100, 4, 200, 1, 3, 2]

# arr.sort()

# count = 1
# longest = 1

# for i in range(1, len(arr)):
#     if arr[i] == arr[i-1] + 1:
#         count += 1
#     elif arr[i] != arr[i-1]:
#         count = 1

#     if count > longest:
#         longest = count

# print("Longest consecutive sequence length:", longest)

# 21.Find the trapped rainwater between elevation bars.
# arr = [3, 0, 2, 0, 4]

# water = 0

# for i in range(1, len(arr)-1):
#     left = arr[0]
#     right = arr[i]

#     for j in range(i, len(arr)):
#         if arr[j] > right:
#             right = arr[j]

#     for j in range(i):
#         if arr[j] > left:
#             left = arr[j]

#     if left < right:
#         water = water + left - arr[i]
#     else:
#         water = water + right - arr[i]

# print("Trapped water:", water)

# 22.Find the median of two sorted arrays in O(log(m+n)) time.
# a = [1, 3]
# b = [2, 4]

# c = a + b
# c.sort()

# n = len(c)

# if n % 2 == 0:
#     median = (c[n//2 - 1] + c[n//2]) / 2
# else:
#     median = c[n//2]

# print("Median:", median)

# 23. Find the maximum product of a contiguous subarray.
# arr = [2, 3, -2, 4]

# maximum = arr[0]
# current = arr[0]

# for i in arr[1:]:
#     if i > current * i:
#         current = i
#     else:
#         current = current * i

#     if current > maximum:
#         maximum = current

# print("Maximum product:", maximum)

# 24. Find the smallest missing positive integer from an unsorted array.
# arr = [3, 4, -1, 1]

# i = 1

# while i in arr:
#     i = i + 1

# print("Smallest missing positive:", i)

# 25.Count the number of subarrays whose sum equals K
# def count_subarrays(arr, k):
#     count = 0

#     for i in range(len(arr)):
#         total = 0

#         for j in range(i, len(arr)):
#             total += arr[j]

#             if total == k:
#                 count += 1

#     return count


# arr = [1, 2, 3, -2, 2]
# k = 3

# print(count_subarrays(arr, k))

# 26.Find the longest increasing subsequence in an array.
# def longest_increasing(arr):
#     n = len(arr)
#     dp = [1] * n

#     for i in range(n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)

#     return max(dp)


# arr = [10, 9, 2, 5, 3, 7, 101, 18]

# print(longest_increasing(arr))

# 27.Solve the Coin Change problem using dynamic programming.
# coins = [1, 2, 5]
# amount = 11

# dp = [float('inf')] * (amount + 1)

# dp[0] = 0

# for i in range(1, amount + 1):
#     for coin in coins:
#         if i >= coin:
#             dp[i] = min(dp[i], dp[i - coin] + 1)

# if dp[amount] == float('inf'):
#     print(-1)
# else:
#     print(dp[amount])

# 28.Solve the Word Break problem using dynamic programming.

# s = "ilikepython"

# word_dict = ["i", "like", "python"]

# dp = [False] * (len(s) + 1)

# dp[0] = True

# for i in range(1, len(s) + 1):
#     for j in range(i):
#         if dp[j] and s[j:i] in word_dict:
#             dp[i] = True
#             break

# print(dp[len(s)])

# 29. Find the minimum number of jumps required to reach the last index.
# arr = [2, 3, 1, 1, 4]

# jumps = 0
# i = 0

# while i < len(arr) - 1:
#     i = i + arr[i]
#     jumps += 1

# print(jumps)

# 30.Find the maximum profit from buying and selling stocks with multiple transactions
# prices = [7, 1, 5, 3, 6, 4]

# profit = 0

# for i in range(1, len(prices)):
#     if prices[i] > prices[i-1]:
#         profit += prices[i] - prices[i-1]

# print(profit)

# 31.Implement an LRU Cache with O(1) time complexity for get() and put().
# from collections import OrderedDict

# cache = OrderedDict()
# capacity = 3

# # Put elements
# cache[1] = 10
# cache[2] = 20
# cache[3] = 30

# print(cache)

# # Get element
# key = 2

# if key in cache:
#     value = cache.pop(key)
#     cache[key] = value
#     print("Value:", value)

# # Put new element
# key = 4
# value = 40

# if key in cache:
#     cache.pop(key)
# elif len(cache) >= capacity:
#     cache.popitem(last=False)

# cache[key] = value

# print(cache)

# 32.Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).
# stack = []
# min_stack = []

# # Push
# for i in [5, 3, 7, 2]:
#     stack.append(i)

#     if not min_stack or i <= min_stack[-1]:
#         min_stack.append(i)

# print("Stack:", stack)

# # Pop
# x = stack.pop()

# if x == min_stack[-1]:
#     min_stack.pop()

# print("Top:", stack[-1])
# print("Minimum:", min_stack[-1])


# 33.Find the number of islands in a 2D matrix using DFS or BFS.
# grid = [
#     [1, 1, 0, 0],
#     [1, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 0, 0, 0]
# ]

# rows = len(grid)
# cols = len(grid[0])

# count = 0

# for i in range(rows):
#     for j in range(cols):

#         if grid[i][j] == 1:
#             count += 1

#             stack = [(i, j)]

#             while stack:
#                 x, y = stack.pop()

#                 if x < 0 or x >= rows or y < 0 or y >= cols:
#                     continue

#                 if grid[x][y] == 0:
#                     continue

#                 grid[x][y] = 0

#                 stack.append((x + 1, y))
#                 stack.append((x - 1, y))
#                 stack.append((x, y + 1))
#                 stack.append((x, y - 1))

# print("Number of islands:", count)

# 34.Find the shortest path in a weighted graph using Dijkstra's algorithm.
# graph = {
#     'A': {'B': 4, 'C': 2},
#     'B': {'A': 4, 'C': 1, 'D': 5},
#     'C': {'A': 2, 'B': 1, 'D': 8},
#     'D': {'B': 5, 'C': 8}
# }

# distance = {'A': 0, 'B': float('inf'), 'C': float('inf'), 'D': float('inf')}

# visited = []

# while len(visited) < len(graph):

#     min_node = None

#     for node in graph:
#         if node not in visited:
#             if min_node is None or distance[node] < distance[min_node]:
#                 min_node = node

#     visited.append(min_node)

#     for neighbour, weight in graph[min_node].items():
#         new_distance = distance[min_node] + weight

#         if new_distance < distance[neighbour]:
#             distance[neighbour] = new_distance

# print(distance)

# 35.Detect a cycle in a directed and undirected graph
# graph = {
#     0: [1, 2],
#     1: [0, 2],
#     2: [0, 1, 3],
#     3: [2]
# }

# visited = set()
# cycle = False

# for start in graph:

#     if start not in visited:

#         stack = [(start, -1)]

#         while stack:
#             node, parent = stack.pop()

#             if node in visited:
#                 continue

#             visited.add(node)

#             for neighbour in graph[node]:

#                 if neighbour not in visited:
#                     stack.append((neighbour, node))

#                 elif neighbour != parent:
#                     cycle = True

# print("Cycle found" if cycle else "No cycle")

# 36.Implement topological sorting for a directed acyclic graph.
# graph = {
#     0: [2, 3],
#     1: [3],
#     2: [4],
#     3: [4],
#     4: []
# }

# indegree = [0] * 5

# for i in graph:
#     for j in graph[i]:
#         indegree[j] += 1

# queue = []

# for i in range(5):
#     if indegree[i] == 0:
#         queue.append(i)

# result = []

# while queue:
#     node = queue.pop(0)
#     result.append(node)

#     for neighbour in graph[node]:
#         indegree[neighbour] -= 1

#         if indegree[neighbour] == 0:
#             queue.append(neighbour)

# print("Topological Order:", result)

# 37.Solve the N-Queens problem using backtracking
# n = 4

# board = [[0]*n for i in range(n)]

# def solve(row):
#     if row == n:
#         return True

#     for col in range(n):

#         safe = True

#         for i in range(row):
#             if board[i][col] == 1:
#                 safe = False

#         i = row-1
#         j = col-1

#         while i >= 0 and j >= 0:
#             if board[i][j] == 1:
#                 safe = False
#             i -= 1
#             j -= 1

#         i = row-1
#         j = col+1

#         while i >= 0 and j < n:
#             if board[i][j] == 1:
#                 safe = False
#             i -= 1
#             j += 1

#         if safe:
#             board[row][col] = 1

#             if solve(row+1):
#                 return True

#             board[row][col] = 0

#     return False


# solve(0)

# for row in board:
#     print(row)

# 38.Generate all permutations of a given string or array without duplicates.
# arr = [1, 2, 3]

# import itertools

# result = list(itertools.permutations(arr))

# for i in result:
#     print(i)

# 39.Serialize and deserialize a binary tree.
# # Binary Tree
# tree = [1, 2, 3, None, None, 4, 5]

# # Serialize
# data = ""

# for i in tree:
#     data += str(i) + ","

# print("Serialized:", data)

# # Deserialize
# result = data.strip(",").split(",")

# new_tree = []

# for i in result:
#     if i == "None":
#         new_tree.append(None)
#     else:
#         new_tree.append(int(i))

# print("Deserialized:", new_tree)

# 40.Find the lowest common ancestor of two nodes in a binary tree
# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.left = None
#         self.right = None


# def lca(root, n1, n2):

#     if root is None:
#         return None

#     if root.data == n1 or root.data == n2:
#         return root

#     left = lca(root.left, n1, n2)
#     right = lca(root.right, n1, n2)

#     if left and right:
#         return root

#     if left:
#         return left

#     return right


# # Create Binary Tree
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# result = lca(root, 4, 5)

# print("Lowest Common Ancestor:", result.data)

