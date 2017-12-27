# -*- coding: utf-8 -*-
"""
=====================
知识图谱-卒中中心手册

分词-概念-实体
=====================
第八章
第四节
第五节



"""
import os
import json
import csv

import jieba
import nltk

def kg_segmentation():
    #读入文本
    disk = os.getcwd()
    file_name = disk + r'\data\stroke_2.txt'
    jieba.load_userdict(disk + r'\data\dic_1.txt') 
    if os.path.exists(file_name):
        with open(file_name, 'rt', encoding='gbk') as file:
            text = file.read()
    #分词
    seg_list = jieba.cut(text)
    return seg_list

def fd():
    seg_list = kg_segmentation()
    #展示分词
    #print(", ".join(seg_list))
    #统计词频
    fd = nltk.FreqDist(seg_list)
    keys = fd.keys()
    item = fd.items()
    dicts = dict(item)
    header = ['key', 'value']
    for key, value in dicts.items():
        dic = {'key': key, 'value': value}
        with open('aa.csv', 'a', newline='', encoding='gbk', errors='ignore') as csvfile:
            writer = csv.DictWriter(csvfile, header)
            writer.writerow(dic)

if __name__ == '__main__':
    seg_list = kg_segmentation()
    str_result = "/ ".join(seg_list)
    with open('restult.txt', 'wt') as file:
        file.write(str_result)
