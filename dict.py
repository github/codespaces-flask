# 创建一个空字典
fruits = {}

# 创建一个包含一些水果及其数量的字典
fruits = {
    'apple': 10,
    'banana': 5,
    'orange': 8
}
# 访问字典中的值
print(fruits['apple'])  # 输出: 10
# 添加一个新的键值对
fruits['mango'] = 15

# 更新一个已有的键值对
fruits['banana'] = 7

print(fruits)
# 输出: {'apple': 10, 'banana': 7, 'orange': 8, 'mango': 15}
# 删除一个键值对
del fruits['orange']

print(fruits)
# 输出: {'apple': 10, 'banana': 7, 'mango': 15}

# 遍历字典中的键值对
for fruit, quantity in fruits.items():
    print(f"The quantity of {fruit} is {quantity}")

# 检查键是否在字典中
if 'apple' in fruits:
    print("Apple is in the dictionary")

if 'grape' not in fruits:
    print("Grape is not in the dictionary")

# 获取所有的键
keys = fruits.keys()
print(keys)  # 输出: dict_keys(['apple', 'banana', 'mango'])

# 获取所有的值
values = fruits.values()
print(values)  # 输出: dict_values([10, 7, 15])