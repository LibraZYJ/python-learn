"""
在控制台输出跑马灯演示
"""
import os
import time


def main():
    content = '好彩妹说：好彩自然来！'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
