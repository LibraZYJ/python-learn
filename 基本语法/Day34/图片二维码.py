"""
Myqr制作二维码
pip3 install qrcode
pip3 install myqr
"""
from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont


def img_code():
    myqr.run(words='https://niit-zyj.oss-cn-beijing.aliyuncs.com/img/e58f383f-de99-46ff-93d8-526f1608463d.png',
             version=1,
             level='H',
             picture='./res/img/beijin.jpg',
             colorized=True,
             contrast=1.0,
             brightness=1.0,
             save_name='erweima.png',
             save_dir=os.getcwd() + '/res/img/')


def draw():
    img = Image.open('./res/img/erweima.png')
    w, h = img.size
    txt = 'yujie'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./res/font/SimHei.ttf', 26)
    draw.text((w/2-100, 10), txt, (0, 0, 0), font=font)
    img.save('./res/img/code3.png')


if __name__ == '__main__':
    img_code()
    draw()
