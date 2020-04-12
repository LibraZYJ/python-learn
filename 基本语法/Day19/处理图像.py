"""
使用Pillow来处理图像：pip3 install Pillow
"""

# 图片相关
from io import BytesIO
from PIL import Image
import requests as req
from PIL import Image, ImageFilter
# 系统相关
import os

# 打开图片， 打印其格式、大小、图片类型
img = Image.open('./res/img/zek.jpg')
# print(img.format, img.size, img.mode)

# 直接可以复制
Image.open('./res/img/zek.jpg').save('./res/img/zek-1.jpg')

# 用thumbnail() 方法为其生成原尺寸1/3大小的缩略图
w, h = img.size
img.thumbnail((w//3, h//3))
img.save('./res/img/缩略.jpg', 'jpeg')

# 使用filter() 滤镜，此处使用模糊效果
img = Image.open('./res/img/zek.jpg')
img1 = img.filter(ImageFilter.BLUR)
img1.save('./res/img/模糊.jpg', 'jpeg')

# 翻转
img = Image.open('./res/img/zek.jpg')
img1 = img.transpose(Image.FLIP_LEFT_RIGHT)
img1.save('./res/img/左右翻转.jpg', "JPEG")
img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
img1.save('./res/img/上下翻转.jpg', "JPEG")
img1 = img.transpose(Image.ROTATE_90)
img1.save('./res/img/旋转90度.jpg', "jpeg")
img1 = img.transpose(Image.ROTATE_180)
img1.save('./res/img/旋转180度.jpg', "jpeg")

# 遍历目录和文件
list = os.listdir('./res/img')
# print(list)
for file in list:
    if os.path.splitext(file)[-1] == '.jpg':
        print(os.path.splitext(file))       # file 是元组 -> ('1-1', '.jpg')
        print(os.path.splitext(file)[0])       # 取到文件名
        print(os.path.splitext(file)[-1])       # 取到文件后缀

# 遍历所有
for root, dirs, files in os.walk("res"):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

# 处理网络图片
resp = req.get(
    'https://niit-zyj.oss-cn-beijing.aliyuncs.com/img/18c47958-31eb-424e-a8f3-0c3f2267c4f1.jpg')
Image = Image.open(BytesIO(resp.content))
# 在此之前可以做相关处理
Image.save('./res/download/test.png')
