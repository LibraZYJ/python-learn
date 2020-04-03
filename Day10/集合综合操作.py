"""
集合综合操作
@Date 2020.4.3
Author：Yujie_zhao
"""
# 创建集合的各种方法
# 字面量语法
set1 = {1, 2, 3, 4, 6, 2}
print(set1)
print('Length =', len(set1))
# 构造器语言
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 推导式语法
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 集合天机删除元素
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)  # {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12}
print(set3.pop())  # 1
print(set3)  # {2, 3}
# 交集、并集、差集、对称差运算
print(set1 & set2)  # {1, 2, 3}
# print(set1.intersection(set2))
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
# print(set1.union(set2))
print(set1 - set2)  # {4, 5}
# print(set1.difference(set2))
print(set1 ^ set2)  # {4, 5, 6, 7, 8, 9, 11, 12}
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)  # False
# print(set2.issubset(set1))
print(set3 <= set1)  # True
# print(set3.issubset(set1))
print(set1 >= set2)  # False
# print(set1.issuperset(set2))
print(set1 >= set3)  # True
# print(set1.issuperset(set3))
