# -*- coding: utf-8 -*-
"""
=========================
识别图片中的文字
=========================

"""
import os

from PIL import Image
import pytesseract

def sample():
    #主程序
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    #语言，训练数据
    tessdata_dir_config = r'C:\Program Files (x86)\Tesseract-OCR\tessdata'
    image_object = Image.open('img.jpg')
    aa = pytesseract.image_to_string(image_object, lang='chi_sim', config=tessdata_dir_config)
    with open('aa.txt', 'wt') as f:
        f.write(aa)
    bb = 1

def main():
    #主程序
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    #语言，训练数据
    tessdata_dir_config = r'C:\Program Files (x86)\Tesseract-OCR\tessdata'
    pics = all_pic()
    print(len(pics))
    i = 0
    for pic in pics:
        i += 1
        print(i)
        image_object = Image.open(pic)
        aa = pytesseract.image_to_string(image_object, lang='chi_sim', config=tessdata_dir_config)
        file_name = 'stroke_2.txt'
        if not os.path.exists(file_name):
            with open(file_name, 'wt') as file: #, encoding='utf-8'
                file.writelines('================\n' + pic + '\n================\n')
                file.write(aa + '\n')
        else:
            with open(file_name, 'at') as file:
                file.writelines('================\n' + pic + '\n================\n')
                file.write(aa + '\n')

def all_pic():
    disk = os.getcwd()
    path = disk[0] + r':/Downloads/卒中中心手册' #os.path.join(disk, 'json_data')
    pics = list()
    for parent, _, filenames in os.walk(path):
        #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        pics = [os.path.join(parent, file) for file in filenames]
        #只读取根目录下的文件
        break
    return pics

if __name__ == '__main__':
    main()