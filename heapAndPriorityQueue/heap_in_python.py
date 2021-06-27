import heapq

import _heapq

# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
# import heapq

# initializing list
li = [5, 7, 9, 1, 3]

print(li)
_heapq.heapify(li)  # max heap
print(li)

_heapq._heapify_max(li)  # max heap
print(li)

print(_heapq.heappush(li, 0))
print(li)

print(_heapq.heappushpop(li, 10))
print(li)

print(_heapq.heappop(li))
print(li)

print(_heapq.heapreplace(li, -1))
print(li)

aa = [120, 20, 90, -20]
heapq.heapify(aa)  # min heap
print(aa)
heapq.heappush(aa, 500)
heapq.heappop(aa)

ll = [1, 2, -1, 3]
merged = heapq.merge(aa, ll)
print(next(merged))

print(heapq.nsmallest(2, aa))  # 20, 90
print(heapq.nlargest(2, aa))  # 500,120

# for max heap using heapq, insert with negative value
