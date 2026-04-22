s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

# 1.	Add element 60 using add() and explain why duplicates are not allowed in sets.
s1.add(60) 
s2.add(60)
# because sets dosen't allow duplicate vaules and repeated vaules into sets and holds the unique values.
print(s1)
print(s2)
# 2.	Add multiple elements [70, 80, 90] using update() and explain difference from add(). 
s1.update([70,80,90])
# add only add single iteam in set but using update we can update as set 
print(s1)
# 3.	Remove element 20 using remove() and explain what happens if element is not found. 
s1.remove(20)
# if the number is not in set what we called to remove using remove(), it throw an error.
print(s1)
# 4.	Remove element 100 safely using discard() and explain why it does not throw error.
s1.discard(100)
# it doesn't throw error like remove(), if the number that we called is not existing in set
print(s1)
# 5.	Remove and return a random element using pop() and explain unpredictability. 
s1.pop()
# pop will remove a last item but in sets it doesn't like that because it is not ordered in sequence so, it will not remove the last element in it. 
print(s1)
# 6.	Create a copy of set using copy() and modify the copy — verify original remains unchanged.
s1_copy = s1.copy()
s1_copy.add(303)
print("s1=",s1)
print("s1_copy=", s1_copy)
# 7.	Clear all elements using clear() and check length using len(). 
s1_copy.clear()
print(len(s1_copy))
print(len(s1))
# 8.	Convert a list with duplicates [1,2,2,3,3,4] into a set and explain deduplication. 
s3 = [1,2,2,3,3,4]
duplicates = set(s3)
print(duplicates)
# 9.	Convert the set into a list and sort it (since sets are unordered). 
s4 = sorted(list(s3))
print("sorted list:",s4)
