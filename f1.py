# 2.  Remove duplicate elements from a nested list and create a single list containing unique elements.
    
data = [[10, 20, 30], [20, 40, 50], [10, 50, 60]]
uniq = []
for nums in data:
  for j in nums:
    if j not in uniq:
      uniq.append(j)
# print(uniq)