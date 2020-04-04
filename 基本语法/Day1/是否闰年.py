# 输入年份，如果是软年输入True，否则False


year = int(input('请输入年丰：'))
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap)