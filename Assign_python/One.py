data = [10, 20, 30, 40, 50, 20, 30, 60, 70, 80, 90]

#1.	Use append() to add [100, 110] as a single element. 
data.append([100,110])
print(data)

#2.	Use extend() to add elements 120, 130 separately. 
data.extend([120,130])
print(data)
# 3.	Insert 25 at index 2 using insert(). 
data.insert(2,25)
print(data)

# 4.	Remove the first occurrence of 20 using remove(). 
data.remove(20)
print(data)
# 5.	Remove the last element using pop() and store it. 
removed_number= data.pop()
print ("removed number: ", removed_number )
print(data)
# 6.	Count how many times 30 appears using count(). 
print(data.count(30))
# 7.	Find index of first 40 using index(). 
print(data.index(40))
# 8.	Reverse the list using reverse(). 
data.reverse()
print(data)
# 9.	Sort only the top-level elements (ignore nested list) using sort() — explain issue. 
data.remove([100,110])
data.sort()
print(data)