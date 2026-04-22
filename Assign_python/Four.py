student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

# 1.	Access name using get(). 
print(student.get("name"))
# 2.	Add new key grade using assignment. 
student.update({"grade":"A"})
print(student)
# 3.	Update age using update(). 
student.update({"age":22})
print(student)
# 4.	Remove age using pop(). 
student.pop("age")
print(student)
# 5.	Remove last inserted item using popitem(). 
student.popitem()
print(student)
# 6.	Get all keys using keys().
print(student.keys())
# 7.	Get all values using values(). 
print(student.values())
# 8.	Get all items using items(). 
print(student.items())
# 9.	Use setdefault() to add city. 
student.setdefault("city","Chennai")
print(student)
# 10.	Merge another dictionary using update().
student_info = {"class": 10,"section":"b"} 
student.update(student_info)
print(student)

