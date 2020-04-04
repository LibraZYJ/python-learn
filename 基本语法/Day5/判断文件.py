"""
判断自一组文件中图片的个数
Date:2020.3.29
Author:Yujie_Zhao
"""

def count_image(file_list):
    """
    判断一组文件的个数
    :param file_list：文件列表
    :return：图片数量
    """
    count = 0
    for file in file_list:
        if file.endswith('png') or file.endswith('jpg') or file.endswith('webp') or file.endswith('bmp'):
            count = count +1
    return count

# 调用函数 
img_list = ['1.jpg','2.md','3.bmp','4.webp','5.mp4','6.png']
result = count_image(img_list)
print('一共有',result,'个图片文件')