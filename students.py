import json

# 读取 JSON 文件
with open('students.json', 'r') as file:
    students = json.load(file)

print(students)

# 遍历学生列表
for student in students:
    name = student['name']
    courses = student['courses']
    print(f"Student: {name}")
    print("Courses:")
    for course in courses:
        print(f" - {course}")

# 添加新学生
new_student = {
    "name": "Charlie",
    "age": 24,
    "courses": ["Art", "Design"]
}
students.append(new_student)

# 将更新后的数据写回到 JSON 文件
with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)

print("New student added.")

# 删除名为 "Bob" 的学生
students = [student for student in students if student['name'] != 'Bob']

# 将更新后的数据写回到 JSON 文件
with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)

print("Student 'Bob' deleted.")