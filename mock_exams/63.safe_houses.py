'''
Safe Houses
'''

spawns = int(input())
safe_houses = sorted([int(x) for x in input().split()])
gr_distance = safe_houses[0]  # Declaring the first distance from the start
for i in range(1, len(safe_houses)):  # Traversing the distances in between the safes
    cur_distance = (safe_houses[i] - safe_houses[i - 1]) // 2
    if gr_distance < cur_distance:
        gr_distance = cur_distance

if gr_distance < spawns - 1 - safe_houses[-1]:  # Checking also the last spawn
    gr_distance = spawns - 1 - safe_houses[-1]
print(gr_distance)
