"""
类和对象
@Date 2020.04.08
"""


class Student(object):

    # __init_是一个特殊方法用于再创建对象时进行初始化操作
    # 通过这个方法我们以为学生对象绑定name 和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《猫和老鼠》.' % self.name)
        else:
            print('%s正在观看3D大片.' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('某某', 28)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('某某某', 15)
    stu2.study('Python')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
