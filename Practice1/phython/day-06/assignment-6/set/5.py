#5. Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#Expected output:
#{70, 10, 20, 60}
s1=set1|set2
s2=set1&set2
print(s1-s2)
