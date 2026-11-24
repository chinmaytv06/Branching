# 1.  Extract all even numbers from a nested list and store them in a new list.
    
data = [[10, 15, 20], [25, 30, 35], [40, 45, 50]]
even = []
for num in data:
  for j in num:
    if j%2 == 0:
      even.append(j)
# print(even)